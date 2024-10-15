from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from common.forms import ContactModelForm
from common.models import ContactModel


class ContactCreateView(CreateView):
    model = ContactModel
    form_class = ContactModelForm
    template_name = 'contact.html'
    success_url = reverse_lazy('common:contact')

    def form_valid(self, form):
        response = super().form_valid(form)

        # Add a success message
        messages.success(self.request, 'Contact created successfully!')

        return response
