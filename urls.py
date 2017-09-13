# coding: utf-8
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

import views

from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)



urlpatterns = [
    #成功页面
    # url(r'^', include(router.urls)),
    url(r'^$', views.index, name='#'),
    url(r'^success/$', views.successPage, name='success'),
    url(r'^NoFound/$', views.NoFound, name='NoFound'),
    url(r'^PrivatePolicy/$', views.PrivatePolicy, name='PrivatePolicy'),
    url(r'^$', views.mainPage, name=''),
    # 订单管理
    url(r'^Order/', include('Order.urls', namespace='Order')),
    # 店铺管理
    url(r'^Shop/', include('Shop.urls', namespace='Shop')),
    #用户管理，包括登陆、注册、忘记密码。
    url(r'^Account/', include('Account.urls', namespace='Account')),
    url(r'^Admin/', include('Admin.urls', namespace='Admin')),
    # 商品管理
    url(r'^Product/', include('Product.urls', namespace='Product')),
    # 首页推荐
    url(r'^Recommendation/', include('Recommendation.urls', namespace='Recommendation')),
    # 售后
    url(r'^AfterSale/', include('AfterSale.urls', namespace='AfterSale')),
    # 初始化
    url(r'^Initiation/', include('Initiation.urls', namespace='Initiation')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
