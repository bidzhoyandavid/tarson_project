from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


# Create your models here.
class Vocabulary(models.Model):
    title = models.CharField(
        max_length=100, null=False, blank=False, verbose_name="title"
    )
    definition = RichTextUploadingField(
        verbose_name="definition", null=False, blank=False
    )
    date_upload = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Vocabulary"
        verbose_name_plural = "Vocabulary"
        ordering = (
            "id",
            "title",
        )


class EducationPost(models.Model):
    title = models.CharField(
        max_length=255, null=False, blank=False, verbose_name="title"
    )
    image = models.ImageField(null=True, blank=True)
    content = RichTextUploadingField(blank=False, null=False, verbose_name="content")
    date_upload = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Education Post"
        verbose_name_plural = "Education Posts"
        ordering = (
            "id",
            "title",
        )


# class EducationTags(models.Model):
#     tag = models.CharField(max_length=30, null=False, blank=False)

#     def __str__(self):
#         return self.tag

#     class Meta:
#         verbose_name = "Education Tag"
#         verbose_name_plural = "Education Tags"
#         ordering = (
#             "id",
#             "tag",
#         )


# class PostTagConnection(models.Model):
#     post = models.ForeignKey("EducationPost", on_delete=models.PROTECT, null=True)
#     tag = models.ForeignKey("EducationTags", on_delete=models.PROTECT, null=True)
