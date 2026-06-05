from django.db import models

# Create your models here.

class TaskboardDetails(models.Model):
    task_title = models.CharField(max_length=225)
    task_description = models.TextField()
    task_created_date = models.DateTimeField(auto_now_add=True)
    task_updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'taskboard_details'