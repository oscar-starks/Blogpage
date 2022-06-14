from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Info

# Create your views here.
def blogpage(request):
    posts = Info.objects.all().order_by("-timestamp")
    
    context = {
        "posts": posts
    }
    return render(request, "post\\blog3.html", context)

def detailview(request, ID):
    post = Info.objects.get(id = ID)

    context = {
        "info":post
    }
    return render(request, "post\single.html", context)

def createpost(request):

    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        authors = request.user
        post = Info(post_title=title, post_content=content, author = authors)
        post.save()

        return redirect("post:blogpage")
    return render(request, "post\create_post.html")