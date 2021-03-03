from django.shortcuts import render

# Create your views here.
from home.models import Hakkimda, Projeler, KullandigimTeknolojiler, IlgiAlanlari, Egitim


def index(request):
    hakkimda = Hakkimda.objects.get(pk=1)
    projeler = Projeler.objects.all()
    kteknolojiler = KullandigimTeknolojiler.objects.all()
    ialanlari = IlgiAlanlari.objects.get(pk=1)
    egitimlerim = Egitim.objects.all()
    return render(request, "index.html", {
        'hakkimda': hakkimda,
        'projeler': projeler,
        'kteknolojiler': kteknolojiler,
        'ialanlari': ialanlari,
        'egitimlerim':egitimlerim
    })
