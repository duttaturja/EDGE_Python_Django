# from django
from django.views import View
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic import ListView, FormView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

#from rest_framework
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework import status, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# from books
from books.models import Book, Author, Publisher
from books.forms import ContactForm, BookForm
from books.serializers import BookSerializer, AuthorSerializer, PublisherSerializer


#classes
class MyView(View):
    def get(self, request):
        return HttpResponse("Welcome to Django from class")
    
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_success')

    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)
    

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book                                # Model name to add new book details   
    form_class = BookForm                       # Form class to validate the form
    template_name = 'books/book_form.html'      # Template name to render the form
    success_url = reverse_lazy('book_list')     # Success url to redirect after form submission
    permission_required = 'books.can_add_books' # Permission required to add new book details
    
    def handle_no_permission(self):
        """
            To add permission to user:
            from django.contrib.auth.models import Permission, User
            user = User.objects.get(username="duttaturja")
            permission = Permission.objects.get(codename="can_add_books")
            user.user_permissions.add(permission)
        """
        return HttpResponseForbidden("You do not have permission to add a book.")
    # Show http response after form validation
    def form_valid(self, form) -> HttpResponse:
        return super().form_valid(form)
    

#Rest_Frameworks API's
class APIBook(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        print(request.user)
        books = Book.objects.all()
        serializer = BookSerializer(books, many = True)
        data = serializer.data
        return Response(data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
# API views for Author details
class APIAuthor(APIView):
    # Get method to retrieve Author data by id or all authors
    def get(self, request, pk=None):
        if pk:  # Check if primary key is given for a specific author
            try:
                author = Author.objects.get(pk=pk)  # Retrieve Author object using primary key
            except Author.DoesNotExist:
                # Return JSON response with 404 status if author not found
                return Response({"error": "Author not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = AuthorSerializer(author)  # Serialize single author object
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data with OK status
        
        # Retrieve all authors if no primary key is provided
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)  # Serialize multiple authors
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Post method to add a new author
    def post(self, request):
        serializer = AuthorSerializer(data=request.data)  # Pass new Author data to serializer
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save new author if valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

    # Patch method to partially update an author by id
    def patch(self, request, pk=None):
        try:
            author = Author.objects.get(pk=pk)  # Retrieve Author object by primary key
        except Author.DoesNotExist:
            return Response({"error": "Author not found."}, status=status.HTTP_404_NOT_FOUND)
        # Serialize with partial update for provided fields only
        serializer = AuthorSerializer(author, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save updated author data if valid
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

    # Delete method to remove an author by id
    def delete(self, request, pk=None):
        try:
            author = Author.objects.get(pk=pk)  # Retrieve Author object by primary key
        except Author.DoesNotExist:
            return Response({"error": "Author not found."}, status=status.HTTP_404_NOT_FOUND)
        author.delete()  # Delete author from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return no content response after deletion
    
# API views for Publisher details
class APIPublisher(APIView):
    # Get method to retrieve Publisher data by id or all publishers
    def get(self, request, pk=None):
        if pk:  # Check if primary key is given for a specific publisher
            try:
                publisher = Publisher.objects.get(pk=pk)  # Retrieve Publisher object by primary key
            except Publisher.DoesNotExist:
                # Return JSON response with 404 status if publisher not found
                return Response({"error": "Publisher not found."}, status=status.HTTP_404_NOT_FOUND)
            serializer = PublisherSerializer(publisher)  # Serialize single publisher object
            return Response(serializer.data, status=status.HTTP_200_OK)  # Return serialized data with OK status

        # Retrieve all publishers if no primary key is provided
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)  # Serialize multiple publishers
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Post method to add a new publisher
    def post(self, request):
        serializer = PublisherSerializer(data=request.data)  # Pass new Publisher data to serializer
        if serializer.is_valid():  # Validate the data
            serializer.save()  # Save new publisher if valid
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return created status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

    # Patch method to partially update a publisher by id
    def patch(self, request, pk=None):
        try:
            publisher = Publisher.objects.get(pk=pk)  # Retrieve Publisher object by primary key
        except Publisher.DoesNotExist:
            return Response({"error": "Publisher not found."}, status=status.HTTP_404_NOT_FOUND)
        # Serialize with partial update for provided fields only
        serializer = PublisherSerializer(publisher, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()  # Save updated publisher data if valid
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid

    # Delete method to remove a publisher by id
    def delete(self, request, pk=None):
        try:
            publisher = Publisher.objects.get(pk=pk)  # Retrieve Publisher object by primary key
        except Publisher.DoesNotExist:
            return Response({"error": "Publisher not found."}, status=status.HTTP_404_NOT_FOUND)
        publisher.delete()  # Delete publisher from the database
        return Response(status=status.HTTP_204_NO_CONTENT)  # Return no content response after deletion
    


class BookGetUpdateDelete(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    http_method_names = ('get', 'post', "put", 'delete')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
