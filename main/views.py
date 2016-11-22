# -*- coding: utf-8 -*-
from django.shortcuts import render
from main.forms import ContactusForm
from django.contrib import messages

def index(request):
	if request.method == 'POST':
		form = ContactusForm(request.POST)
			# check whether it's valid:
		if form.is_valid():
		# process the data in form.cleaned_data as required
			form.save()
			# redirect to a new URL:
			messages.info(request, "Մենք ստացանք Ձեր նամակը, շուտով կպատասխանենք։ Շնորհակալություն")
		else:
			messages.error(request, "Ձեր նամակը դեռ չի ուղարկվել։ Խնդրում ենք լրացնել բոլոր դաշտերը։")
	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactusForm()

	return render(request,'main/index.html',{'form':form})

def contactus(request):
	pass