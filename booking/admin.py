from django.contrib import admin
from .models import Kota, DetailKota, CompanyDelivery, CompanyDeliveryPrice


# Register your models here.
class KotaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nama Kota', {'fields': ['nama_kota']}),
    ]


class DetailKotaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nama Kota', {'fields': ['kota']}),
        ('Kode Post', {'fields': ['nama_alamat', 'kode_post']}),
    ]
    list_display = ('kota', 'nama_alamat', 'kode_post',)
    list_filter = ['kota']
    search_fields = ['kota__nama_kota']


class CompanyDeliveryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Nama Company', {'fields': ['nama', 'pickup_time']}),
        ('Insurance', {'fields': ['price_insurance', 'toc_insurance']}),
    ]
    list_display = ('nama', 'price_insurance', 'pickup_time',)
    list_filter = ['nama']
    search_fields = ['nama']


class CompanyDeliveryPriceAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Perusahaan', {'fields': ['companydelivery']}),
        ('Tujuan', {'fields': ['fr_city', 'to_city']}),
        ('Harga', {'fields': ['normal_price', 'member_price']}),
    ]
    list_display = ('companydelivery', 'fr_city', 'to_city', 'normal_price', 'member_price',)
    list_filter = ['companydelivery']
    search_fields = ['companydelivery__nama']


admin.site.register(Kota, KotaAdmin)
admin.site.register(DetailKota, DetailKotaAdmin)
admin.site.register(CompanyDelivery, CompanyDeliveryAdmin)
admin.site.register(CompanyDeliveryPrice, CompanyDeliveryPriceAdmin)
