from re import search
from django.shortcuts import render

# Create your views here.
from .models import Post

def main(request):
    if request.method=="POST":
        search = request.POST['qidiruv']
        posts = Post.objects.filter(sarlavha__icontains=search)
        return render(request,'blog/qidiruv.html',{"postlar":posts})
    postlar = Post.objects.all()
    return render(request,'blog/asosiy.html',{"postlar":postlar})

def post_detal(request,id):
    if request.method=="POST":
        search = request.POST['qidiruv']
        posts = Post.objects.filter(sarlavha__icontains=search)
        return render(request,'blog/qidiruv.html',{"postlar":posts})
    post=Post.objects.get(id=id)
    post.kurishlar=post.kurishlar+1
    post.save()
    return render(request,'blog/post_detallar.html',{"post":post})  

def mashxur(request):
    if request.method=="POST":
        search = request.POST['qidiruv']
        postlar = Post.objects.filter(malumot__icontains=search)
        return render(request,'blog/qidiruv.html',{"postlar":postlar})
    post = Post.objects.all().order_by('-kurishlar')
    return render(request,'blog/mashxur.html',{"post":post})  



    
    