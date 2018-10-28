from django.views.generic import TemplateView
from catalog.assets.user_check_mixins import ProfileCheckMixin

class DashboardView(ProfileCheckMixin, TemplateView):
    template_name = "dashboard/dashboard.html"
