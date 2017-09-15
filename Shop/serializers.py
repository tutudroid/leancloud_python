from rest_framework import serializers


class SettleSerializer(serializers.Serializer):
    created = serializers.DateTimeField(auto_now_add=True)
    shopName = serializers.CharField(max_length=20, blank=True, default='defaultShopName')
    brandName = serializers.CharField(max_length=20, blank=True, default='defaultBrandName')
    brandLogo = serializers.CharField(default=False)
    brandDescription = serializers.CharField()
    alipay = serializers.CharField(cdefault='alipay', max_length=20)
