from framework.template import render


class Index:
    def __call__(self, request):
        return '200 OK', render('index.html')


class About:
    def __call__(self, request):
        return '200 OK', render('about.html')


class Contacts:
    def __call__(self, request):
        if request.get('method') == 'POST':
            return '200 OK', render('contacts.html')
        else:
            return '200 OK', render('contacts.html')
