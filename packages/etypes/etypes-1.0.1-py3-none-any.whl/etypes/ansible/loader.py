#################################################
#   [2024] Dan Brosnan dpjbrosnan@gmail.com     #
#################################################

from __future__ import absolute_import, division, print_function
import os

__metaclass__ = type

DOCUMENTATION = """
    vars: etypes
    version_added: "2.10"
    short_description: Load custom host vars from an encrypted python file
    description: Load custom host vars from an encrypted python file
    extends_documentation_fragment:
      - vars_plugin_staging
"""


try:
    import ansible
except ImportError:
    raise Exception("Requires ansible to be installed")

from ansible.plugins.vars import BaseVarsPlugin
from ansible.utils.vars import combine_vars

class VarsModule(BaseVarsPlugin):
    """Allows decryption of a etypes encrypted python file for use as ansible vars"""
    allow_extras = True
    REQUIRES_ENABLED = False
    is_stateless = True

    def load_found_files(self, loader, data, found_files):
        for found in found_files:
            new_data = loader.load_from_file(found, cache="all", unsafe=True)
            if new_data:  # ignore empty files
                data = combine_vars(data, new_data)
        return data

    def get_vars(self, loader, path, entities, cache=True):
        """parses the inventory file"""

        etypes_file = os.environ.get('ETYPES_FILE', None)
        if not etypes_file:
            raise Exception("ETYPES_FILE not specified")
        
        etypes_password = os.environ.get('ETYPES_PASSWORD', None)
        if not etypes_password:
            raise Exception("ETYPES_PASSWORD not specified")
        data = {}
        with open(etypes_file, 'r') as fp:
            source = fp.read()
            _locals = locals()
            exec(source, globals(), _locals)        
            data = dict(locals())

        remove = ['AutoLoader', 'EncryptedSecret', 'DecryptedSecret', '__annotations__', '_locals', 'cache', 'data', 'entities', 'etypes_file', 'etypes_password', 'fp', 'loader', 'path', 'self', 'source']
        for r in remove:
            try:
                del data[r]
            except KeyError:
                pass
        return data