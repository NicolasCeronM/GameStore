from django.shortcuts import render
from . forms import CustomUserCreationForm
# Create your views here.


def home (request):

    return render(request,'home.html')

def registro(request):

    form = CustomUserCreationForm

    data = {
        'form': form
    }

    return render(request,'registration/registro.html', data)
