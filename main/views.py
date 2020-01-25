from django.http import HttpResponse

def hello(request):
    return HttpResponse('<h1>Helllo world</h1>')