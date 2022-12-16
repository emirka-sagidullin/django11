from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from .forms import Section
from .models import Post, Category, Autors, Publisher

# Create your views here.

def posts(request):
    categoryCreate()
    autorsCreate()
    publishersCreate()
    category = Category.objects.all()
    section = Section()
    autors = Autors.objects.all()
    publishers = Publisher.objects.all()
    return render(request, 'posts.html', {'form': section, 'categories': category, 'autors': autors, 'publishers': publishers})

def allPosts(request):
    if request.POST:
        post = Post()
        post.heading = request.POST.get('Heading')
        post.url = request.POST.get('URL')
        post.content = request.POST.get('Content')
        post.publication = request.POST.get('Publication')
        post.category_id = request.POST.get('Category')
        post.autor_id = request.POST.get('Autor')
        post.publisher_id = request.POST.get('Publisher')
        post.save()
    all = Post.objects.all()
    return render(request, 'allPosts.html', {'posts': all})


def categoryCreate():
    if Category.objects.all().count() == 0:
        Category.objects.create(name = 'Javapon')
        Category.objects.create(name = 'Pythonpon')
        Category.objects.create(name = 'djangopon')

def autorsCreate():
    if Autors.objects.all().count() == 0:
        Autors.objects.create(name = 'DjangoPon')
        Autors.objects.create(name = 'JavaPon')
        Autors.objects.create(name = 'FlaskoPon')

def publishersCreate():
    if Publisher.objects.all().count() == 0:
        Publisher.objects.create(name = 'Alabuga')
        Publisher.objects.create(name = 'Elabuga')

def edit(request, id):
    try:
        post = Post.objects.get(id=id)

        if request.method == 'POST':
            post.heading = request.POST.get('heading')
            post.url = request.POST.get('url')
            post.autor_id = request.POST.get('autor')
            post.category_id = request.POST.get('category')
            post.publisher_id = request.POST.get('publisher')
            post.save()
            return HttpResponseRedirect('/posts/allPosts')
        else:
            autor = Autors.objects.all()
            categories = Category.objects.all()
            publishers = Publisher.objects.all()
            return render(request, 'edit.html', {'post':  post, 'autors':  autor, 'categories': categories, 'publishers': publishers})
    except post.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')

def delete(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return HttpResponseRedirect('/posts/allPosts')
    except Post.DoesNotExist:
        return HttpResponseNotFound('<h2>Product not found</h2>')