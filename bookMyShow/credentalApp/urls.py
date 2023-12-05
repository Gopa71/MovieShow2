from django.urls import path
from .import views
urlpatterns = [
    path('Register/',views.Register,name='Register'),
     path('Login/',views.login,name='Login'),
     path('logout/',views.logout,name='logout')
   
   

]