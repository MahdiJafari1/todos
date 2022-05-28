from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class List(models.Model):
    """Model difinition for Todo list"""
    class Meta:
        verbose_name = _("List")
        verbose_name_plural = _("Lists")

    def __str__(self):
        return self.text[:20]

    def get_absolute_url(self):
        return reverse("list_detail", kwargs={"pk": self.pk})
    
    
class Todo(models.Model):

    text = models.TextField(max_length=250)
    list = models.ForeignKey("List", default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Todo")
        verbose_name_plural = _("Todos")
        ordering = ("id",)
        unique_together = ("list", "text",)

    def __str__(self):
        return self.text[:20]

    def get_absolute_url(self):
        return reverse("todo_detail", kwargs={"pk": self.pk})

