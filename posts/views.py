# Models
from posts.models import Post
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name='home.html'
# class PostsFeedView( ListView):
#     """ Return all published posts. """

#     template_name = 'posts/feed.html'
#     model = Post
#     ordering = ('-created',)
#     paginate_by = 2
#     context_object_name = 'posts'


