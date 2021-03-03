from django.contrib import admin

from .models import  Hakkimda,IlgiAlanlari,KullandigimTeknolojiler,Projeler
# Register your models here.

@admin.register(Hakkimda)
class HakkimdaAdmin(admin.ModelAdmin):
    class Meta:
        model=Hakkimda


@admin.register(IlgiAlanlari)
class IlgiAlanlariAdmin(admin.ModelAdmin):
    class Meta:
        model = IlgiAlanlari


@admin.register(KullandigimTeknolojiler)
class KullandigimTeknolojilerAdmin(admin.ModelAdmin):
    class Meta:
        model = KullandigimTeknolojiler

@admin.register(Projeler)
class KullandigimTeknolojilerAdmin(admin.ModelAdmin):
    class Meta:
        model = Projeler