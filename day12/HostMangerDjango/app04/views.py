#!/usr/bin/env python
# _*_ coding:utf8 _*_
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http.response import HttpResponse
import json
# Create your views here.
def Ajax(request):
    if request.method == 'POST':
        print request.POST
        data = {'status':0,'msg':'请求成功','data':[11,22,33,44,55]}
        return HttpResponse(json.dumps(data))
    else:
        return render_to_response('app04/ajax.html')