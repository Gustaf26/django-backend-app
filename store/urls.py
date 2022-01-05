from django.urls import path

# This is a relative import of views.py from the current package
# using dots
from . import views

#URLConf
urlpatterns = [
    path('products/', views.getProducts)]

