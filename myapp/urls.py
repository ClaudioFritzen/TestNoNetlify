from django.urls import path
from . import views


urlpatterns = [
    path('add_person/', views.add_person, name='add_person'),
    path('profile/<int:person_id>/', views.profile, name='profile'),
    path('update_profile/<int:person_id>/', views.update_profile, name='update_profile'),
]

