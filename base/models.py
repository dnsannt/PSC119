from re import L
from django.db import models

from django.contrib.auth.models import User


# class User(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     DOKTER = 'DR',
#     IT = 'IT',
#     ADMIN = 'ADM',
#     PERAWAT = 'PR',
#     DRIVER = 'DRV'

#     PROFESI = [
#         ('DOKTER', 'DOKTER'),
#         ('IT', 'IT'),
#         ('ADMIN', 'ADMIN'),
#         ('PERAWAT', 'PERAWAT'),
#         ('DRIVER', 'DRIVER'),
#     ]
#     profesi = models.CharField(
#         max_length=10,
#         choices=PROFESI,
#         default=IT,
#     )

#     class Meta:
#         verbose_name_plural = "User"


# class Rm(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     norm = models.CharField(max_length=200)
#     nama = models.CharField(max_length=200, null=False)
#     umur = models.CharField(max_length=100)
#     lakilaki = 'Laki-Laki',
#     wanita = 'Wanita'
#     jk = [
#         ('Wanita', 'Wanita'),
#         ('Laki-Laki', 'Laki-Laki'),
#     ]
#     jk = models.CharField(
#         max_length=10,
#         choices=jk,
#         default=lakilaki
#     )

#     tlp = models.CharField(max_length=50)
#     alamat = models.CharField(max_length=200)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#     anamnesis = models.CharField(max_length=200)
#     diagnosis = models.CharField(max_length=200)
#     td = models.CharField(max_length=100)
#     terapi = models.CharField(max_length=200)

#     class Meta:
#         verbose_name_plural = "RekamMedis"
#         ordering = ['-updated', '-created']


# class Card(models.Model):
#     nama = models.ForeignKey(Rm, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = "KartuBerobat"


# class Apotik(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     nama = models.CharField(max_length=200)
#     cair = 'Cair',
#     tablet = 'Tablet',
#     salep = 'Salep',
#     jenis = [
#         ('Cair', 'Cair'),
#         ('Tablet', 'Tablet'),
#         ('Salep', 'Salep')
#     ]
#     jenis = models.CharField(
#         max_length=100,
#         choices=jenis,
#         default=tablet
#     )
#     stok = models.IntegerField()
#     BOX = 'BOX'
#     PCS = 'PCS'
#     TYPE = [
#         ('BOX', 'BOX'),
#         ('PCS', 'PCS'),
#     ]
#     type = models.CharField(
#         max_length=10,
#         choices=TYPE,
#         default=BOX,
#     )
#     dosis = models.CharField(max_length=50)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)
#     exp = models.DateField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Apotik"
#         ordering = ['-updated', '-created']


# class Transaksi(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     nama = models.ForeignKey(Rm, on_delete=models.CASCADE)
#     obat = models.ForeignKey(Apotik, on_delete=models.CASCADE)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name_plural = "Transaksi"
#         ordering = ['-updated', '-created']
