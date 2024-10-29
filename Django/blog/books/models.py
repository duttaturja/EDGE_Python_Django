from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    birthdate = models.DateField()

class Book(models.Model):
    title =  models.CharField(max_length=50)
    publication_date = models.DateField()
    description = models.TextField()
    price = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(null= True, blank= True)

    class Meta:
        permissions = [
            ("can_add_books", "Can add new books"),
        ]

    def __str__(self):
        return self.title
    
    @classmethod
    def calculate_avg_price(cls):
        return Book.objects.aggregate(models.Avg('price'))['price__avg']
        

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    published_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return self.name