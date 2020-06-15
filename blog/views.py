from django.shortcuts import render

def post_list(request):                                             # Create your views here.
    return render(request, 'blog/post_list.html', {})
