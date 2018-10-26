def handler(req):
    """
    Echo the request back as a response.
    :param req: The request.
    :return: The response.
    """
    res = req
    return res

# TODO: Add a enterpoint handler and remove this.
req = req if req else 'Hello'
handler(req)
