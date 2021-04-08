from django.db import models
from django.urls import reverse
from django.utils.timezone import now
from django.utils.text import slugify
# Create your models here.


class Blog(models.Model):
    blog_title = models.CharField(max_length=250)
    slug = models.SlugField(null=False, unique=True)
    sub_title = models.CharField(max_length=500)
    body = models.CharField(max_length=3000)
    blog_image = models.FileField(upload_to='blog_image', blank=True)
    created_date_time = models.DateTimeField(default=now)

    def __str__(self):
        return self.blog_title

    def get_absolute_url(self):
        return reverse('blog_app:blog_post', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        slug = slugify(self.blog_title)
        unique_slug = slug
        num = 1
        while Blog.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)
