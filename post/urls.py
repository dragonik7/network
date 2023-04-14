from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='post.index'),
	path('<uuid:post_id>/', views.detail, name='post.detail')
]
