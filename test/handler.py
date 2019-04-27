import datetime
import os


def get_secret(name):
    try:
        with open('/var/openfaas/secrets/test', 'r') as secret_file:
            return secret_file.read()
    except IOError:
        return "Could not read"


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    now = datetime.datetime.now()
    print("hello there 2")
    x = get_secret('test')
    print(str(req))
    print(str(x))
    return str(now)
