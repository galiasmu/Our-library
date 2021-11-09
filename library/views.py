from django.http import HttpResponse


def index(request):
    return HttpResponse("Hola, esto es un pito grande.")
