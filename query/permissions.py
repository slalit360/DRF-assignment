from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_user():
            return True
        return False


class IsMentor(BasePermission):
    def has_permission(self, request, view):
        print(request.user)
        if request.user.is_mentor():
            print("yes mentor")
            return True
        print("no mentor : user")
        return False
