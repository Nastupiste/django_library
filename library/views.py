from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import BookForm
from .models import Book
# Create your views here.


class BookList(View):

    books = Book.objects.all()

    def updateBookList(self):
        self.books = Book.objects.all()
        return self.books

    def get(self, request):
        return render(request, 'book_list.html', {'books': self.updateBookList()})


class BookAdd(View):

    def get(self, request):
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')
        return render(request, 'add_book.html', {'form': form})


class BookDetails(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        return render(request, 'book_details.html', {'book': book})


class BookEdit(View):

    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(instance=book)
        return render(request, 'book_edit.html', {'book': book, 'form': form})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            book = form.save(commit=False)
            form.save()
            return redirect('book_details', pk=book.pk)
        return render(request, 'book_edit.html', {'book': book, 'form': form})
