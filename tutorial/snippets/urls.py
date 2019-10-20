from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.api_root, name="root"),
    path('snippets/', views.snippet_list.as_view(), name="list-view"),
    path('snippets/<int:pk>/', views.snippet_detail.as_view(), name="detail-view"),
    path('snippets/<int:pk>/highlight', views.snippet_highlight.as_view(), name="snippet-highlight"),
    path('users/', views.user_list.as_view(), name="user-list-view"),
    path('users/<int:pk>/', views.user_detail.as_view(), name="user-detail-view"),
]

urlpatterns = format_suffix_patterns(urlpatterns)