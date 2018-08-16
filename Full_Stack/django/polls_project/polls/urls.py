from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    # # use these paths if not using Generic Views
    # # e.g. /polls/
    # path('', views.index, name='index'),
    # # e.g. /polls/34/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # e.g. /polls/34/results
    # path('<int:question_id>/results/', views.results, name='results'),
    # # e.g. /polls/34/vote
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    # same as above, but using generic views
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
