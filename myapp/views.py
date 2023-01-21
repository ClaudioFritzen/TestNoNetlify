
# Create your views here.
from django.shortcuts import render, redirect 
from .models import Person
from .forms import ProfilePictureForm

from django.contrib import messages

def add_person(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            photo = form.cleaned_data.get('photo')
            person = Person(name=name, photo=photo)
            person.save()
            messages.success(request, 'Person added successfully!')
            return redirect('profile', person_id=person.id)
        else:
            messages.error(request, 'Please correct the errors')
    else:
        form = ProfilePictureForm()
    return render(request, 'add_person.html', {'form': form})

""" 
from django import forms
from PIL import Image

class ProfilePictureForm(forms.Form):
    picture = forms.ImageField()

    def clean_picture(self):
        picture = self.cleaned_data.get("picture")
        if not picture:
            raise forms.ValidationError("No image was selected")
        try:
            image = Image.open(picture)
            width, height = image.size
            if width > 180 or height > 180:
                raise forms.ValidationError("The image size should be 180x180")
        except:
            raise forms.ValidationError("Invalid image format")
        return picture
 """

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

