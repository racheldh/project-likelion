from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

def home(request):
    blogs = Blog.objects
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html', {'blogs': blogs, 'posts': posts})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog_detail})

def new(request):#new.html을 띄워주는 함수
    return render(request, 'blog/new.html')

def create(request):#입력 받은 내용을 데이터베이스에 넣어 주는 함수
    blog = Blog() #Blog 함수에서 blog 객체 생성
    blog.title = request.GET['title'] #변수에 입력된 내용 넣어주기
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.blogger = request.user
    blog.save() #객체 내용을 저장하는 것. 지우는 것은 객체.delete()
    return redirect('/blog/'+str(blog.id)) #id는 int이므로 url은 항상 string이기 때문에 형 변화.

