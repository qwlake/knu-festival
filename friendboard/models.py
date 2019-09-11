from django.db import models

# Create your models here.
class Post(models.Model):
    
    content = models.TextField(default='')             # 길이 제한이 없는 문자열
    created_at = models.DateTimeField(auto_now_add=True) # 해당 레코드 생성시 현재 시간 자동저장
    password = models.CharField(max_length=50)

    class Meta:
        ordering=['-created_at']
        
    def __str__ (self):
        return self.content


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)