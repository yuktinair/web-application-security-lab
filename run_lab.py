
from waitress import serve
from app import app, init_db


class HideServerVersion:
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        def custom_start_response(status, headers, exc_info=None):
            headers = [
                (name, value)
                for name, value in headers
                if name.lower() != "server"
            ]
            return start_response(status, headers, exc_info)

        return self.application(environ, custom_start_response)


if __name__ == "__main__":
    init_db()
    serve(
        HideServerVersion(app),
        host="127.0.0.1",
        port=5000
    )
