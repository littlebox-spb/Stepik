from urllib.parse import urlparse, parse_qs


def wsgi_first(environ, start_response):
    body = []
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return body


s = "get https://github.com/?a=1&a=2&b=3"

print(urlparse(s))
print(parse_qs(s[2:]))
