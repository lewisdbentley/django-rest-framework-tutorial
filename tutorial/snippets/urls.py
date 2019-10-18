from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('', views.snippet_list, name='list-view'),
    # path('<int:pk>/', views.snippet_detail, name='detail-view')
    path('', views.snippet_list.as_view(), name="list-view"),
    path('<int:pk>/', views.snippet_detail.as_view(), name="detail-view"),
]

urlpatterns = format_suffix_patterns(urlpatterns)