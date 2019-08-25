import os
from django.db import models
from django.conf import settings

class LostPost(models.Model):
    content = models.TextField(null=False)
    image = models.ImageField(null=True, upload_to="lostpost")
    found = models.BooleanField(default=False)      # 주웠어요=True, 잃어버렸어요=False
    comment_count = models.IntegerField(default=0)
    password = models.CharField(null=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("{}").format(self.content)

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(LostPost, self).delete(*args, **kargs)

class Comment(models.Model):
    lostpost = models.ForeignKey('LostPost', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
