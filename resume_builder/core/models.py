from django.db import models
from django.utils.text import slugify

#--------------RESUME MODEL-----------------

class Resume(models.Model):
    name  = models.CharField(max_length=100)
    slug  = models.SlugField(unique=True, blank=True)
    theme = models.CharField(max_length=50, default="default")
    views = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1

            while Resume.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

#-----------------SKILL MODEL-----------------

class Skill(models.Model):
    resume = models.ForeignKey(
        Resume,
        on_delete=models.CASCADE,
    )
    name         = models.CharField(max_length=50)
    endorsements = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.resume.name})"

