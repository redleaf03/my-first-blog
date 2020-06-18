from django.shortcuts import render
from django.utils import timezone                                   # timezone 모듈을 불러와야하니
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def post_list(request):                                             # Create your views here.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')      # posts 퀴리셋의 이름
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
                                                                    # 'blog/post_list.html' 템플릿
                                                                    # {} - 이곳에 템플릿을 사용하기 위해 매개변수를 추가할 거에요.
                                                                    # (이 매개변수를'posts'라고 할거에요){'posts': posts}이렇게 작성할거에요.
                                                                    #  :이전에 문자열이 와야하고, 작은 따옴표''
