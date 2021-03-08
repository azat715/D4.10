from django import forms
from p_library.models import Book, Friend, BookReader

class FriendForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput) 

    class Meta:
        model = Friend
        fields = '__all__'

class BookSendForm(forms.ModelForm):  

    class Meta:
        model = BookReader
        fields = '__all__'
        # fields = ['date_send', 'copy_count_send',]

    # book = forms.ModelChoiceField(queryset=Book.objects.all())
    # freind = forms.ModelChoiceField(queryset=Friend.objects.all())
