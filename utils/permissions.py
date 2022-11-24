from rest_framework import permissions
import ipdb

class isAdminOrOwnerShop(permissions.BasePermission):
    def has_object_permission(self, req, view, obj) -> bool:
        return (
            req.user.is_authenticated
            and req.user.is_superuser
            or req.user.is_authenticated
            and obj.owner.id == req.user.id
        )
class isAdminOrOwnerUser(permissions.BasePermission):
    def has_object_permission(self, req, view, obj) -> bool:
        return (
            req.user.is_authenticated
            and req.user.is_superuser
            or req.user.is_authenticated
            and obj.id == req.user.id
        )



class isAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_authenticated and request.user.is_superuser