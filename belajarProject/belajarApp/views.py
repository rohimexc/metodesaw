from collections import UserString
from curses import noraw
from multiprocessing import context
from timeit import repeat
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
import numpy as np
import pandas as pd
from .models import *
from .form import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

def loginPage(request):
    page='login'
    if request.method=='POST':
        if request.user.is_authenticated:
            return redirect('index')

        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except: 
            messages.error(request,'User belum terdaftar')
        user=authenticate(request, username=username, password=password)     
        if user is not None:
           login(request,user)
           return redirect('index') 
        else:
            messages.error(request,'User atau password salah')
    
    context={'page':page}
    return render(request,'indriapp/login.html', context )

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    user=User.objects.all()
    if request.method=='POST':

        username = request.POST.get('username')
        password =request.POST.get('exampleinputpassword')
        repeat_password=request.POST.get('examplerepeatpassword')
        user.username = username
        user.password = password
        user.password_confirmation = repeat_password
        user.save()
        return redirect('home')
    return render(request,'indriapp/register.html')

def home(request):
    q=request.GET.get('q') if request.GET.get('q') != None else ''
    rooms=Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    topic=Topic.objects.all()
    room_count=rooms.count()
    context = {'rooms':rooms, 'topic':topic,'room_count':room_count}
    return render(request,'belajarApp/home.html',context)
def room(request,pk):
    room =Room.objects.get(id=pk) 
    context ={'room':room}
    return render(request,'belajarApp/room.html',context)
@login_required(login_url='login')
def createForm(request):
    form=RoomForm()
    
    if request.method=='POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,"belajarApp/form.html",context)
@login_required(login_url='login')
def updateForm(request,pk):
    room=Room.objects.get(id=pk)
    form=RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse('Kamu tidak dibolehkan disini')
    if request.method=='POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={'form':form}
    return render(request,'belajarApp/form.html', context)
@login_required(login_url='login')
def deleteForm(request,pk):
    room=Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse('Kamu tidak dibolehkan disini')
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    return render(request,'belajarApp/delete.html', {'obj':room})
@login_required(login_url='login')
def index(request):
    jumlahsiswa=DataSiswa.objects.all().count()
    context={"jumlahsiswa":jumlahsiswa}
    return render(request,"indriapp/index.html",context)

def datasiswa(request):
    datasiswa=DataSiswa.objects.all()
    context={'tabel':datasiswa}
    return render(request, 'indriapp/datasiswa.html',context)
def adddatasiswa(request):
    judul="Tambah Data Siswa"
    form = DataSiswaform()
    if request.method=='POST':
        form=DataSiswaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('datasiswa')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def updatedatasiswa(request,pk):
    judul="Update Data Siswa"
    datasiswa=DataSiswa.objects.get(id=pk)
    form = DataSiswaform(instance=datasiswa)
    if request.method=='POST':
        form=DataSiswaform(request.POST,instance=datasiswa)
        if form.is_valid():
            form.save()
            return redirect('datasiswa')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def deletedatasiswa(request,pk):
    datasiswa=DataSiswa.objects.get(id=pk)
    if request.method=='POST':
        datasiswa.delete()
        return redirect('datasiswa')
    return render(request, 'indriapp/delete.html',{"objek":datasiswa})

def datajmltgortu(request):
    data=JumlahTanggunganOrangTua.objects.all()
    context={'tabel':data}
    return render(request, 'indriapp/jumlahtanggunganorangtua.html',context)
def adddatajmltgortu(request):
    judul="Tambah Data Jumlah Tanggungan Orang Tua"
    form = DataTgortuform()
    if request.method=='POST':
        form=DataTgortuform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jumlahtanggunganorangtua')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def updatedatajmltgortu(request,pk):
    judul="Update Data Tanggungan Orang Tua"
    data=JumlahTanggunganOrangTua.objects.get(id=pk)
    form = DataTgortuform(instance=data)
    if request.method=='POST':
        form=DataTgortuform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('jumlahtanggunganorangtua')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def deletedatajmltgortu(request,pk):
    datasiswa=JumlahTanggunganOrangTua.objects.get(id=pk)
    if request.method=='POST':
        datasiswa.delete()
        return redirect('jumlahtanggunganorangtua')
    return render(request, 'indriapp/delete.html',{"objek":datasiswa})
def datajmlpeortu(request):
    data=JumlahPenghasilanOrtu.objects.all()
    context={'tabel':data}
    return render(request, 'indriapp/penghasilanorangtua.html',context)
