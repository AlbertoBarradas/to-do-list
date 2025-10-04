from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Task
from .utils import send_realtime_notifications
from django.urls import reverse_lazy
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = "__all__"
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

    
def logout_user(request):
    logout(request)
    return redirect('login')

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete'] 
    template_name = "base/task_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        task = form.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{self.request.user.id}",
            {
                "type": "send_notification",
                "message": f"Task '{task.title}' created"
            }
        )

        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'title': task.title})

        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors})
        return super().form_invalid(form)
    
class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete'] 
    template_name = "base/task_update.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        task = form.save()

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"user_{self.request.user.id}",
            {
                "type": "send_notification",
                "message": f"Task '{task.title}' updated"
            }
        )

        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'title': task.title})

        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors': form.errors})
        return super().form_invalid(form)
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = "task"
    success_url = reverse_lazy('tasks')

def complete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.complete = True
    task.save()
    send_realtime_notifications(request.user, f"Task '{task.title}' completed!")
    return redirect('tasks')