﻿# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("欢迎来到白色空间！")
