"""backend_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#import debug_toolbar
from django.urls import path, include

urlpatterns = [
    # The path() function receives four arguments, two required and two optional. The arguments below are routes. Route is a string that contains a URL pattern.
    path('admin/', admin.site.urls),

    # The include() function allows you to reference other URLconfs. Each time Django finds include() it cuts off any part of the URL that matches up to that point and sends the remaining string to the included URLconf to follow the process.
    path('playground/', include('playground.urls')),
    path('store/', include('store.urls'))
]
