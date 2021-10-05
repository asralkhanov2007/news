from django import forms
from .models import Comment

class AddCommentForm(forms.ModelForm):
	# Add Comment 
	
	class Meta:
		model = Comment
		fields = '__all__' # Hamma maydonini olish
		exclude = ['post','subject'] # qaysi maydonlarni korsatmaslik
		# fields = ['name', 'email','subject', 'comment'] 
		widgets = {
		'comment': forms.TextInput(attrs={'class': 'form-control'}), # or whatever class you want to apply
		# and so on
		}