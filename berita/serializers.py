from rest_framework import serializers
from berita.models import Kategori, Artikel
from pengguna.models import Biodata
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'firts_name', 'last_name', 'email']

class BiodataSerializer(serializers.ModelSerializer):
    class Meta :
        model = Biodata
        fields = ['user', 'alamat', 'telepon', 'foto']


class KategoriSerializer(serializers.ModelSerializer):
    user =UserSerializer(many=False)
    class Meta:
        model = Kategori
        fields = ['id', 'nama']
        
class ArtikelSerializers(serializers.ModelSerializer):
    author = UserSerializer()
    kategori = KategoriSerializer()
    class Meta:
        model = Artikel
        fields = ['id', 'judul', 'isi', 'kategori', 'author','thumbnail','created_at','slug']