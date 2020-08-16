from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #all class base view
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin    #1st for check suer is login or not and
from .models import Post                                                          # 2nd used to check curr_user is owner of post
# Create your views here.
# posts = [
#     {
#         'topic' : 'first blog',
#         'author' : 'sheru khan',
#         'date' : '21-04-2020',
#         'content' : 'it is first blog.'
#
#     }
# ]

def home(request):
    context = {
        'title' : 'home',
        'posts' : Post.objects.all()
    }
    return render(request,'home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date']              #listing of post by data in new to old
    paginate_by = 2                   #how many post in one page

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 2


    '''
    if we go to particular user , if he is available them show his/her all post or show error that user dont exist
    '''
    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return Post.objects.filter(author = user).order_by('-date')

class PostDetailView(DetailView):
    # other work is done by auth_view in url.py but follow <app_name>/<model>_detail.html
    model = Post


# user must be login to create post that why 1st argument and by-default template name <app>/<model>_form
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['topic','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#for update , user must be login and owner of post so first 2 argument
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['topic','content']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):            # to check is user is owner of post or not
        current_post = self.get_object()
        if self.request.user == current_post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'             #after delete where to go
    def test_func(self):           # to check user is owner or not of the post
        current_post = self.get_object()
        if self.request.user == current_post.author:
            return True
        return False


def about(request):
    context = {
        'title': 'about',

    }
    return render(request,'blog/about.html',context)