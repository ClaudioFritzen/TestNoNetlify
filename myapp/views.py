
# Create your views here.
from django.shortcuts import render, redirect 
from .models import Person

def add_person(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        photo = request.FILES.get('photo')
        person = Person(name=name, photo=photo)
        person.save()
        return redirect('profile', person_id=person.id)
    return render(request, 'add_person.html')

def profile(request, person_id):
    person = Person.objects.get(id=person_id)
    return render(request, 'profile.html', {'person':person})

def update_profile(request, person_id):
    person = Person.objects.get(id=person_id)
    if request.method == 'POST':
        person.name = request.POST.get('name')
        if request.FILES.get('photo'):
            person.photo = request.FILES.get('photo')
        person.save()
        return redirect('profile', person_id=person_id)
    return render(request, 'update_profile.html', {'person': person})
