from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, null = False, blank = False, verbose_name='Title')
    text = models.TextField(null = False, blank = False, verbose_name='text')
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    is_published = models.BooleanField()
    image = models.ImageField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ['id']