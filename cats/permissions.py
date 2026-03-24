from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешает редактирование только владельцу объекта.
    Для всех остальных (включая анонимов) — только безопасные методы (GET).
    """
    def has_permission(self, request, view):
        # Разрешаем запрос, если метод безопасный или пользователь авторизован
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        # Проверяем, совпадает ли автор объекта с пользователем из запроса
        return obj.owner == request.user


class ReadOnly(permissions.BasePermission):
    """
    Разрешает только чтение (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS