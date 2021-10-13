from django.shortcuts import render,redirect
from .models import blog
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .forms import postform
from django .urls import reverse_lazy
# Create your views here.

class home(ListView):
    model = blog
    template_name = 'index.html'
    context_object_name = 'obj1'
    ordering = ['-id']

class article_view(DetailView):
    model = blog
    template_name = 'single.html'
    context_object_name = 'i'


class addpost(CreateView):
    model = blog
    form_class = postform
    template_name = 'addpost.html'

    # field = '__all__'

class updatepost(UpdateView):
    model = blog
    template_name = 'updatepost.html'
    fields = ['title','title_tag','body','author','img']

class deletepost(DeleteView):
    model = blog
    template_name = 'deletepost.html'
    context_object_name = 'i'
    success_url = reverse_lazy('home')