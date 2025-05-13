from django.db import models
from django.urls import reverse, NoReverseMatch

class Menu(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, related_name='items', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    url = models.CharField(max_length=500, blank=True, help_text="Absolute URL")
    named_url = models.CharField(max_length=200, blank=True, help_text="Django named URL")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('menu', 'parent', 'order')
        ordering = ('parent__id', 'order')

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return self.url or '#'
        return self.url or '#'