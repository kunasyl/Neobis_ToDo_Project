from django.db import models

class ToDoItem(models.Model):
    title = models.CharField('Название задачи', max_length=200)
    text = models.TextField('Текст', max_length=800)
    is_complete = models.BooleanField('Завершено', default=False)

    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title