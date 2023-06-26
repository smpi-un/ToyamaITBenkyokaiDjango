from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .forms import BookForm


def index(request):
    try:
        # Get the first user
        user = User.objects.first()
        if user is None:
            return render(request, 'error.html', {"message": "No users found in the database."})

        # Get the first book of the user
        book = Book.objects.filter(user=user).first()
        if book is None:
            return render(request, 'error.html', {"message": f"No books found for the user: {user.username}"})

        # Pass the book object to the template
        return render(request, 'index.html', {'book': book})

    except ObjectDoesNotExist:
        return render(request, 'error.html', {"message": "Data not found."})


@login_required
def book_list(request):
    # Get all books for the current user
    books = Book.objects.filter(user=request.user)

    # Render the template with the books
    return render(request, 'book_list.html', {'books': books})


@login_required
def book_detail(request, book_id):
    # Get the book with the given ID
    book = get_object_or_404(Book, id=book_id)

    # Check if the book belongs to the current user
    if book.user != request.user:
        raise PermissionDenied

    # Render the template with the book
    return render(request, 'book_detail.html', {'book': book})

@login_required
def book_add(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            return redirect('book_detail', book_id=book.id)
    else:
        form = BookForm()
    return render(request, 'book_add.html', {'form': form})
