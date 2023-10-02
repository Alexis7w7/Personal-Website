from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="title")
    description = models.TextField(verbose_name="description")
    image = models.ImageField(verbose_name="imagen", upload_to="Projects")
    link = models.URLField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ["-created"]

    def __str__(self):
        return self.title
