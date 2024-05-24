import os
import ast

from typing import get_type_hints

from etypes import EncryptedString
from etypes.processor import decrypt_value, derive_key


class AutoLoader:
    password = None

    @classmethod
    def process(cls, value):
        key = derive_key(cls.password)
        return decrypt_value(key, ast.Constant(value))

    @classmethod
    def walk(cls, node, annotations):
        if isinstance(node, dict):
            for key, value in node.items():
                if key[0] == "_":
                    # ignore private and builtins
                    continue

                if isinstance(value, dict):
                    node[key] = cls.walk(value, annotations)
                if isinstance(value, list):
                    for v in value:
                        if isinstance(x, EncryptedString):
                            node[key] = cls.process(v)

                if key in annotations:
                    if annotations[key] == EncryptedString:
                        node[key] = cls.process(value)

        return node

    @classmethod
    def __init__(cls, environment_variable, locals):

        cls.password = os.environ.get(environment_variable, None)
        if not cls.password:
            raise Exception(
                f"No password provided in environment variable {environment_variable}"
            )

        annotations = locals["__annotations__"]
        cls.walk(locals, annotations)
