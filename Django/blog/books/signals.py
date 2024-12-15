from django.db.models.signals import post_save
from django.dispatch import receiver
from books.models import Book
from random import randint

@receiver(post_save, sender=Book)
def after_save(sender, instance, **kwargs):
    hex_code = hex(randint(0, 255))
    print(f"Book created: {hex_code}")