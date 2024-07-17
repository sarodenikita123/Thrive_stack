from django.db import models


class Manangesystem(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    context = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
