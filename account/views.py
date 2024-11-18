from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django_email_verification import send_email

User = get_user_model()
from .forms import UserCreateForm


# Register new user
def register_user(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            user_email = form.cleaned_data.get('email')
            user_username = form.cleaned_data.get('username')
            user_password = form.cleaned_data.get('password1')
            # Create new user
            user = User.objects.create_user(
                username=user_username, email=user_email, password=user_password
            )
            user.is_active = False
            send_email(user)

            return redirect('/account/email-verification-sent/')
    else:
        form = UserCreateForm()
    return render(request, 'account/registration/register.html', {'form': form})
