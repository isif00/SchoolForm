from django import forms
from .models import Users

TRAININGS_CHOICES = (
    ('web_dev','Web Dev'),
    ('linux', 'Linux and git'),
    ('python', 'Python'),
    ('3d', '3D modeling '),
    ('design', 'Design',),
)

SOCIAL_MEDIA_APPS = (
    ('facebook','Facebok'),
    ('instagram','Instagram'),
    ('linkedin','Linked In'),
    ('discord','Discord'),
    ('others','Others'),
)

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = '__all__'
    