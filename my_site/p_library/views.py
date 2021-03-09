from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.template import loader
from django.shortcuts import redirect
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from p_library.models import Book, Friend, BookReader
from p_library.forms import FriendForm, BookSendForm


# Create your views here.

def books_json(request):
    books = Book.objects.all()
    qs_json = serializers.serialize('json', books)
    return HttpResponse(qs_json, content_type='application/json')

def books_list(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    biblio_data = {
        "title": "мою библиотеку",
        "books": books,
        "loop": range(1, 101),
    }
    return HttpResponse(template.render(biblio_data, request))


def book_increment(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            book.copy_count += 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def book_decrement(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect('/index/')
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect('/index/')
            if book.copy_count < 1:
                book.copy_count = 0
            else:
                book.copy_count -= 1
            book.save()
        return redirect('/index/')
    else:
        return redirect('/index/')


def publisher_list(request):
    return render(request, 'publishers.html', {
        'publishers': Book.objects.select_related('publisher').order_by('publisher'),
    },)

class FriendAdd(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'friend_add.html'

class FriendList(ListView):
    model = Friend
    template_name = 'friends.html'

class FriendDetail(DetailView):
    model = Friend
    template_name = 'friend_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["sent_books"] = self.object.bookreader_set.all()
        return context
    

class BookSend(CreateView):
    model = BookReader
    form_class = BookSendForm
    success_url = reverse_lazy('p_library:friend_list')
    template_name = 'book_send.html'
    
