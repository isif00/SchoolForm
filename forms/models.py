from django.db import models


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

class Users(models.Model):
    full_name = models.CharField(max_length=200)
    discord_id = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    first_training = models.CharField(max_length=20, choices=TRAININGS_CHOICES, default='green')
    second_training = models.CharField(max_length=20, choices=TRAININGS_CHOICES, default='green')
    pub_source = models.CharField(max_length=20, choices=SOCIAL_MEDIA_APPS, default='green')

    def __str__(self) -> str:
        return self.full_name
