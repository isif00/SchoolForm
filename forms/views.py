from django.shortcuts import render
from .forms import UsersForm
# Create your views here.


def display(request):
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            print("done")
    else:
        form = UsersForm()

    return render(request, "registrations.html", {'form': form})