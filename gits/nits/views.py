# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return HttpResponse("Hello wordl")

def about(request):
	return Http Response("About")
