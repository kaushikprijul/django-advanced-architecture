from django.urls import path

from .views import (
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
    set_theme,
    custom_logout
)

urlpatterns = [

    path('', CourseListView.as_view(), name='course_list'),

    path('course/<int:pk>/', CourseDetailView.as_view(),
         name='course_detail'),

    path('course/create/', CourseCreateView.as_view(),
         name='course_create'),

    path('course/<int:pk>/update/', CourseUpdateView.as_view(),
         name='course_update'),

    path('course/<int:pk>/delete/', CourseDeleteView.as_view(),
         name='course_delete'),

    path('theme/<str:theme>/', set_theme, name='set_theme'),

    path('logout/', custom_logout, name='logout'),

]