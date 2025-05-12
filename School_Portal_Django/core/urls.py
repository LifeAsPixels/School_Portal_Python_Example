from django.urls import path
from .views import StudentListCreateView, CourseListCreateView, GradeListCreateView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='students'),
    path('courses/', CourseListCreateView.as_view(), name='courses'),
    path('grades/', GradeListCreateView.as_view(), name='grades'),
]
