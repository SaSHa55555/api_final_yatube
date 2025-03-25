from rest_framework import permissions


class AuthorOrReadOnlyPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        # Разрешаем доступ для безопасных методов
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        # Разрешаем доступ для безопасных методов
        # Для небезопасных методов проверяем, является ли пользователь автором
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )