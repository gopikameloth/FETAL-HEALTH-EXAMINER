from django.shortcuts import render, redirect
from .forms import UserRegistrationForm


def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup_success')  # Redirect to a success page
    else:
        form = UserRegistrationForm()
    return render(request, 'signup.html', {'form': form})

