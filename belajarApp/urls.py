from django.urls import path
from . import views

urlpatterns = [
    path('coba',views.home, name="home"),
    path('login',views.loginPage, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path('register',views.registerUser, name="register"),
    path('room/<str:pk>',views.room,name='room'),
    path('createForm',views.createForm, name='createForm'),
    path('updateForm/<str:pk>',views.updateForm, name='updateForm'),
    path('deleteForm/<str:pk>',views.deleteForm, name='deleteForm'),
    path('datasiswa/',views.datasiswa, name='datasiswa'),
    path('adddatasiswa/',views.adddatasiswa, name='adddatasiswa'),
    path('updatedatasiswa/<str:pk>',views.updatedatasiswa, name='updatedatasiswa'),
    path('deletedatasiswa/<str:pk>',views.deletedatasiswa, name='deletedatasiswa'),

    path('datajmlpeortu/',views.datajmlpeortu, name='datajmlpeortu'),
    path('adddatajmlpeortu/',views.adddatajmlpeortu, name='adddatajmlpeortu'),
    path('updatedatajmlpeortu/<str:pk>',views.updatedatajmlpeortu, name='updatedatajmlpeortu'),
    path('deletedatajmlpeortu/<str:pk>',views.deletedatajmlpeortu, name='deletedatajmlpeortu'),

    path('datajmltgortu/',views.datajmltgortu, name='datajmltgortu'),
    path('addjmltgortu/',views.adddatajmltgortu, name='addjmltgortu'),
    path('updatejmltgortu/<str:pk>',views.updatedatajmltgortu, name='updatejmltgortu'),
    path('deletejmltgortu/<str:pk>',views.deletedatajmltgortu, name='deletejmltgortu'),
    
    path('datanilairaport/',views.nilairaport, name='datanilairaport'),
    path('addnilairaport/',views.addnilairaport, name='addnilairaport'),
    path('updatenilairaport/<str:pk>',views.updatenilairaport, name='updatenilairaport'),
    path('deletenilairaport/<str:pk>',views.deletenilairaport, name='deletenilairaport'),

    path('datapresentasekehadiransiswa/',views.presentasekehadiransiswa, name='datapresentasekehadiransiswa'),
    path('addpresentasekehadiransiswa/',views.addpresentasekehadiransiswa, name='addpresentasekehadiransiswa'),
    path('updatepresentasekehadiransiswa/<str:pk>',views.updatepresentasekehadiransiswa, name='updatepresentasekehadiransiswa'),
    path('deletepresentasekehadiransiswa/<str:pk>',views.deletepresentasikehadiransiswa, name='deletepresentasekehadiransiswa'),

    path('dataprestasi/',views.prestasi, name='dataprestasi'),
    path('addprestasi/',views.addprestasi, name='addprestasi'),
    path('updateprestasi/<str:pk>',views.updateprestasi, name='updateprestasi'),
    path('deleteprestasi/<str:pk>',views.deleteprestasi, name='deleteprestasi'),

    path('datapembobotankriteria/',views.pembobotankriteria, name='pembobotankriteria'),
    path('addpembobotankriteria/',views.addpembobotankriteria, name='addpembobotankriteria'),
    path('updatepembobotankriteria/<str:pk>',views.updatepembobotankriteria, name='updatepembobotankriteria'),
    path('deletepembobotankriteria/<str:pk>',views.deletepembobotankriteria, name='deletepembobotankriteria'),

    path('dataprestasi/',views.prestasi, name='dataprestasi'),
    path('addprestasi/',views.addprestasi, name='addprestasi'),
    path('updateprestasi/<str:pk>',views.updateprestasi, name='updateprestasi'),
    path('deleteprestasi/<str:pk>',views.deleteprestasi, name='deleteprestasi'),

    path('Hasilanalisa/',views.Hasilanalisa, name='Hasilanalisa'),
    
    path('',views.index, name="index"),

]