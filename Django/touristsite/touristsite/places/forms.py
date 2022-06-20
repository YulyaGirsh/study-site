from django import forms
from .models import Categories, Review
import re
from django.core.exceptions import ValidationError


# class ReviewForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Краткое описание', widget=forms.TextInput(
#         attrs={"class": "form-control"}))
#     content = forms.CharField(label='Текст отзыва', widget=forms.Textarea(attrs={
#         "class": "form-control",
#         "rows": 5,
#     }))
#     is_published = forms.BooleanField(label='Опубликовать')
#     category = forms.ModelChoiceField(queryset=Categories.objects.all(),
#                                       label='Выберите, в каком направлении вы совершали поездку', required=False, empty_label='Выберите категорию',
#                                       widget=forms.Select(attrs={"class": "form-control"}))


class ReviewForm2(forms.ModelForm):
    class Meta:
        model = Review
        # fields = '__all__'
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
