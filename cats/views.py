from rest_framework import viewsets
from .permissions import OwnerOrReadOnly, ReadOnly
from .models import Achievement, Cat, User
from .serializers import AchievementSerializer, CatSerializer, UserSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class CatViewSet(viewsets.ModelViewSet):
    # select_related for the FK owner and prefetch_related for the
    # achievements M2M avoid an N+1 query per row when the serializer
    # touches `owner` and `achievements` for every Cat in the list.
    queryset = Cat.objects.select_related('owner').prefetch_related(
        'achievements')
    serializer_class = CatSerializer
    permission_classes = (OwnerOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter)
    filterset_fields = ('color', 'birth_year')
    search_fields = ('name',)
    ordering_fields = ('name', 'birth_year')
    ordering = ('birth_year',)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action == 'retrieve':
            return (ReadOnly(),)
        return super().get_permissions()


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # prefetch_related('cats') avoids an N+1 query when the serializer
    # renders the reverse `cats` relation for every user in the list.
    queryset = User.objects.prefetch_related('cats')
    serializer_class = UserSerializer
    # Permissions are left as-is here — the global IsAuthenticated from
    # settings.py already applies.


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    # OwnerOrReadOnly could be added here if achievements gain an owner.