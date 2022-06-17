from django.urls import path
from . import views 

app_name='App_Blog'

urlpatterns=[
    path('',views.BlogListView.as_view(),name='blog_list'),
    path('create/',views.CreateBlogView.as_view(),name='create'),
    path('details/<slug>',views.BlogDetailsView,name='blog_details'),
    path('like/<pk>',views.liked,name='like'),
    path('unlike/<pk>',views.unliked,name='unlike'),
    path('myblog/',views.MyBlog.as_view(),name='myblog'),
    path('edit_blog/<pk>',views.EditBlog.as_view(),name='editblog'),
]
