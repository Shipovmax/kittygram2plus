from rest_framework import viewsets
from .permissions import OwnerOrReadOnly, ReadOnly
from .models import Achievement, Cat, User
from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from rest_framework.throttling import ScopedRateThrottle
from .pagination import CatsPagination
from django_filters.rest_framework import DjangoFilterBackend
from .throttling import WorkingHoursRateThrottle
from rest_framework import filters

class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('achievements__name', 'owner__username')
    pagination_class = None

    def perform_create(self, serializer):
        # Автоматически сохраняем текущего пользователя как владельца
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        # Если нужно посмотреть детали конкретного котика (action 'retrieve')
        if self.action == 'retrieve':
            # Разрешаем доступ всем (ReadOnly)
            return (ReadOnly(),)
        # В остальных случаях используем настройки из permission_classes
        return super().get_permissions()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Здесь права не меняем — действует глобальное IsAuthenticated из settings.py


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    # Можно добавить OwnerOrReadOnly, если у достижений появится владелец