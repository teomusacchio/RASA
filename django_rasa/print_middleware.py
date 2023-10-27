# print_middleware.py
class PrintRedirectURLMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if 'google' in request.path:
            with open("redirect_log.log", "a") as f:  # Scrive nel file redirect_log.log nella root del tuo progetto
                f.write(f"Requested URL: {request.path}\n")
        response = self.get_response(request)
        return response

