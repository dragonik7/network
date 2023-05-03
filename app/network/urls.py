from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from post.views import PostViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

token = [
    path('', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]
# posts = [
#     path('', PostListViewSet.as_view()),
#     path('<uuid:pk>/', PostDetailView.as_view())
# ]
api = [
    path('token/', include(token)),
    path('', include(router.urls))
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api)),

]
