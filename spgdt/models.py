from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

from embed_video.fields import EmbedVideoField


class Telp(models.Model):
    nama = models.CharField(max_length=200, null=True)
    notelp = models.CharField(max_length=200, null=True)
    lokasi = models.CharField(max_length=200, null=True)
    kategori = models.CharField(max_length=200, null=True)
    subkategori = models.CharField(max_length=200, null=True)
    detailkategori = models.CharField(max_length=200, null=True)
    keterangan = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True)
    startcall = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Telp"

    def __str__(self):
        return self.nama


class Pbfree(models.Model):
    nama = models.CharField(max_length=200)
    jk = models.CharField(max_length=10)
    td = models.CharField(max_length=200, null=True)
    usia = models.IntegerField(null=True)
    dx = models.CharField(max_length=200, null=True, blank=True)
    alamat = models.CharField(max_length=200)
    nohp = models.CharField(max_length=200, null=True)
    tgl = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Pengobatan"

    def __str__(self):
        return self.nama


class Giat(models.Model):
    ket = models.CharField(max_length=200)
    giat = models.CharField(max_length=200)
    lokasi = models.CharField(max_length=200)
    tgl = models.DateField(null=True)

    class Meta:
        verbose_name_plural = "Giat"

    def __str__(self):
        return self.ket


# menggunakan database dan import video langsung ke dalam folder file project
class Video(models.Model):
    giat = models.ForeignKey(Giat, on_delete=models.SET_NULL, null=True)
    video = models.FileField(upload_to="filevideo/%y")

    class Meta:
        verbose_name_plural = "Video"

    def __str__(self):
        return self.giat


# menggunakan url youtube
class Video_giat(models.Model):
    giat = models.ForeignKey(Giat, on_delete=models.SET_NULL, null=True)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.giat)

    class Meta:
        ordering = ['-added']
        verbose_name_plural = "Video_giat"
