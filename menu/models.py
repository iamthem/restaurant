from django.db import models

class MenuSections(models.Model):

    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class Success (object):

    def __init__(self, success):
        self.success = success

    def __str__(self):
        return self.success

