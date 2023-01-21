
# Create your views here.
from django.shortcuts import render
from .models import Person

def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES.get('photo')
        person = Person(name=name, photo=photo)
        person.save()
    return render(request, 'add_person.html')
