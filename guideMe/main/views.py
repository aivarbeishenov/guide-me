from django.shortcuts import render, redirect
from .forms import TripForm



def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def build_trip(request):
    error = ''
    if request.method == 'POST':
        form = TripForm(request.POST)
        form.save()
        print(form)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Не правильно заполнена форма'

    form = TripForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/build_trip.html', data)
