from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, UpdateView
from django.urls import reverse_lazy, reverse


# Create your views here.

class UserIndexView(ListView):
    model = User
    paginate_by = 50
    template_name = "backend/user/index.html"


class Update(SuccessMessageMixin, UpdateView):
    model = User
    template_name = "backend/user/form.html"
    form_class = UserForm
    success_message = "User Updated Successfully."
    success_url = reverse_lazy('user.index')


def LoginPage(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)

        if not user:
            try:
                user = User.objects.get(email=username, pin=password)
            except User.DoesNotExist:
                user = None

        if user:
            login(request, user)
            messages.success(request, 'User Successfully Logging')
            return redirect(reverse('home:index'))
        else:
            messages.error(request, 'User Not found')

    context = {
        'form': form
    }
    return render(request, 'backend/auth/login.html', context)


def logoutView(request):
    logout(request)
    messages.success(request, 'Logout Successfully')
    return redirect('login')


def FaceLoginPage(request):
    return render(request, 'backend/auth/face-login.html')


def reset_password(request, pk):
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        user = User.objects.filter(pk=pk).first()

        if user:
            user.set_password(new_password)
            user.save()
            return redirect('user.index')

    return render(request, 'backend/user/reset-password.html', {'user_id': pk})


def reset_pin(request, pk):
    if request.method == 'POST':
        new_pin = request.POST.get('new_pin')
        user = User.objects.filter(pk=pk).first()

        if user:
            user.pin = new_pin
            user.save()
            return redirect('user.index')

    return render(request, 'backend/user/reset-pin.html', {'user_id': pk})


class DeletedUserIndexView(ListView):
    model = User
    paginate_by = 50
    template_name = "backend/user/deleted/index.html"

    def get_queryset(self):
        return User.objects.filter(is_deleted=True)
