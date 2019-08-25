import os
from django.db import models
from django.conf import settings

class LostPost(models.Model):
    content = models.TextField(null=False)
    image = models.ImageField(null=True, upload_to="lostpost")
    finding = models.BooleanField(default=False)
    comment_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("{}").format(self.content)

    def delete(self, *args, **kargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(LostPost, self).delete(*args, **kargs)

class Comment(models.Model):
    lostpost = models.ForeignKey('LostPost', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
