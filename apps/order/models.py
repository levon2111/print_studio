import uuid

from django.db import models
from mptt.models import MPTTModel

from apps.core.models import AbstractBaseModel


def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'photo_holder_images/' + filename


class HolderType(MPTTModel, AbstractBaseModel):
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        unique=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Holder Type"

    class MPTTMeta:
        order_insertion_by = ['name']
        parent_attr = 'parent'


class PhotoHolder(AbstractBaseModel):
    """
    name -> holder name (ex: "cup, yellow cup...")
    description -> describe holder, any information about it (ex: "this is big cup for coffee")
    prise -> holder prise (ex: "2400 ")
    type -> holder type (ex: "cup, t_shirt ")
    photo

    """

    type = models.ForeignKey(
        HolderType,
        on_delete=models.CASCADE,
        null=False
    )
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    prise = models.IntegerField(
        null=False,
        blank=False,
    )

    photo = models.ImageField(
        null=False,
        blank=False,
        upload_to=get_file_path
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Photo Holder"


class Order(AbstractBaseModel):
    photo_holder = models.ForeignKey(PhotoHolder, null=False, blank=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, blank=False)
    phone = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Order'
