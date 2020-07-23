from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from . import models

# from .models import Post
# 사용시 models.Post 대신 Post로 사용 가능

def main(request):
    return render(request, "post/main.html")


def post_list(request):

    all_posts = models.Post.objects.all()
    #all_posts는 Post모델로 만들어진 Post 객체가 리스트로 담긴다.
    ctx = {
        "posts":all_posts
    }
    return render(request, "post/post_list.html",ctx)


def post_detail(request, pk):
    post1 = models.Post.objects.get(pk=pk)
    ctx = {
        "post":post1
    }
    return render(request, "post/post_detail.html",ctx)





def post_create(request):
    if request.method == "POST":

        new_Post=models.Post.objects.create(
            title=request.POST.get("tit"),
            writer=request.POST.get("wri"),
            content=request.POST.get("con"),
        )


        new_pk=new_Post.pk
        address='/post/post_list/'+str(new_pk)+'/'
        # return redirect(address)

        return redirect(reverse('post:post_d',kwargs={'pk':new_pk}))




    else:
        # get요청처리
        return render(request, "post/post_create.html")


def post_update(request, pk):
    uPost = models.Post.objects.get(pk=pk)
    if request.method == "POST":



        uPost.title=request.POST.get("tit")
        uPost.writer=request.POST.get("wri")
        uPost.content=request.POST.get("con")

        uPost.save()


        return redirect(reverse('post:post_d',kwargs={'pk':pk}))

    else:
        ctx={"post":uPost}
        # get요청처리
        return render(request, "post/post_update.html", ctx)



def post_delete(request,pk):
    if request.method == "POST":
        post=models.Post.objects.get(pk=pk)
        post.delete()

    # return redirect("/post/post_list")
    return redirect(reverse("post:post_l"))