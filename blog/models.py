from django.db import models

import os
class Post(models.Model):
    head_image = models.ImageField(upload_to='blog/images/%Y/%M/%d/', blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField()
    hook_text = models.CharField(max_length=100, blank= True)
    head_image = models.ImageField(upload_to='blog/images/%Y/%M/%d/', blank = True)
    file_upload = models.FileField(upload_to='blog/images/%Y/%M/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    hook_text = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.file_upload.name().split('.')[-1]

