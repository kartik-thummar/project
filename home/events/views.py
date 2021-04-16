from django.shortcuts import render,HttpResponse
from events.models import Post
from django.views.generic import ListView, DetailView

def events(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request, 'events.html', context)

# class events(ListView):
#     model = Post
#     template_name = 'events.html'

def eventPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request, 'eventsPost.html', context)

# def category_list(request):
#     categories = Category.objects.all() 

#     return render (request, 'blog/category_list.html', {'categories': categories}) 

# def category_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)

#     return render(request, 'blog/category_detail.html', {'category': category}) 


def about(request):
    return render(request, 'about.html')

# def search(request):
#     query = request.GET['query']
#     allPosts = Post.objects.filter(title__icontains=query)
#     params = {'allPosts': allPosts }
#     return render(request, 'search.html', params)