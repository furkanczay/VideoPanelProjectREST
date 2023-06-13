from django.urls import path
from .views import ListVideosAPI, UserVideosAPIView, VideoDetailAPI, VideoCommentCreateAPI, VideoCommentsListAPI, VideoAddAPI

urlpatterns = [
    path('', ListVideosAPI.as_view(), name='list_videos'),
    path('create/', VideoAddAPI.as_view(), name='create_video'),
    path('instructor/<slug>/', UserVideosAPIView.as_view(), name='list_user_videos'),
    path('video/<slug>/', VideoDetailAPI.as_view(), name='video_detail'),
    path('comments/create/', VideoCommentCreateAPI.as_view(), name='video_comment_create'),
    path('comments/', VideoCommentsListAPI.as_view(), name='video_comment_list'),
]