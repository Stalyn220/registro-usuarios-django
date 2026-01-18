from django.shortcuts import render, redirect
from .forms import RegistroForm
from django.contrib.auth.models import User

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('registro')
    else:
        form = RegistroForm()

    return render(request, 'registro.html', {'form': form})
