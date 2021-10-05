from django.db import models
from django.urls import reverse
# ForeignKey = birga kop ulash
# OneToOneField = birga bir ulash
# ManyToManyField = Kopga kopga ulash

class Category(models.Model):
	name = models.CharField('Nomi:', max_length=100)
	slug = models.SlugField('*', max_length=100, unique=True)

	def __str__(self):
		return f"{self.name}"

		def get_absolute_url(self):
			return reverse('main:category_detail', kwargs={'category_slug':self.slug})

	class Meta:
		verbose_name = 'Kategoriya'
		verbose_name_plural = 'Kategoriyalar'

class Tags(models.Model):
	name = models.CharField('Nomi:', max_length=100)
	slug = models.SlugField('*', max_length=100, unique=True)

	def __str__(self):
		return f"{self.name}"

	def get_absolute_url(self):
		return reverse('main:tag_detail', kwargs={'tag_slug':self.slug})

	class Meta:
		verbose_name = 'Teg'
		verbose_name_plural = 'Teglar'


class Post(models.Model):
	title = models.CharField('Nomi', max_length=300)
	slug = models.SlugField('*', max_length=100, unique=True)
	author = models.CharField('Aftor', max_length=80)
	image = models.ImageField('Rasmi', upload_to='posters/')
	body = models.TextField('Body')
	views = models.PositiveIntegerField('Korildi', default=0)
	published = models.DateTimeField(auto_now_add=True)
	category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='posts')
	tag = models.ManyToManyField(Tags,related_name='products')

	def __str__(self):
		return f"{self.title}"

	def get_absolute_url(self):
		return reverse('main:post_detail', kwargs={'post_slug':self.slug})

	class Meta:
		verbose_name = 'Maqola'
		verbose_name_plural = 'Maqolalar'


class Comment(models.Model):
	post = models.ForeignKey(Post,
	on_delete=models.CASCADE,
	related_name='comments')
	date = models.DateTimeField('Bildirilgan sana',
		auto_now_add=True,
		null=True)
	name = models.CharField('Ismingiz', max_length=50)
	email = models.EmailField('Email')
	subject = models.CharField('Mavzu', max_length=150)
	comment = models.TextField('Xabar matni')

	def __str__(self):
		return f"{self.name}"

	class Meta:
		verbose_name = 'Muhokama'
		verbose_name_plural = 'Muhokamalar'