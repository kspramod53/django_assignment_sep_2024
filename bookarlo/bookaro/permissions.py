# bookaro/permissions.py

from rest_framework.permissions import BasePermission

class IsEventManager(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.role == 'Event Manager'
