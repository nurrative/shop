from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from drf_yasg.utils import swagger_auto_schema
from .models import Comment, Rating, Favorite
from .serializers import CommentSerializer, RatingSerializer, FavoriteSerializer


class CommentsViewSet(mixins.CreateModelMixin,mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]


class FavoriteViewSet(mixins.CreateModelMixin, mixins.ListModelMixin,
                      mixins.DestroyModelMixin, GenericViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class AddRatingAPIView(APIView):
    permission_classes = [IsAuthenticated,]
    @swagger_auto_schema(request_body=RatingSerializer())
    def post(self, request):
        ser = RatingSerializer(data=request.data, context={"request": request})
        ser.is_valid(raise_exception=True)
        ser.save()
        return Response(ser.data, status=201)












