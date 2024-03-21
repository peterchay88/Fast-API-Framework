def build_request_headers(access_token, content_type="application/json", **kwargs):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": content_type
    }
    headers.update(kwargs) # Update headers with additional keyword arguments
    return headers

