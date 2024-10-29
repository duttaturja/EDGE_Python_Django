from django.shortcuts import render, redirect
# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import permission_required


def profile_view(request):
    #template_name = 'profile_view.html'
    return render(request, 'profile_view.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        
    else:
        form = UserCreationForm()
        return render(request, 'register.html', {'form': form})
