from django.urls import path
from .import views

app_name = 'main'

urlpatterns = [
	path('',views.HomePageView.as_view(), name='home'),
	path('post-detail/<slug:post_slug>',views.postDetailPage, name='post_detail'),
    path('category/detail/<slug>',views.CategoryDetailView.as_view(),name='category_detail'),
    path('post/<slug:tag_slug>',views.tagDetailPage, name='tag_detail'),
]