from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.throttling import AnonRateThrottle, ScopedRateThrottle
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from .models import Achievement, Cat, User
from .pagination import CustomPagination
from .permissions import OwnerOrReadOnly, ReadOnly
from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from .throttling import WorkingHoursThrottling


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    filter_backends = (
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    )
#    pagination_class = CatsPagination
    filterset_fields = ('color', 'birth_year',)
    search_fields = ('name', 'owner__username')
    ordering = ('color',)
    ordering_fields = ('owner',)
    throttle_classes = (
        WorkingHoursThrottling,
        AnonRateThrottle,
        ScopedRateThrottle,
    )
#    throttle_scope = 'low_request'

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (OwnerOrReadOnly(),)
        return super().get_permissions()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer