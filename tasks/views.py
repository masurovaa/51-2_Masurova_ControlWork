from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Task, Category
from .forms import TaskForm
from django.db.models import Q

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        if category:
            queryset = queryset.filter(category__id=category)
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = reverse_lazy('task-list')