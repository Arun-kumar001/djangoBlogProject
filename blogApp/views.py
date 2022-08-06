from django.shortcuts import render
from django.http import HttpResponse
from blogApp.models import Post, Contact, Comment
# Create your views here.

def home(request):
    getPost1 = Post.objects.all()
    comnt = Comment.objects.all()
    getPost = Post.objects.get(post_title='Django')
    getAbout = getPost.post_about
    getContent = getPost.post_content
    getDate = getPost.post_pubDate
    getAuthor = getPost.post_authorName
    perms = {'title':getPost, 'about':getAbout, 'content':getContent, 'date':getDate, 'author':getAuthor,'getPost0':getPost1, 'cmt':comnt }

    if request.method=='POST':
        post_name = request.POST['name']
        post_email = request.POST['email']
        post_text = request.POST['textarea']
        print(post_name, post_email, post_text)
        comt = Comment(name=post_name, email=post_email, comm=post_text)
        comt.save()
        perm ={
            'post':'Comment Posted'
        }
    return render(request, 'home.html',perms)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        content = request.POST['textarea']
        print(name, email, content)
        cont = Contact(name=name, email=email, comment=content)
        cont.save()
        perm={'post':'Your Post has been Sent'}
        return render(request, 'contact.html', perm)
    else:
        return render(request, 'contact.html')

def allpost(request):
    getPost1 = Post.objects.all()
    perm ={
        'post0':getPost1
    }
    return render(request, 'allpost.html',perm )

def bash(request):
    return render(request, 'bash.html')