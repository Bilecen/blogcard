from django.db import models


# Create your models here.

class BaseModel(models.Model):
    create_at = models.DateTimeField(auto_created=True, auto_now=False)
    update_at = models.DateTimeField(auto_now=True, auto_created=False)

    class Meta:
        abstract = True


class Kategori(BaseModel):
    adi = models.CharField(verbose_name="Adi" , max_length=255)
    slug = models.SlugField(verbose_name="slug" , editable=False)

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategori Yönetimi"
        ordering = ["-create_at"]


