from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from blog.forms import CommentForm
from django.shortcuts import redirect
# Create your views here.

from django.shortcuts import render, get_object_or_404

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

# details of post made
def post_detail(request, slug):
    # make sure post exists for which we are submitting the comment
    post = get_object_or_404(Post, slug=slug)
    
    # check the user is logged in
    if request.user.is_active:
      
      # check if it is POST request. User is submitting a comment
      if request.method=="POST":
        comment_form=CommentForm(request.POST)
        
        # check if Post request contains all field with proper format  
        if comment_form.is_valid():

          comment=comment_form.save(commit=False)
          # add post and user to comment 
          comment.content_object=post
          comment.creator=request.user
          comment.save()

      
      # if not post request, make an empty form  
      else:
        comment_form=CommentForm()

    else:
      comment_form=None
  
    return render(request, "blog/post-detail.html", {"post": post,"comment_form":comment_form})