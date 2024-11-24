from django.urls import path
from .views import *

app_name = 'home'
urlpatterns = [
    path('home/', HomeView.as_view(), name='index'),

    path('home/extract/data', ExtractData, name='extract.data'),

    path('link/', LinkIndex.as_view(), name='link.index'),
    path('link/create/', LinkCreate.as_view(), name='link.create'),
    path('link/update/<str:pk>', LinkUpdate.as_view(), name='link.update'),
    path('link/delete/<str:pk>', LinkDelete.as_view(), name='link.delete'),
]
