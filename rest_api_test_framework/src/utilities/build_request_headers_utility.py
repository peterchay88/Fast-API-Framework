def build_request_headers(access_token, content_type_accept="application/json",
                          additonal_content_header=False, **kwargs):
    if additonal_content_header:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": content_type_accept,
            "Content-Type": content_type_accept
        }
    elif not additonal_content_header:
        headers = {
            "Authorization": f"Bearer {access_token}",
            "Accept": content_type_accept
        }
    headers.update(kwargs)  # Update headers with additional keyword arguments
    return headers


