# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

# Login view
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome {user.username}!')
            return redirect('home')  # Redirect to home page after successful login
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

# Logout view
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')  # Redirect to login page after logging out
