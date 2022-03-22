from urllib.parse import urlparse
from django.urls import path
from .views import CourseListView

urlpatterns = [
    path('', CourseListView.as_view(), name="course_list")
]
