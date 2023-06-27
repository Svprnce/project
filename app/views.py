from django.shortcuts import render
from django.http import HttpResponse
from .models import Books

# Create your views here.

def index(request):
    return HttpResponse("Hello Index")

def view(request):
    Booklist = Books.objects.all()
    print(Booklist)
    return render(request, 'app/view.html', {
        'books' : Booklist
    })

