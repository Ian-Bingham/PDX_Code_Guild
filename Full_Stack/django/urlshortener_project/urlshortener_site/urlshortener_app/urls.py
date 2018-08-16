from django.urls import path
from . import views

app_name = 'urlshortener_app' # for namespacing
urlpatterns = [
    path('index/', views.index, name='index'),
    path('saveurl/', views.saveurl, name='saveurl'),
    path('redirect/<str:url_tag>', views.redirect_site, name='redirect_site'),
]
