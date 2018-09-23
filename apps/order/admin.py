from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin

from apps.order.models import HolderType, PhotoHolder, Order


@admin.register(HolderType)
class HolderTypeModel(DjangoMpttAdmin):
    pass


@admin.register(PhotoHolder)
class PhotoHolderAdmin(admin.ModelAdmin):
    list_display = [
        'type',
        'name',
        'description',
        'prise',
        'photo',
    ]


@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = [
        'photo_holder',
        'name',
        'email',
        'phone',
        'address',
    ]
