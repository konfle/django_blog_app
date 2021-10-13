from django.shortcuts import render

posts = [
    {
        'author': "konfle",
        'title': "Blog Post 1",
        'content': " Blog post content",
        "date_posted": "13.10.2021"
    },
    {
        'author': "wafle",
        'title': "Blog Post 2",
        'content': " Blog post content 2",
        "date_posted": "14.10.2021"
    }
]


def home(request):
    context = {
        "posts": posts,
        "title": "Home"
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {"title": "About"})
