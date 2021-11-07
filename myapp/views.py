from django.shortcuts import render
from .models import Post
from .forms import PostForm

def index(request):
    form=PostForm()
    return render(request,'index.html',{'form':form})