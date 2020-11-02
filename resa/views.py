from django.shortcuts import render
from .models import Dive, Diver, Site
from django.views.generic import ListView, TemplateView, DeleteView, CreateView, UpdateView, DetailView

from django.urls import reverse_lazy
from . import forms


# Create your views here.
# CRUD planning des plongée

class DiveList(ListView):
    queryset = Dive.objects.all()
    context_object_name = 'dives'
    template_name = 'resa/dive/list.html'


class DiveCreate(CreateView):
    pass


class DiveDetail(DetailView):
    pass


class DiveUpdate(UpdateView):
    pass


class DiveDelete(DeleteView):
    pass


# CRUD plongeurs
class DiverList(ListView):
    queryset = Diver.objects.all()
    context_object_name = 'divers'
    template_name = 'resa/diver/list.html'


class DiverCreate(CreateView):
    pass


class DiverDetail(DeleteView):
    pass


class DiverUpdate(UpdateView):
    pass


class DiverDelete(DeleteView):
    pass


## Site Views : CRUD
class SiteDetail(DetailView):
    context_object_name = "site"
    model = Site
    template_name = 'resa/site/site_detail.html'


class SiteCreate(CreateView):
    model = Site
    form_class = forms.SiteForm
    template_name = 'resa/site/site_form.html'


class SiteUpdate(UpdateView):
    model = Site
    form_class = forms.SiteForm


class SiteDelete(DeleteView):
    model = Site
    success_url = reverse_lazy("site_list")


class SiteList(ListView):
    model = Site
    queryset = Site.objects.all()
    context_object_name = 'sites'
    template_name = 'resa/site/site_list.html'
