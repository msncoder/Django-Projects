"""miniblog2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home, name= 'home page'),
    path('about/', views.About, name= 'about page'),
    path('contact/', views.Contact, name= 'contact page'),
    path('dashboard/', views.Dashboard, name= 'dashboard page'),
    path('signup/', views.User_Signup, name= 'signup page'),
    path('login/', views.User_Login, name= 'login page'),
    path('logout/', views.User_Logout, name= 'logout page'),
    path('addpost/', views.AddPost, name='add post page'),
    path('updatepost/<int:id>/', views.UpdatePost, name='update post page'),
    path('deletepost/<int:id>/', views.DeletePost, name='delete post page'),
    

]
