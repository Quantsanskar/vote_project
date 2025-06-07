from django.urls import path
from . import views

urlpatterns = [
    path('', views.VoteView.as_view(), name='vote'),
    path('baby/mhbdhmb/gvnhde/gv/', views.GirlfriendView.as_view(), name='girlfriend'),
    path('api/votes/', views.get_vote_count, name='vote_count_api'),
]
