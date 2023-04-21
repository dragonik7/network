from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from post.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
