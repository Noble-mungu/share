from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category, Location
# Create your views here.

def home(request):
    posts = Post.get_posts()
    return render(request,'home.html', {"posts": posts})

def open_location(request,id):    
    posts = Post.get_location_post(id)
    return render(request,'location.html', {"posts": posts})


def search_results(request):

    if 'post' in request.GET and request.GET["post"]:
        search_term = request.GET.get("post")
        searched_posts = Post.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "posts": searched_posts})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message": message})