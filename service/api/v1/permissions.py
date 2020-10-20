"""
Custom Permission classes
"""
from django.db.models import Q
from rest_framework import permissions
import logging

logger = logging.getLogger(__name__)


class IsValidAdmin(permissions.IsAdminUser):
    """
    Allow an action to be taken by an Admin
    """

    def has_permission(self, request, view):

        if request.user and request.user.is_authenticated:
            admin = (request.user.groups
                        .filter(Q(name='admin'))
                        .exists())

            if admin:
                return True

        return False

    def has_object_permission(self, request, view, obj):

        if request.user and request.user.is_authenticated:
            admin = (request.user.groups
                        .filter(Q(name='admin'))
                        .exists())

            if admin:
                return True

        return False
