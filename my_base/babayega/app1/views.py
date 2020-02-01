from app1.models import PhoneContacts
from django.views.generic import (TemplateView, UpdateView, DeleteView, CreateView, ListView,
                                  DetailView)
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import PhoneForm, ContactForm
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse


class ProfileView(TemplateView):
    template_name = 'app1/index.html'


class DashboardView(TemplateView):
    template_name = 'app1/dashboard.html'


class ContactListView(ListView):
    model = PhoneContacts
    context_object_name = 'contact_list'

    def get_queryset(self):
        return PhoneContacts.objects.all().order_by('name')


class ContactDetailView(DetailView):
    model = PhoneContacts


class ContactCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login'
    redirect_field_name = 'app1/phone_list.html'
    form_class = PhoneForm
    model = PhoneContacts


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login'
    redirect_field_name = 'app1/phone_list.html'
    form_class = PhoneForm
    model = PhoneContacts
    context_object_name = 'Phones'


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    model = PhoneContacts
    success_url = reverse_lazy('phone_list')


def contact_me(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse('Hey!, thank you for reaching out, we are so happy to hear from you')
        else:
            return form.errors('Please ensure you filled the form very well')

    else:
        form = ContactForm()
        return render(request, 'app1/contact_form.html', {'form': form})


