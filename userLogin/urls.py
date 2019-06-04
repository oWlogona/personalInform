from django.urls import path
from userLogin import views

urlpatterns = [
    path('login/', views.UserLoginView.as_view()),
    path('homePage/', views.UserHomePageView.as_view()),
    path('logout/', views.UserLogOutView.as_view())
]
