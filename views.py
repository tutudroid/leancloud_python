# coding: utf-8

from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
import tempfile
import leancloud


def successPage(request):
    return render(request, 'result.html', {})


def NoFound(request):
    if request.method == 'POST':
        dataString = request.POST.get('detailDescription')
        tup = tempfile.mkstemp()
        file = open(tup[0], 'wb+')
        file.write(bytes(dataString, encoding = "utf8") )
        lc_file = leancloud.File('detailDescription', data=file)
        Test = leancloud.Object.extend('test')
        test = Test()
        test.set('detailDescription', lc_file)
        test.save()
        url = test.get('detailDescription')

        return render(request, '404.html', {'detailDescription': url})

    return render(request, '404.html')


def mainPage(request):
    return HttpResponseRedirect('/Account/Login/')


def PrivatePolicy(request):
    return render(request, 'PrivatePolicy.html')


def index(request):
    return render(request, 'login.html')
