import urllib.parse


def url_encode_string(string):
    """
    This function takes a string input and returns the URL-Encoded format of it back
    :param string:
    :return:
    """
    converted_string = urllib.parse.quote(string)
    return converted_string
