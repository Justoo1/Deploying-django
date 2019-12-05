from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('index',views.index, name='index'),
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
