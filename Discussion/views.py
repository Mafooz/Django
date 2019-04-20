from django.shortcuts import render,get_object_or_404,redirect
from .forms import PostForm,CommentForm
from .models import Post, Comment 
def home(request):
	posts=Post.objects.all()
	return render(request,'Discussion/home.html',{'posts':posts})

def post_details(request,pk):
	current_post=get_object_or_404(Post,pk=pk)
	cts=Comment.objects.filter(cpost=current_post)
	form = CommentForm(request.POST)
	if form.is_valid():
		print("valid")
		comment = form.save(commit=False)
		cbody = form.cleaned_data['cbody']
		comment.ctor=request.user
		comment.cpost=current_post
		comment.save()
		print("abcd")
		print(comment)
		return redirect('Discussion:post_details',pk=pk)
	print(cts)
	return render (request,'Discussion/details.html',{'current_post': current_post,
														'cts' : cts,
														'forms': form})

def Post_it(request):
	form = PostForm(request.POST)
	if form.is_valid():
		print("valid")
		post = form.save(commit=False)
		title = form.cleaned_data['title']
		body = form.cleaned_data['body']
		post.Author=request.user
		post.save()
		return redirect('Discussion:home')
	return render(request, 'Discussion/Post_it.html',{'form':form})

