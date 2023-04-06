from django.shortcuts import render,get_object_or_404,redirect
from .models import Blog
from .forms import BlogForm

def home(request):
    blogs = Blog.objects.all()
    return render(request,'home.html',{'blogs':blogs})

def detail(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request,'detail.html',{'blog':blog})

def new(request):
    return render(request,'new.html')
    


def create(request):
    form = BlogForm(request.POST)
    if form.is_valid():
        new_blog=form.save(commit=False)
        new_blog.save()
        print(form)
        return redirect('detail',new_blog.id)
    
    return render(request, 'new.html')



def edit(request, blog_id):
    edit_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'edit.html', {'edit_blog':edit_blog})


def update(request, blog_id):
    old_blog = get_object_or_404(Blog, pk=blog_id)
    form = BlogForm(request.POST, instance=old_blog)
    if form.is_valid():
        new_blog = form.save(commit=False)
        new_blog.save()
        return redirect('detail', old_blog.id)
    return render(request, "new.html")

def delete(request, blog_id):
    delete_blog = get_object_or_404(Blog, pk=blog_id)
    delete_blog.delete()
    return redirect('home')


def search(request):
    searched = request.POST.get('searched')
    print(searched)
    ss = request.POST['searched']
    print(ss)
    search_result = Blog.objects.filter(title__contains=searched)
    print(search_result)
    print(len(search_result))
    if len(search_result) != 0:
        return render(request, 'search.html', {'searched':searched, 'search_result':search_result})
    else:
         return render(request, 'search.html', {'searched':searched})