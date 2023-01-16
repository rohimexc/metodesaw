from tokenize import Name
from turtle import update
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Room(models.Model):
    host =models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic =models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    updated =models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering =['-updated','-created']


    def __str__(self):
        return self.name

class Message(models.Model):
    user =models.ForeignKey(User, on_delete=models.CASCADE)
    room=models.ForeignKey(Room, on_delete=models.CASCADE)
    body=models.TextField()
    updated =models.DateTimeField(auto_now=True)
    created =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]
   
class JumlahPenghasilanOrtu(models.Model):
    Name=models.CharField(max_length=100)
    bobot=models.DecimalField(max_digits=3,decimal_places=2)
    def __str__(self):
        return self.Name

class NilaiRatarataRaport(models.Model):
    Name=models.CharField(max_length=100)
    bobot=models.DecimalField(max_digits=3,decimal_places=2)
    def __str__(self):
        return self.Name

class JumlahTanggunganOrangTua(models.Model):
    Name=models.CharField(max_length=100)
    bobot=models.DecimalField(max_digits=3,decimal_places=2)
    def __str__(self):
        return self.Name

class PresentaseKehadiranSiswa(models.Model):
    Name=models.CharField(max_length=100)
    bobot=models.DecimalField(max_digits=3,decimal_places=2)
    def __str__(self):
        return self.Name

class Prestasiyangdiraih(models.Model):
    Name=models.CharField(max_length=100)
    bobot=models.DecimalField(max_digits=3,decimal_places=2)
    def __str__(self):
        return self.Name

class DataSiswa(models.Model):
    jk=(('Laki-laki','Laki-laki'),('Perempuan','Perempuan')) 
    Nama=models.CharField(max_length=100)
    NISN=models.CharField(max_length=10)
    jenis_kelamin=models.CharField(default=1, choices=jk, max_length=30)
    Penghasilan_orangtua=models.ForeignKey(JumlahPenghasilanOrtu, on_delete=models.CASCADE)
    Nilai_ratarata_raport=models.ForeignKey(NilaiRatarataRaport, on_delete=models.CASCADE)
    Jumlah_tanggungan_orang_tua=models.ForeignKey(JumlahTanggunganOrangTua, on_delete=models.CASCADE)
    Presentase_kehadiran_siswa=models.ForeignKey(PresentaseKehadiranSiswa, on_delete=models.CASCADE)
    Prestasi_yang_pernah_diraih=models.ForeignKey(Prestasiyangdiraih, on_delete=models.CASCADE)

    class Meta:
        ordering =['id']
    def __str__(self):
        return self.Nama

class PembobotanKriteria(models.Model):
    cb=(('Cost','Cost'),('Benefit','Benefit'))
    kriteria=models.CharField(max_length=100, null=True, default="")
    Name=models.CharField(max_length=100)
    bobot=models.DecimalField(max_digits=3,decimal_places=2)
    Keterangan=models.CharField(default=1, choices=cb, max_length=30)
    def __str__(self):
        return self.kriteria

class HasilAnalisa(models.Model):
    
    NISN=models.CharField(max_length=100)
    Nama=models.CharField(max_length=100,null=True)
    JenisKelamin=models.CharField(max_length=100, null=True)
    Rangking=models.IntegerField()
    Poin=models.DecimalField(max_digits=5,decimal_places=2)
  





