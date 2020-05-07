from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')

def register(request):
    return render(request, 'basic_app/register.html')
