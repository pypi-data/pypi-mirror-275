import re

# Set the X-XSS-Protection header to 0
import wsgiref.simple_server
def application(environ, start_response):
    start_response('200 OK', [('X-XSS-Protection', '0')])

    # Check if there is any input
    name = environ.get('QUERY_STRING')
    if name and 'name=' in name:
        name = re.sub(r'<(.*)s(.*)c(.*)r(.*)i(.*)p(.*)t', '', name.split('=')[1])
        html = f"<pre>Hello {name}</pre>"
        return [html.encode()]
    else:
        return [b'']

if __name__ == '__main__':
    httpd = wsgiref.simple_server.make_server('', 8000, application)
    print(f"Serving on port 8000...")
    httpd.serve_forever()

