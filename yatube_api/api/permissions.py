from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return any([
            request.method in permissions.SAFE_METHODS,
            request.user.is_authenticated
        ])

    def has_object_permission(self, request, view, obj):
        return any([
            request.method in permissions.SAFE_METHODS,
            obj.author == request.user
        ])
