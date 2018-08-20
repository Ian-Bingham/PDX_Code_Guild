from django.urls import path
from . import views

app_name = 'library_app'  # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:username>', views.profile, name='profile'),
    path('checkin/<int:book_id>/<str:username>', views.checkin, name='checkin'),
    path('checkout/<int:book_id>/<str:username>', views.checkout, name='checkout'),
]
