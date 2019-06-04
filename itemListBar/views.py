from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class UserCreateCardView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        return render(request, 'createUserCard.html', locals())

    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        return render(request, 'createUserCard.html', locals())
