from django.db import models
from datetime import datetime, timedelta


class ToDoItem(models.Model):
    title = models.CharField('Название задачи', max_length=200)
    text = models.TextField('Текст', max_length=800)
    is_complete = models.BooleanField('Завершено', default=False)
    deadline = models.DateTimeField(
        'Дедлайн',
        default=(datetime.now() + timedelta(days=1)).replace(hour=23, minute=59, second=59)
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title