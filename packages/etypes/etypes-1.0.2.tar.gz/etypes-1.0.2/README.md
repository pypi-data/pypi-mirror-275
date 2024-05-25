## ETYPES

This package allows for encrypting secret strings in python files in a human readable way using type hints. 
it also supports dynamic loading of python files which contain encrypted strings, providing the password via an environment variable
 
## Installation

`$ pip install etypes`

or

`$ poetry add etypes`

## Example
Define a variable with the type hint DecryptedSecret
```
from etypes import DecryptedSecret
SECRET_VAR: DecryptedSecret = "some-secret-value"
```

### encrypt
To encrypt the file, run the following

`$ etypes encrypt -p PASSWORD ./path/to/python_file.py`

or 

`$ etypes encrypt -pf ./path/to/password_file ./path/to/python_file.py`

```
from etypes import EncryptedSecret
SECRET_VAR: EncryptedSecret = "gAAAAABmT9yA6HQOXF4BM6gvUG_ryKqrXK9BEgRY2W4lNQvDNBVbiCEOz50-viDLEMXA71upgcGgRbqvC-IAltbjE8w5MbSooJN5EV-8sVe1q3LndfBNzEg="
```

### decrypt

`$ etypes decrypt -p PASSWORD ./path/to/python_file.py`

or 

`$ etypes v -pf ./path/to/password_file ./path/to/python_file.py`

To import this python file in your project and have it decrypt itself seamlessly when accessed

You must import the AutoLoader
```
# app/settings/secrets.py

from etypes import EncryptedSecret, AutoLoader
SECRET_VAR: EncryptedSecret = "gAAAAABmT9yA6HQOXF4BM6gvUG_ryKqrXK9BEgRY2W4lNQvDNBVbiCEOz50-viDLEMXA71upgcGgRbqvC-IAltbjE8w5MbSooJN5EV-8sVe1q3LndfBNzEg="

AutoLoader(password="SOME_ENV_VAR_WHICH_CONTAINS_PASSWORD", locals())
# or
AutoLoader(password_file="/path/to/your/secret_file", locals())

```
import your settings/secrets file normally.

```
# app/main.py

from .settings import secrets
print(secrets.SECRET_VAR)
```

Run your application providing the password declaring in your AutoLoader
`$ SOME_ENV_VAR_WHICH_CONTAINS_PASSWORD="PASSWORD" ./main.py`


> TODO: Add support for the environs package 
