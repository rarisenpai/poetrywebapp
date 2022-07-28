from typing import List
from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.views.generic import ListView,DetailView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import DeleteView

from .forms import PoemsForm
from .models import Poems

class PoemsDeleteView(LoginRequiredMixin,DeleteView):
  model = Poems
  success_url = '/smart/poems'
  login_url = '/login'
  

class PoemsUpdateView(LoginRequiredMixin,UpdateView):
  model = Poems
  success_url = '/smart/poems'
  form_class = PoemsForm
  login_url = '/login'
  
class PoemsCreateView(LoginRequiredMixin,CreateView):
  model = Poems
  success_url = '/smart/poems'
  form_class = PoemsForm
  login_url = '/login'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user= self.request.user
    self.object.save()
    return HttpResponseRedirect(self.get_success_url())
  

class PoemsListView(LoginRequiredMixin,ListView):
  model = Poems
  context_object_name = "poems"
  login_url = '/login'

  def get_queryset(self):
    return self.request.user.poems.all()

class PoemsDetailView(DetailView):
  model = Poems
  context_object_name = 'poem'



