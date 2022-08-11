from datetime import date
from views import Index, Page, Contact, Examples, AnotherPage


# front controller
def secret_front(request):
    request['data'] = date.today()


def other_front(request):
    request['key'] = 'key'


fronts = [secret_front, other_front]

routes = {
    '/': Index(),
    '/page/': Page(),
    '/contact/': Contact(),
    '/examples/': Examples(),
    '/anotherPage/': AnotherPage(),
}