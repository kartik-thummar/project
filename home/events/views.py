from django.shortcuts import render,HttpResponse
from events.models import Post, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def events(request):
#     allPosts = Post.objects.all()
#     context = {'allPosts': allPosts}
#     return render(request, 'events.html', context)

class events(ListView):
    model = Post
    template_name = 'events.html'
    cats = Category.objects.all()
    ordering = ['-sno']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(events, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

# def addPost(request):
#     return render(request, 'blog/addPost.html')

class addPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/addPost.html'
    # fields = '__all__'
    # fields = ('title', 'content')

class updatePost(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'blog/updatePost.html'
    # fields = ['title','category','content','slug','timeStamp']

class deletePost(DeleteView):
    model = Post
    template_name = 'blog/deletePost.html'
    success_url = reverse_lazy('events')

class addCategory(CreateView):
    model = Category
    template_name = 'blog/addCategory.html'
    fields = '__all__'

def categoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'blog/categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

def categoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'blog/category_list.html', {'cat_menu_list':cat_menu_list})

def eventPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    if post:
        context = {'post':post}
        return render(request, 'eventsPost.html', context)
    return HttpResponse('Specified Content not found!')


# def category_list(request):
#     categories = Category.objects.all() 

#     return render (request, 'blog/category_list.html', {'categories': categories}) 

# def category_detail(request, pk):
#     category = get_object_or_404(Category, pk=pk)

#     return render(request, 'blog/category_detail.html', {'category': category}) 

def about(request):
    return render(request, 'about.html')

# class about(ListView):
    # template_name = 'about.html'

# def search(request):
#     query = request.GET['query']
#     allPosts = Post.objects.filter(title__icontains=query)
#     params = {'allPosts': allPosts }
#     return render(request, 'search.html', params)

