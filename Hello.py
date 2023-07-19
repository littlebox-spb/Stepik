from urllib.parse import urlparse, parse_qs


def wsgi_first(environ, start_response):
    body = []
    status = "200 OK"
    headers = [("Content-Type", "text/plain")]
    start_response(status, headers)
    return body


s = "https://stepik.org/lesson/14826/step/11?unit=4175"

print(urlparse(s))
print(parse_qs(s[2:]))
