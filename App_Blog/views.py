from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView, ListView, DetailView, View, TemplateView, DeleteView
from App_Blog.models import Blog,Likes
import uuid
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse
from App_Blog.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# def blog_list(request):
#     return render(request, 'App_Blog/blog_list.html', {})


class CreateBlogView(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = "App_Blog/create_blog.html"
    fields=('blog_title','blog_content','blog_image')

    def form_valid(self,form):
        form_obj=form.save(commit=False)
        form_obj.author=self.request.user
        title=form_obj.blog_title
        form_obj.slug=title.replace(" ","-")+"-"+str(uuid.uuid4())
        form_obj.save()
        return HttpResponseRedirect(reverse_lazy('index'))

class BlogListView(ListView):
    context_object_name="blog_list"
    model=Blog 
    template_name="App_Blog/blog_list.html"
    fields=('blog_title','blog_image')

@login_required
def BlogDetailsView(request,slug):
    blog=Blog.objects.get(slug=slug)
    comment_form=CommentForm()
    current_user=request.user
    already_liked=Likes.objects.filter(blog=blog,user=current_user)
    if already_liked:
        liked=True 
    else:
        liked=False
    if request.method=="POST":
        comment_form=CommentForm(request.POST)
        frm_obj=comment_form.save(commit=False)
        frm_obj.blog=blog 
        frm_obj.user=request.user
        print(frm_obj.blog)
        frm_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':slug} ))
        
    dict={"blog":blog,"comment_form":comment_form,"liked":liked}
    return render(request, "App_Blog/blog_details.html", context=dict)
    
@login_required
def liked(request,pk):
    current_user=request.user 
    blog=Blog.objects.get(pk=pk)
    already_liked=Likes.objects.filter(blog=blog,user=current_user)
    if not already_liked:
        likes=Likes(blog=blog,user=current_user)
        liked=True 
        likes.save()
        return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':blog.slug} ))

@login_required 
def unliked(request,pk ):
    current_user=request.user 
    blog=Blog.objects.get(pk=pk)
    already_liked=Likes.objects.filter(blog=blog,user=current_user)
    if already_liked:
        already_liked.delete()
        return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'slug':blog.slug} ))


class MyBlog(LoginRequiredMixin,ListView):
    context_object_name="blog"
    model=Blog 
    template_name="App_Blog/my_blog.html"


class EditBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = "App_Blog/edit_blog.html"
    fields = ('blog_title', 'blog_content', 'blog_image')
    def get_success_url(self, **kwargs):
        return reverse_lazy('App_Blog:blog_details', kwargs={'slug':self.object.slug})

