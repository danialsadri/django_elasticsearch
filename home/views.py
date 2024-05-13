from django.shortcuts import render, get_object_or_404
from django.views import View
from .documents import BookDocument
from .forms import BookForm
from .models import Book


class HomeView(View):
    def get(self, request):
        form = BookForm()
        results = None
        if request.GET.get('search'):
            results = BookDocument.search().query('match', name=request.GET.get('search'))
        return render(request, 'home/home.html', {'form': form, 'results': results})


class BookDetailView(View):
    def get(self, request, book_id, book_slug):
        book = get_object_or_404(Book, id=book_id, slug=book_slug)
        return render(request, 'home/book_detail.html', {'book': book})
