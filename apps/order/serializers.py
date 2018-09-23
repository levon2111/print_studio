from rest_framework import serializers

from apps.order.models import HolderType, PhotoHolder, Order


class HolderTypeSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = HolderType
        fields = [
            'id',
            'name',
            'parent',
        ]


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    photo_holder = serializers.PrimaryKeyRelatedField(
        queryset=PhotoHolder.objects.all(),
        allow_empty=False,
        allow_null=False,

    )
    name = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    email = serializers.EmailField(max_length=255, allow_null=False, allow_blank=False)
    phone = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)
    address = serializers.CharField(max_length=255, allow_null=False, allow_blank=False)

    class Meta:
        model = Order
        fields = [
            'id',
            'photo_holder',
            'name',
            'email',
            'phone',
            'address',
        ]
