from .models import Post, Tags, Category


def view_all(request):

	context = {
		'home':Post.objects.all().order_by('?')[:3],
		'categories':Category.objects.all(),
		'tags':Tags.objects.all(),
		'footer_category':Category.objects.all()[:4],
		'footer_tags':Tags.objects.all()[:4],
		'tops':Post.objects.all().order_by('-views')[:6],
		'all_post':Post.objects.all().order_by('?')[:8]
	}

	return context