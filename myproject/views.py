from django.shortcuts import render
from berita.models import Artikel, Kategori
def home(request):
    template_name = "halaman/index.html"
    kategori = request.GET.get('kategori')
    if kategori == None:
        data_artikel = Artikel.objects.all()
        menu_aktif = "ALL"
    else:
        try :
            get_kategori = Kategori.objects.get(nama=kategori)
            data_artikel = Artikel.objects.filter(kategori=get_kategori)
            menu_aktif = kategori
        except:
            menu_aktif = "ALL"
            data_artikel = []
        
        
    data_kategori = Kategori.objects.all()
    context ={
        'title' : 'HoleOfDamascus',
        'data_artikel' : data_artikel,
        'data_kategori' : data_kategori,
        'menu_aktif' : menu_aktif
    }
    return render(request, template_name, context)

def about(request):
    template_name = "halaman/about.html"
    context ={
        'title' : 'Tentang Kami'
    }
    return render(request, template_name, context)

def contact(request):
    template_name = "halaman/contact.html"
    context ={
        'title' : 'Tentang Kami'
    }
    return render(request, template_name, context)

def detail_artikel(request, slug):
    template_name = 'halaman/detail_artikel.html'
    artikel = Artikel.objects.get(slug=slug)
    context = {
        'title' : artikel.judul,
        'artikel' : artikel
    }
    return render (request, template_name, context)