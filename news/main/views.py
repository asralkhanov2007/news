from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView,ListView,DetailView
from .models import *	
from .forms import AddCommentForm
# Create your views here.

class HomePageView(ListView):
	model = Post
	paginate_by = 6
	template_name = 'index.html'
	context_object_name = 'posts'


def tagDetailPage(request, tag_slug):
	tag = get_object_or_404(Tags, slug=tag_slug)
	print(tag)
	post = Post.objects.filter(tag=tag)
	return  render(request, 'tag.html', {'posts':post})


class CategoryDetailView(DetailView):
	model = Category
	slug_field = 'slug'
	template_name = 'category.html'


def postDetailPage(request, post_slug):
	post = Post.objects.get(slug=post_slug)
	if request.method == 'POST':
		form = AddCommentForm(request.POST)
		if form.is_valid():
			f = form.save(commit=False)
			f.post = post
			f.save()
	else:
		form = AddCommentForm()
	post.views += 1
	post.save()
	context = {
		'post':post,
		'form':form,
	}
	return render(request, 'single.html', context)

def entry_not_found(request, exception=None):
    return render(request, '404.html')
