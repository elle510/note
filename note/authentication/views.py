from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
# from django.template import RequestContext

from .forms import UserForm, LoginForm

# Create your views here.

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('memo_list')
    else:
        form = UserForm()
        return render(request, 'authentication/join.html', {'form': form})

def signin(request):
    if request.method == "POST":
        # form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('memo_list')
            else:
                return HttpResponse('유효한 계정이 아닙니다. 다시 시도 해보세요.')
        else:
            return HttpResponse('로그인 실패. 다시 시도 해보세요.')
    else:
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})
