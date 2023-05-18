from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


# Create your models here.


class Blog(models.Model):
    title = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="Title"
    )
    text = RichTextUploadingField(null=False, blank=False, verbose_name="text")
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    is_published = models.BooleanField()
    image = models.ImageField(null=True, blank=True, upload_to="media")
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/post/{self.id}"

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"
        ordering = ["id"]
