from django.urls import path
from .views import friend_login, friend_page, unlock_text

urlpatterns = [
    path('<slug:slug>/', friend_login, name='friend_login'),
    path('<slug:slug>/page/', friend_page, name='friend_page'),
    path('unlock-text/<int:text_id>/', unlock_text, name='unlock_text'),
]
