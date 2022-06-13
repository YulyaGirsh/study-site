from django import forms
from .models import Categories


class ReviewForm(forms.Form):
    title = forms.CharField(max_length=150, label='Краткое описание', widget=forms.TextInput(
        attrs={"class": "form-control"}))
    content = forms.CharField(label='Текст отзыва', widget=forms.Textarea(attrs={
        "class": "form-control",
        "rows": 5,
    }))
    is_published = forms.BooleanField(label='Опубликовать')
    category = forms.ModelChoiceField(queryset=Categories.objects.all(),
                                      label='Выберите, в каком направлении вы совершали поездку', required=False, empty_label='Выберите категорию',
                                      widget=forms.Select(attrs={"class": "form-control"}))