def adddatajmlpeortu(request):
    judul="Tambah Data Jumlah Penghasilan Orang Tua"
    form = Penghasilanortuform()
    if request.method=='POST':
        form=Penghasilanortuform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jumlahpenghasilanorangtua')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def updatedatajmlpeortu(request,pk):
    judul="Update Data Jumlah Penghasilan Orang Tua"
    data=JumlahPenghasilanOrtu.objects.get(id=pk)
    form = Penghasilanortuform(instance=data)
    if request.method=='POST':
        form=Penghasilanortuform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('jumlahpenghasilanorangtua')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def deletedatajmlpeortu(request,pk):
    data=JumlahPenghasilanOrtu.objects.get(id=pk)
    if request.method=='POST':
        data.delete()
        return redirect('jumlahpenghasilanorangtua')
    return render(request, 'indriapp/delete.html',{"objek":data})
def nilairaport(request):
    data=NilaiRatarataRaport.objects.all()
    context={'tabel':data}
    return render(request, 'indriapp/nilairaport.html',context)
def addnilairaport(request):
    judul="Tambah nilai raport"
    form = Nilaiform()
    if request.method=='POST':
        form=Nilaiform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('datanilairaport')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def updatenilairaport(request,pk):
    judul="Update Data Jumlah Penghasilan Orang Tua"
    data=NilaiRatarataRaport.objects.get(id=pk)
    form = Nilaiform(instance=data)
    if request.method=='POST':
        form=Nilaiform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('datanilairaport')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def deletenilairaport(request,pk):
    data=NilaiRatarataRaport.objects.get(id=pk)
    if request.method=='POST':
        data.delete()
        return redirect('datanilairaport')
    return render(request, 'indriapp/delete.html',{"objek":data})
def presentasekehadiransiswa(request):
    data=PresentaseKehadiranSiswa.objects.all()
    context={'tabel':data}
    return render(request, 'indriapp/presentasekehadiransiswa.html',context)
def addpresentasekehadiransiswa(request):
    judul="Tambah Data Presentase Kehadiran Siswa"
    form = PresentaseKehadiranform()
    if request.method=='POST':
        form=PresentaseKehadiranform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('presentasekehadiransiswa')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def updatepresentasekehadiransiswa(request,pk):
    judul="Update Data Presentase Kehadiran Siswa"
    data=PresentaseKehadiranSiswa.objects.get(id=pk)
    form = PresentaseKehadiranform(instance=data)
    if request.method=='POST':
        form=PresentaseKehadiranform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('presentasekehadiransiswa')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def deletepresentasikehadiransiswa(request,pk):
    data=PresentaseKehadiranSiswa.objects.get(id=pk)
    if request.method=='POST':
        data.delete()
        return redirect('presentasekehadiransiswa')
    return render(request, 'indriapp/delete.html',{"objek":data})
def prestasi(request):
    data=Prestasiyangdiraih.objects.all()
    context={'tabel':data}
    return render(request, 'indriapp/prestasiyangpernahdiraih.html',context)
def addprestasi(request):
    judul="Tambah Data Prestasi"
    form = Prestasiform()
    if request.method=='POST':
        form=Prestasiform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dataprestasi')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def updateprestasi(request,pk):
    judul="Update Data Prestasi"
    data=Prestasiyangdiraih.objects.get(id=pk)
    form = Prestasiform(instance=data)
    if request.method=='POST':
        form=Prestasiform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('dataprestasi')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def deleteprestasi(request,pk):
    data=Prestasiyangdiraih.objects.get(id=pk)
    if request.method=='POST':
        data.delete()
        return redirect('dataprestasi')
    return render(request, 'indriapp/delete.html',{"objek":data})
def pembobotankriteria(request):
    data=PembobotanKriteria.objects.all()
    context={'tabel':data}
    return render(request, 'indriapp/pembobotankriteria.html',context)
def addpembobotankriteria(request):
    judul="Tambah Data pembobotan kriteria"
    form = pembobotankriteriaform()
    if request.method=='POST':
        form=pembobotankriteriaform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pembobotankriteria')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def updatepembobotankriteria(request,pk):
    judul="Update Data pembobotan kriteria"
    data=PembobotanKriteria.objects.get(id=pk)
    form = pembobotankriteriaform(instance=data)
    if request.method=='POST':
        form=pembobotankriteriaform(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('pembobotankriteria')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'judul':judul}
    return render(request, 'indriapp/adddata.html',context)
def deletepembobotankriteria(request,pk):
    data=PembobotanKriteria.objects.get(id=pk)
    if request.method=='POST':
        data.delete()
        return redirect('pembobotankriteria')
    return render(request, 'indriapp/delete.html',{"objek":data})

