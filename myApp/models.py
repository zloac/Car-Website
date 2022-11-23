
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Post(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    image = models.FileField(("Post Fotoğrafı"), upload_to='post')
    fiyat = models.IntegerField(("fiyat"))

class UserSave(models.Model):
    user = models.CharField(("Kullanıcı adı "), max_length=200)
    password = models.CharField(("Kullanıcı Şifre"), max_length=200)
    
    def __str__(self) -> str:
        return self.user
    
class Sepet(models.Model):
    car = models.ForeignKey(Post, verbose_name=("Araba"), on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    adet = models.IntegerField(("Adet"))
    fiyat = models.FloatField(("Toplam fiyat"))
    
    def __str__(self) -> str:
        return self.car.title