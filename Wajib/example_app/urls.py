from django.urls import path
from example_app.views import index, indexWelcome, indexLogin


app_name = 'example_app'

urlpatterns = [
    path('', index, name='index'),
    path('welcome/', indexWelcome, name='index'),
    path('loginForm/', indexLogin, name='index'), 
]