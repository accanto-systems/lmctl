import click
from typing import List

default_pwd_help = 'TNCO (ALM) password used for authenticating '\
    + '(only required if the environment is secure and a username has been included in your configuration file with no password)'

def tnco_pwd_option(options: List = ['--pwd'], var_name: str = 'pwd', help: str = default_pwd_help):
    def decorator(f):
        return click.option(*options, var_name, 
                        help=help
                        )(f)
    return decorator

default_secret_help = 'TNCO (ALM) client secret used for authenticating '\
    + '(only required if the environment is secure and a client_id has been included in your configuration file with no client_secret)'

def tnco_client_secret_option(options: List = ['--client-secret'], var_name: str = 'client_secret', help: str = default_secret_help):
    def decorator(f):
        return click.option(*options, var_name, 
                        help=help
                        )(f)
    return decorator