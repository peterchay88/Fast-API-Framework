def build_request_headers(access_token, content_type_accept="application/json", **kwargs):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": content_type_accept
    }

    if "content_type" in kwargs:
        headers["Content-Type"] = kwargs["content_type"]
    return headers


