from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Kota(models.Model):
    nama_kota = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kota


class DetailKota(models.Model):
    kota = models.ForeignKey(Kota)
    nama_alamat = models.CharField(max_length=50)
    kode_post = models.IntegerField(default=0)

    # def namakode(self):
    #     return self.('')

    def __str__(self):
        return self.nama_alamat


class CompanyDelivery(models.Model):
    nama = models.CharField(max_length=25)
    price_insurance = models.IntegerField(default=0)
    toc_insurance = models.TextField()
    pickup_time = models.TimeField(default=datetime.time)

    def __str__(self):
        return self.nama


class CompanyDeliveryPrice(models.Model):
    fr_city = models.ForeignKey(Kota, related_name='price_fr_city_list_kota')
    to_city = models.ForeignKey(Kota, related_name='price_to_city_list_kota')
    normal_price = models.IntegerField(default=0)
    member_price = models.IntegerField(default=0)
    companydelivery = models.ForeignKey(CompanyDelivery)


class Booking(models.Model):
    fr_city = models.ForeignKey(Kota, related_name='fr_city_list_kota')
    fr_code_post = models.ForeignKey(DetailKota, related_name='fr_code_post_code_post')
    to_city = models.ForeignKey(Kota, related_name='to_city_list_kota')
    to_code_post = models.ForeignKey(DetailKota, related_name='to_code_post_code_post')
    company_delivery = models.ForeignKey(CompanyDelivery)
    # user = models.ForeignKey('user_profile.MyUser')
    book_user = models.ForeignKey('auth.User')
    book_date = models.DateTimeField(default=timezone.now)
    weight = models.IntegerField(default=0)
    pay_price = models.IntegerField(default=0)
    sudah_bayar = models.BooleanField(default='false')
    pay_date = models.DateTimeField(blank=True, null=True)
#
#
# class BookingDetail(models.Model):
#     booking = models.ForeignKey(Booking)
#     ship_name = models.CharField(max_length=25)
#     ship_address = models.TextField
#     ship_phone = models.CharField(max_length=20)
#     ship_email = models.EmailField(max_length=35)
#     receive_name = models.CharField(max_length=25)
#     receive_address = models.TextField
#     receive_phone = models.CharField(max_length=20)
#     receive_email = models.EmailField(max_length=35)
