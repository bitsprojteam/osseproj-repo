"""project URL Configuration

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
from vetclinic import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),

    # #clinic urls
    # path('clinic/', views.ItemCollection.as_view()),
    # path('clinic/<int:pk>', views.ItemDetail.as_view()),

    # vet urls
    path('vet/', views.ItemCollection.as_view()),
    path('vet/<str:vetID>', views.ItemDetail.as_view()),
]