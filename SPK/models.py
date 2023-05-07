from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist

# Create your models here.
class Alternatif(models.Model):
    simbol          = models.CharField(max_length=50, unique=True)
    nik             = models.IntegerField()
    nama_alternatif = models.CharField(max_length=50, unique=True)
    alamat          = models.TextField()

    def __str__(self):
        return str(self.nama_alternatif)

class Kriteria(models.Model):
    simbol          = models.CharField(max_length=50)
    nama_kriteria   = models.CharField(max_length=50)
    bobot           = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.nama_kriteria

class SubKriteria(models.Model):
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    nama_sub_kriteria = models.CharField(max_length=50)
    nilai_sub_kriteria = models.IntegerField()

    def __str__(self):
        return self.nama_sub_kriteria

class Penilaian(models.Model):
    simbol = models.ForeignKey(Alternatif, on_delete=models.CASCADE, related_name='penilaian_simbol', to_field='simbol')
    nama = models.ForeignKey(Alternatif, on_delete=models.CASCADE, related_name='penilaian_nama', to_field='nama_alternatif')
    kondisi_rumah = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_kondisi_rumah')
    penghasilan = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_penghasilan')
    bumil_dan_bunsui = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_bumil_dan_bunsui')
    lansia = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_lansia')
    anak_sekolah = models.ForeignKey(SubKriteria, on_delete=models.CASCADE, related_name='penilaian_anak_sekolah')

    def __str__(self):
        return str(self.simbol)

    @property
    def nilai_kondisi_rumah(self):
        return self.kondisi_rumah.nilai_sub_kriteria

    @property
    def nilai_penghasilan(self):
        return self.penghasilan.nilai_sub_kriteria

    @property
    def nilai_bumil_dan_bunsui(self):
        return self.bumil_dan_bunsui.nilai_sub_kriteria

    @property
    def nilai_lansia(self):
        return self.lansia.nilai_sub_kriteria

    @property
    def nilai_anak_sekolah(self):
        return self.anak_sekolah.nilai_sub_kriteria
