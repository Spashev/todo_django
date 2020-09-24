from django.db import models

class Todo(models.Model):
    TODO = 'todo'
    DONE = 'done'
    STATUS = (
        (TODO, 'Todo'),
        (DONE, 'Done')
    )
    description = models.CharField(max_length=255, verbose_name="Description")
    status = models.CharField(max_length=10, verbose_name="Status", choices=STATUS)
