from django.forms import ModelForm
from .models import * 
from tkinter import Widget
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields ='__all__'
class DataSiswaform(ModelForm):
    class Meta:
        model=DataSiswa
        fields='__all__'
        widgets={
            'Nama':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'NISN':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'jenis_kelamin':forms.Select(attrs={'class':'form-control','required':True,}),
            'Penghasilan_orangtua':forms.Select(attrs={'class':'form-control','required':True,}),
            'Nilai_ratarata_raport':forms.Select(attrs={'class':'form-control','required':True,}),
            'Jumlah_tanggungan_orang_tua':forms.Select(attrs={'class':'form-control','required':True,}),
            'Presentase_kehadiran_siswa':forms.Select(attrs={'class':'form-control','required':True,}),
            'Prestasi_yang_pernah_diraih':forms.Select(attrs={'class':'form-control','required':True,}),

        }

class pembobotankriteriaform(ModelForm):
    class Meta:
        model=PembobotanKriteria
        fields='__all__'
        widgets={
            'Kriteria':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'Name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'bobot':forms.NumberInput(attrs={'class':'form-control','required':True,'step':0.2}),
        }

class DataTgortuform(ModelForm):
    class Meta:
        model=JumlahTanggunganOrangTua
        fields='__all__'
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'bobot':forms.NumberInput(attrs={'class':'form-control','required':True,'step':0.25}),
        }
class Penghasilanortuform(ModelForm):
    class Meta:
        model=JumlahPenghasilanOrtu
        fields='__all__'
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'bobot':forms.NumberInput(attrs={'class':'form-control','required':True,'step':0.25}),
        }
class PresentaseKehadiranform(ModelForm):
    class Meta:
        model=PresentaseKehadiranSiswa
        fields='__all__'
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'bobot':forms.NumberInput(attrs={'class':'form-control','required':True,'step':0.25}),
        }
class Prestasiform(ModelForm):
    class Meta:
        model=Prestasiyangdiraih
        fields='__all__'
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'bobot':forms.NumberInput(attrs={'class':'form-control','required':True,'step':0.25}),
        }
class Nilaiform(ModelForm):
    class Meta:
        model=NilaiRatarataRaport
        fields='__all__'
        widgets={
            'Name':forms.TextInput(attrs={'class':'form-control','required':True,}),
            'bobot':forms.NumberInput(attrs={'class':'form-control','required':True,'step':0.25}),
        }