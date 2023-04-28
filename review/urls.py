from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentsViewSet, FavoriteViewSet, AddRatingAPIView

router = DefaultRouter()
router.register('comments', CommentsViewSet)
router.register('favorites', FavoriteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('rating/', AddRatingAPIView.as_view())
]