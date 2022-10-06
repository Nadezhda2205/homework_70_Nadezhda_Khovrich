from django.db import models


class Status(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, null=False)

    def __str__(self) -> str:
        return self.name


class Type(models.Model):
    name = models.CharField(verbose_name='Название', max_length=50, null=False)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    summary = models.CharField(verbose_name='Заголовок', max_length=200, null=False)
    description = models.TextField(verbose_name='Описание', null=True)
    status = models.ForeignKey(to='issue.Status', verbose_name='Статус', related_name='status', on_delete=models.RESTRICT)
    type = models.ForeignKey(to='issue.Type', verbose_name='Тип', related_name='type', on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self) -> str:
        return self.summary

