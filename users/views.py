from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserOurRegistration
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserOurRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.clean_password2()
            messages.success(request, f'Аккаунт  {username} был успешно создан')
            return redirect('user')
    else:
        form = UserOurRegistration
    return render(request, 'users/registration.html', {'form': form, 'title':'Регистрация пользователя'})
