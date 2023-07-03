from django.urls import path
from followers.views import FollowList, FollowDetail

urlpatterns = [
    path('follows/', FollowList.as_view(), name='follow-list'),
    path('follows/<int:pk>/', FollowDetail.as_view()),
]
