from django.urls import path
from .views import *

urlpatterns = [
    path('', Menu.as_view()),
    path('<slug:content_slug>', ShowItem.as_view(), name='content')

]
