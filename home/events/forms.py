from django import forms
from .models import Post, Category

choices = Category.objects.all().values_list('cat_name','cat_name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','author','category','content','slug')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # 'timeStamp': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category', 'content','slug')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            # 'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            # 'timeStamp': forms.TextInput(attrs={'class': 'form-control'}),
        }