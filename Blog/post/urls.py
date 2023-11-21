from django.urls import path
from . import views


app_name = "post"

urlpatterns = [ 
     path("", views.display_blog_view, name="display_blog_view"),
    path("add/", views.add_blog_view, name="add_blog_view")

]