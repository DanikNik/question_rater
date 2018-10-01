from django.views.generic import TemplateView
# from authenticate import requirements

class DashboardView(TemplateView):
    template_name = "dashboard/dashboard.html"
