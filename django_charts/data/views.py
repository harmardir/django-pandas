from django.views.generic import TemplateView
from .methods import csv_to_db

class Dashboard(TemplateView):
    template_name = 'dashboard.html'
    def get_context_data(self, **kwargs):
         # get the data from the default method       
        context = super().get_context_data(**kwargs)
        csv_to_db()
