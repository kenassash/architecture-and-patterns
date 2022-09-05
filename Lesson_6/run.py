from wsgiref.simple_server import make_server

from framework.main import AppFramework
from views import routes

# class DebugApplication(AppFramework):
#
#     def __init__(self, routes_obj):
#         self.application = AppFramework(routes_obj)
#         super().__init__(routes_obj)
#
#     def __call__(self, env, start_response):
#         print('DEBUG MODE')
#         print(env)
#         return self.application(env, start_response)

# class FakeApplication(AppFramework):
#
#     def __init__(self, routes_obj):
#         self.application = AppFramework(routes_obj)
#         super().__init__(routes_obj)
#
#     def __call__(self, env, start_response):
#         start_response('200 OK', [('Content-Type', 'text/html')])
#         return [b'Hello from Fake']

application = AppFramework(routes)

# application = DebugApplication(routes)
# # application = FakeApplication(routes)

with make_server('', 8080, application) as httpd:
    print("Запуск на порту 8080...")
    httpd.serve_forever()
