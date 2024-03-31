from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello your are at poll index")
