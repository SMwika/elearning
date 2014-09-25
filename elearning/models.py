from django.db import models
#from django.contrib.auth.models import User

"""
    base model untuk menyimpan user add, user modify, add date dan modify date
"""
"""
class Emodel(models.Model):
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    useradd = models.ForeignKey(User)
    useredit = models.CharField(max_length=255)
"""


"""
    Model Anggota
"""
"""
class Anggota(models.Model):
    user  = models.OneToOneField(User, primary_key=True)
    username = models.CharField(max_length=255,blank=False, null=False, unique= True)
    password  = models.CharField(max_length=255,blank=False, null=False)
    nama = models.CharField(max_length=255,blank=False, null=False)
    email = models.CharField(max_length=255,blank=False, null=False)

    def __str__(self):
        return self.username
    def daftar(self):
        return self.save()
"""

"""
    Model KursusKategori
"""
"""
class KursusKategori(models.Model):
    KURSUS_KATEGORI_ID =0
    nama  = models.CharField(max_length=255)
    #children = models.ManyToManyField("self", blank=True)
    #parent = models.ForeignKey('self', blank=True, null=True)
    #parent = models.ForeignKey('self', blank=True, null= True, default=0)
    #parent = models.ManyToManyField("self", blank=True, null= True, related_name="children")
    def __str__(self):
        return self.nama
"""

class KategoriKursus(models.Model):
    nama = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null= True, default=0)
    def __str__(self):
        return self.nama

"""
    Model Kursus
"""
class Kursus(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_mulai = models.DateField('tanggal mulai')
    tanggal_selesai = models.DateField('tanggal selesai')
    keterangan = models.CharField(max_length=255)
    #tutor = models.ForeignKey(User)
    status = models.IntegerField(default=0)
    kategori = models.ForeignKey(KategoriKursus)

    def __str__(self):
        return self.nama

"""
    Model KursusRelAnggota
"""
class KursusRelAnggota(models.Model):
    #anggota = models.ForeignKey(User)
    kursus = models.ForeignKey(Kursus)
    posisi = models.CharField(max_length=255,blank=False, null=False)

    def __str_(self):
        return self.anggota.nama + " " + self.kursus.nama



"""
    Model Anggota Akses Kursus
"""
class AnggotaAksesKursus(models.Model):
    #anggota = models.ForeignKey(User)
    kursus = models.ForeignKey(Kursus)
    tanggal_mulai = models.DateField("tanggal mulai")
    tanggal_selesai = models.DateField("tanggal selesai")

    def __str__(self):
        return anggota.nama + " " + kursus.nama

"""
    Model Materi
"""
class Materi(models.Model):
    nama = models.CharField(max_length=255)

    id_kursus = models.ForeignKey(Kursus)

    def __str__(self):
        return self.nama

"""
    Model MateriIsi
"""
class MateriIsi(models.Model):
    judul = models.CharField(max_length=255)
    id_materi = models.ForeignKey(Materi)

    def __str__(self):
        return self.judul

"""
    Model kuis
"""
class Kuis(models.Model):
    nama = models.CharField(max_length=255)
    tanggal_mulai = models.DateField("tanggal mulai")
    tanggal_selesai = models.DateField("tanggal selesai")
    kursus = models.ForeignKey(Kursus)

    def __str__(self):
        return self.nama
"""
    Model KuisPertanyaan
"""
class KuisPertanyaan(models.Model):
    pertanyaan = models.CharField(max_length=255)
    jenis = models.CharField(max_length = 255)
    kuis = models.ForeignKey(Kuis)

    def __str__(self):
        return self.pertanyaan


"""
    Model KuisJawaban
"""
class KuisJawaban(models.Model):
    jawaban  = models.CharField(max_length=255)
    pertanyaan = models.ForeignKey(KuisPertanyaan)

    def __str__(self):
        return self.jawaban
