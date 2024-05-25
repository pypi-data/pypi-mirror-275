import os
import ast

from typing import get_type_hints

from etypes import EncryptedSecret
from etypes.processor import decrypt_value, derive_key
from etypes.exceptions import NoPasswordProvidedError, NoPasswordFileProvidedError

class AutoLoader:
    password = None
    password_file = None

    def process(self, value):
        key = derive_key(self.password)
        return decrypt_value(key, ast.Constant(value))

    def walk(self, node, annotations):
        if isinstance(node, dict):
            for key, value in node.items():
                if key[0] == "_":
                    # ignore private and builtins
                    continue

                if isinstance(value, dict):
                    node[key] = self.walk(value, annotations)
                if isinstance(value, list):
                    for v in value:
                        if isinstance(value, EncryptedSecret):
                            node[key] = self.process(v)

                if key in annotations:
                    if annotations[key] == EncryptedSecret:
                        node[key] = self.process(value)

        return node

    
    def __init__(self, locals=None, password_var_name=None, password_file=None):

        if not type(locals) == dict:
            raise Exception("Locals must be a dict")
        
        if not password_file and not password_var_name:
            raise Exception("You must specify a password_var_name or password_file")

        if password_var_name and not password_file:
            self.password = os.environ.get(password_var_name, None)
            if not self.password:
                raise NoPasswordProvidedError(
                    f"No password found in environment variable: {password_var_name}"
                )

        if not password_var_name and password_file:
            if not os.path.isfile(password_file):
                raise NoPasswordFileProvidedError(f"Could not find {password_file}")
            password = open(password_file,'r').read()
            if not password:
                raise NoPasswordProvidedError(f'No password found in {password_file}')
            self.password = password

        annotations = locals["__annotations__"]
        self.walk(locals, annotations)
