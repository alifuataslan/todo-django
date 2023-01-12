from asyncio.windows_events import NULL
from email.policy import default
from pydoc import visiblename
from turtle import title
from django.db import models

class Notes(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=200,verbose_name="İçerik")
    content=models.TextField(verbose_name="içerik")
    created_date=models.DateTimeField(auto_now=True,verbose_name="oluşturma tarihi")
    notes_show=models.BooleanField(default=True)
    deleted_date=models.DateTimeField(blank=True,null=True)
    
    class Meta:
        ordering = ["-created_date"]
