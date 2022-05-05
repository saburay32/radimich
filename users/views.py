from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import UserOurRegistration, ProfileImage, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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
    return render(request, 'users/registration.html', {'form': form, 'title': 'Регистрация пользователя'})

@login_required
def profile(request):
    img_profile = ProfileImage()
    update_user = UserUpdateForm()
    data = {
        'img_profile': img_profile,
        'update_user': update_user
    }
    return render(request, 'users/profile.html',data)
