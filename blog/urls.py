from django.urls import path
from . import views


app_name = 'blog'

urlpatterns = [
    path("blog_form/", views.BlogCreateView.as_view(), name="blog_create"),
    path("blog_list/", views.BlogListView.as_view(), name="blog_list"),
    path("blog_detail/<int:pk>/", views.BlogDetailView.as_view(), name="blog_detail"),
    path("blog_form/<int:pk>/", views.BlogUpdateView.as_view(), name="blog_update"),
    path("blog_delete/<int:pk>/", views.BlogDeleteView.as_view(), name="blog_delete"),
]