def Hasilanalisa(request):
    
    datahapus=HasilAnalisa.objects.all()
    datahapus.delete()
    info=0
    if request.method=='POST':
        info=1

    alternatif=list(DataSiswa.objects.values_list("NISN",flat= True))
    NamaSiswa=list(DataSiswa.objects.values_list("Nama",flat= True))
    JKSiswa=list(DataSiswa.objects.values_list("jenis_kelamin",flat= True))
    A1=list(DataSiswa.objects.values_list("Penghasilan_orangtua__bobot",flat= True))
    A2=list(DataSiswa.objects.values_list("Nilai_ratarata_raport__bobot",flat= True))
    A3=list(DataSiswa.objects.values_list("Jumlah_tanggungan_orang_tua__bobot",flat= True))
    A4=list(DataSiswa.objects.values_list("Presentase_kehadiran_siswa__bobot",flat= True))
    A5=list(DataSiswa.objects.values_list("Prestasi_yang_pernah_diraih__bobot",flat= True))
    kriteria=list(PembobotanKriteria.objects.values_list("Name",flat= True))
    costbenefit=list(PembobotanKriteria.objects.values_list("Keterangan",flat= True))
    kepentingan=list(PembobotanKriteria.objects.values_list("bobot",flat= True))
    rows, cols = (len(A1), 5)
    alternatifkriteria = [[0]*cols]*rows
    for a in range(len(A1)):
        for b in range(len(A2)):
            for c in range(len(A3)):
                for d in range(len(A4)):
                    for e in range(len(A5)):
                        if a==b==c==d==e:
                            alternatifkriteria[a]=[A1[a],A2[b],A3[c],A4[d],A5[e]]
    #pembagi
    print(NamaSiswa)
    print(alternatifkriteria)
    pembagi=[]
    for i in range(len(kriteria)):
        pembagi.append(0)
        for j in range(len(alternatif)):
            if costbenefit[i] == 'Cost':
                if j == 0:
                    pembagi[i] =alternatifkriteria[j][i]
                    
                else:
                    if pembagi [i] > alternatifkriteria[j][i]:
                        pembagi [i] = alternatifkriteria[j][i]
            else:
                if j == 0:
                    pembagi[i] =alternatifkriteria[j][i]
                    
                else:
                    if pembagi [i] < alternatifkriteria[j][i]:
                        pembagi [i] = alternatifkriteria[j][i]
                
    #normalisasi
    
    normalisasi=[]
    for i in range(len(alternatif)):
        normalisasi.append([])
        for j in range(len(kriteria)):
            normalisasi[i].append(0)
            if costbenefit[j] == 'Cost':
                normalisasi[i][j]=pembagi[j] / alternatifkriteria[i][j]

            else:

                normalisasi[i][j]= round(alternatifkriteria[i][j] / pembagi[j],2)
    #hasil

    hasil=[]
    for i in range(len(alternatif)):
        hasil.append(0)
        for j in range(len(kriteria)):
            hasil[i]=hasil[i]+(normalisasi[i][j]*kepentingan[j])

    print(hasil)
    rangking=[]
    for a in range(len(alternatif)):
        rangking.append(a+1)
    
    tabel = pd.DataFrame({
        
    'NISN': alternatif,
    'Nama': NamaSiswa,
    'JK' : JKSiswa,
    'Poin':hasil,
        })
    tabelsort=tabel.sort_values(['Poin'],ascending=False)
    hasil_nama=tabelsort['Nama'].values.tolist()
    hasil_jk=tabelsort['JK'].values.tolist()
    hasil_nisn=tabelsort['NISN'].values.tolist()
    hasil_poin=tabelsort['Poin'].values.tolist()

    for i,a in enumerate(hasil_nisn):
        for j,b in enumerate(hasil_nama):
            for k,c in enumerate(hasil_jk):
                for l,d in enumerate(hasil_poin):
                    for m,e in enumerate(rangking):
                        if i==j==k==l==m:
                            HasilAnalisa.objects.create(
                                NISN=a,
                                Nama=b,
                                JenisKelamin=c,
                                Poin=d,
                                Rangking=e
                            )
    data=HasilAnalisa.objects.all()
    
    context={'tabel':data, 'info':info, 'alternatifkriteria':alternatifkriteria,
    'pembagi':pembagi, 'normalisasi':normalisasi, 'hasil':hasil}
    return render(request, 'indriapp/hasilanalisa.html',context)