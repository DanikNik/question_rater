from django.contrib.auth.mixins import UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCheckMixin(UserPassesTestMixin):
    def handle_no_permission(self):
        if self.raise_exception:
            raise PermissionDenied(self.get_permission_denied_message())
        return redirect(reverse('person_create'))

    def test_func(self):
        return hasattr(self.request.user, 'person')

    raise_exception = False

class StaffCheckMixin(UserPassesTestMixin):
    # def handle_no_permission(self):
    #     if self.raise_exception:
    #         raise PermissionDenied(self.get_permission_denied_message())

    def test_func(self):
        return self.request.user.is_staff

    raise_exception = False
