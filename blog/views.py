from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from .models import Blog
from django.urls import reverse_lazy
from django.urls import reverse


class BlogCreateView(CreateView):
    model = Blog
    fields = ['heading', 'content', 'preview']
    context_object_name = 'blog'
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog:blog_list')


class BlogListView(ListView):
    model = Blog
    context_object_name = 'blogs'
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        self.object_list = super().get_queryset().filter(is_published=True)
        return self.object_list


class BlogDetailView(DetailView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.quantity_views += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ['heading', 'content', 'preview']
    context_object_name = 'blog'
    template_name = 'blog/blog_form.html'

    def get_success_url(self, **kwargs):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    context_object_name = 'blog'
    template_name = 'blog/blog_delete.html'
    success_url = reverse_lazy('blog:blog_list')