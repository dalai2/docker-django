# Models
from posts.models import Post
from django.views.generic import TemplateView
# class HomeView(TemplateView):

# class PostsFeedView(LoginRequiredMixin, ListView):
#     """ Return all published posts. """

#     template_name = 'posts/feed.html'
#     model = Post
#     ordering = ('-created',)
#     paginate_by = 2
#     context_object_name = 'posts'


# class PostsDetailView(LoginRequiredMixin, DetailView):
#     """Return detail of individual posts """
#     template_name = 'posts/detail.html'
#     slug_field = 'id'
#     slug_url_kwarg = 'post_id'
#     queryset = Post.objects.all()

