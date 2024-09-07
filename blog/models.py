from django.db import models
from django.utils.text import slugify
from django.utils import timezone


# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


class RepublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.DRAFT)


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=50, verbose_name="Заголовок")
    slug = models.SlugField(max_length=250, verbose_name="slug", unique_for_date="created_at")
    content = models.TextField(verbose_name="содержимое")
    image = models.ImageField(upload_to="posts/")
    created_at = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    views = models.PositiveIntegerField(default=0, verbose_name="просмотры")
    objects = models.Manager()
    published = PublishedManager()
    not_published = RepublishManager()

    class Meta:
        ordering = ["-created_at"]
        indexes = [models.Index(fields=["-created_at"]), ]
        verbose_name = "публикация"
        verbose_name_plural = "публикации"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
