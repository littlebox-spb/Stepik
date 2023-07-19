from urllib.parse import parse_qs


def wsgi_first(environ, start_response):
    body = parse_qs(environ.get('QUERY_STRING')
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return body
