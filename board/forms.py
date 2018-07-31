from django import forms
from board.models import Board


class BoardForm(forms.ModelForm):
    title = forms.CharField(label='公告標題', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='公告內容', widget=forms.Textarea(attrs={'class': 'form-control'}))
    # we don’t want to call it.
    # We just want a reference to the class that it belongs to, forms.Textarea not forms.Textarea()

    class Meta:
        model = Board
        fields = ['title', 'content']
