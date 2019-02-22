from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegistrationForm, UserProfileForm

HTTP_METHOD_POST = 'POST'
HTTP_METHOD_GET = 'GET'


# Create your views here.
def user_login(request):
    if request.method == HTTP_METHOD_POST:
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user:
                login(request, user)
                return redirect(reverse('blog:blog_title'))
            else:
                return HttpResponse('抱歉，你的用户名或者密码错误！')
        else:
            return HttpResponse('登录成功！')

    if request.method == HTTP_METHOD_GET:
        login_form = LoginForm()
        return render(request, 'account/login.html', {'form': login_form})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def register(request):
    if request.method == HTTP_METHOD_POST:
        user_form = RegistrationForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            new_profile = user_profile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('注册成功！')
        else:
            return HttpResponse('注册失败！')
    else:
        user_form = RegistrationForm()
        user_profile_form = UserProfileForm()
        return render(request, 'account/register.html', {'form': user_form, 'profile': user_profile_form})
