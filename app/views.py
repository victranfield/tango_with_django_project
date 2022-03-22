from django.views.generic import ListView
from .models import Course


class CourseListView(ListView):
    template_name = "course_list.html"
    queryset = Course.objects.all()
