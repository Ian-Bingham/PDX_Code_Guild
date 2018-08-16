from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect, HttpResponse
from .forms import BookForm
from .models import Book, Author
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    book_list = []
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            pub_date = form.cleaned_data['pub_date']
            author_name = form.cleaned_data['author']
            if author_name:
                author = Author.objects.get(name=author_name)

            if not title and not pub_date and not author_name:
                book_list = Book.objects.all()
            elif title and pub_date and author_name:
                book_list = Book.objects.all().filter(title__icontains=title, pub_date=pub_date, author=author)
            elif title and pub_date:
                book_list = Book.objects.all().filter(title__icontains=title, pub_date=pub_date)
            elif title and author_name:
                book_list = Book.objects.all().filter(title__icontains=title, author=author)
            elif pub_date and author_name:
                book_list = Book.objects.all().filter(pub_date=pub_date, author=author)
            elif title:
                book_list = Book.objects.all().filter(title__icontains=title)
            elif pub_date:
                book_list = Book.objects.all().filter(pub_date=pub_date)
            elif author_name:
                book_list = Book.objects.all().filter(author=author)

            form = BookForm()  # blank form
        # if the form is invalid, we just send it back to the template
    else:
        form = BookForm()
    return render(request, 'library_app/index.html', {'form': form, 'book_list': book_list})


@login_required
def checkin(request, book_id):
    book = Book.objects.get(id=book_id)
    book.checked_out = False
    book.save()
    return HttpResponse(f'Checked in book: {book.title}')


@login_required
def checkout(request, book_id):
    book = Book.objects.get(id=book_id)
    book.checked_out = True
    book.save()
    return HttpResponse(f'Checked out book: {book.title}')
