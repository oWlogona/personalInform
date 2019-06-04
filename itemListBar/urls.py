from django.urls import path
from itemListBar import views

urlpatterns = [
    path('create_card/', views.UserCreateCardView.as_view()),
]
