from django.urls import path
from .views import display
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', display, name="display")
]

