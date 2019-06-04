from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate, logout, login
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class UserLoginView(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'userLogin.html', locals())

    def post(self, request, *args, **kwargs):
        data = request.POST
        user = authenticate(username=data.get('useremail'), password=data.get('password'))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/homePage/')
        return render(request, 'userLogin.html', locals())


class UserHomePageView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        print(request.user)
        return render(request, 'userHome.html', locals())


class UserLogOutView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        url = '/login/'
        return HttpResponseRedirect(url)
