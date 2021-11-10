from django.urls import path
from . import views

urlpatterns = [
    path('replys/', views.ReplysList.as_view()),
]
