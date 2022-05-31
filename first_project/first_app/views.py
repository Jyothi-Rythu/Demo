clicked =0
from django.shortcuts import render
from django.http import HttpResponse

def index(request) :
    clicked=clicked+1
    inject_var=clicked
    my_dict = { 'inject_var' : "This is an injected content"}
    return render(request,'index.html',context=my_dict)
