from django.urls import path
from . import views

urlpatterns = [
    path('replys/', views.CommentsList.as_view()),
]
