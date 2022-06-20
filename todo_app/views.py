from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from .form import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy


# Create your views here.
# class TaskListView(ListView):
#     model = Task
#     template_name = 'home.html'
#     context_object_name = 'obj1'


# class TaskCreateView(CreateView):
#     model = Task
#     form_class = Todoforms
#     template_name = 'add.html'
#     success_url = reverse_lazy('home')


class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'i'


class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'pk': self.object.id})


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('home')


def home(request):
    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
    return render(request, 'home.html', {'obj1': obj1})
