import datetime


def handle(req):
    """handle a request to the function
    Args:
        req (str): request body
    """
    now = datetime.datetime.now()
    print("hello there 2")
    print(str(req))
    return  str(now)
