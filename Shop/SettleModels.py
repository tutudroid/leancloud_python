from django.db import models


class Settle(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    shopName = models.CharField(max_length=20, blank=True, default='defaultShopName')
    brandName = models.CharField(max_length=20, blank=True, default='defaultBrandName')
    brandLogo = models.CharField(default=False)
    brandDescription = models.CharField()
    alipay = models.CharField(cdefault='alipay', max_length=20)
