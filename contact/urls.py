from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^contact/', views.contact_form),
    url(r'^base/', views.base_page),
    url(r'^index/', views.index_page),    
]
