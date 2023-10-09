from django.urls import path, include
from .views import *

# app_name = 'user'
urlpatterns = [
    path('users/', UserIndexView.as_view(), name='user.index'),
    path('login/', LoginPage, name='login'),
    path('users/update/<str:pk>', Update.as_view(), name='user.update'),
    path('logout/', logoutView, name='logout'),

    path('face-login/', FaceLoginPage, name='face.login'),

    path('reset_password/<str:pk>', reset_password, name='user.reset_password'),
    path('reset_pin/<str:pk>', reset_pin, name='user.reset_pin'),

    path('user/deletions/', DeletedUserIndexView.as_view(), name='user.deleted.index'),

]
