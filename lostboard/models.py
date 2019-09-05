import os
from django.db import models
from django.conf import settings

class Post(models.Model):
    content = models.TextField(null=False)
    image = models.ImageField(null=True, upload_to="lostpost")
    found = models.BooleanField(default=False)      # 주웠어요=True, 잃어버렸어요=False
    password = models.CharField(null=False, max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created_at']

    def __str__(self):
        return ("{}").format(self.content)

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.image.path))
        super(Post, self).delete(*args, **kargs)

class Comment(models.Model):
    lostpost = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
