from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Course
from django.contrib.auth import logout
from django.shortcuts import redirect


class CourseListView(LoginRequiredMixin, ListView):

    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Course.objects.filter(
            creator=self.request.user
        )


class CourseDetailView(LoginRequiredMixin, DetailView):

    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_queryset(self):
        return Course.objects.filter(
            creator=self.request.user
        )


class CourseCreateView(LoginRequiredMixin, CreateView):

    model = Course
    fields = ['title', 'description', 'duration']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class CourseUpdateView(LoginRequiredMixin, UpdateView):

    model = Course
    fields = ['title', 'description', 'duration']
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('course_list')

    def get_queryset(self):
        return Course.objects.filter(
            creator=self.request.user
        )


class CourseDeleteView(LoginRequiredMixin, DeleteView):

    model = Course
    template_name = 'courses/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')

    def get_queryset(self):
        return Course.objects.filter(
            creator=self.request.user
        )


def set_theme(request, theme):

    if theme not in ['dark', 'light']:
        return redirect('course_list')

    response = redirect('course_list')

    response.set_cookie(
        'preferred_theme',
        theme,
        max_age=60 * 60 * 24 * 30
    )

    return response


def custom_logout(request):

    logout(request)

    request.session.flush()

    return redirect('login')