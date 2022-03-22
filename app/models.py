from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    starting_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
