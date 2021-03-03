import datetime
import os

from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.

def default_value_current_today():
    return datetime.date.today()


def content_file_name_dosyalar(instance, filename):
    filename = "dosyalar/{}".format(filename)
    return os.path.join('hakkimda-dosyalari', filename)


class Hakkimda(models.Model):
    facebook = models.CharField(verbose_name="Facebook ", max_length=255)
    twitter = models.CharField(verbose_name="Twitter ", max_length=255)
    github = models.CharField(verbose_name="GitHub ", max_length=255)
    linked = models.CharField(verbose_name="Linkedin ", max_length=255)
    telefon = models.CharField(verbose_name="Telefon ", max_length=255)
    email = models.CharField(verbose_name="E-Mail ", max_length=255)
    hakkimda = RichTextField(verbose_name="Hakkımda ")
    profil = models.ImageField(verbose_name="Profil ", upload_to=content_file_name_dosyalar)

    class Meta:
        db_table = "hakkimdatb"
        verbose_name = "Hakkımda"
        verbose_name_plural = "Hakkımda Yönet"


class Projeler(models.Model):
    adi = models.CharField(verbose_name="Adi ", max_length=255)
    sirket = models.CharField(verbose_name="Şirket ", max_length=255)
    icerik = RichTextField(verbose_name="İçerik ")
    baslangicTarihi = models.DateField(verbose_name="Başlangıç Tarihi ", default=default_value_current_today)
    bitisTarihi = models.DateField(verbose_name="Bitiş Tarihi ", default=None)

    class Meta:
        db_table = "projetb"
        verbose_name = "Projeler"
        verbose_name_plural = "Projeleri Yönet"


class KullandigimTeknolojiler(models.Model):
    adi = models.CharField(verbose_name="Adi ", max_length=255)
    icon = models.CharField(verbose_name="İcon ", max_length=255)

    class Meta:
        db_table = "kteknolojileritb"
        verbose_name = "Kullanıcı Teknolojileri"
        verbose_name_plural = "Kullanıcı Teknolojileri Yönet"


class IlgiAlanlari(models.Model):
    aciklama = RichTextField(verbose_name="İlgi Alanları ")

    class Meta:
        db_table = "ilgialanitb"
        verbose_name = "İlgi Alanları"
        verbose_name_plural = "İlgi Alanlarını Yönet"


class Egitim(models.Model):
    okulismi = models.CharField(verbose_name="Okul İsmi " , max_length=255)
    alan = models.CharField(verbose_name="Alan" , max_length=255)
    baslangictarihi = models.DateField(verbose_name="Başlangıç Tarihi ")
    bitistarihi = models.DateField(verbose_name="Bitiş Tarihi")
    class Meta:
        db_table = "egitimtb"
        verbose_name = "Eğitim"
        verbose_name_plural = "Eğitim"
