from django.utils import timezone
from rest_framework import serializers
from .models import Book, Author, Publisher
from datetime import datetime, timedelta


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    publisher = PublisherSerializer()

    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, attrs):
        description = attrs.get('description')
        published_date = attrs.get('published_date')
        price = attrs.get('price')
        if attrs.get('title') and len(attrs['title']) > 100:
            raise serializers.ValidationError('Title cannot exceed 100 characters')
        
        if description and len(description.split()) <10:
            raise serializers.ValidationError('Description must have at least 10 words')
        
        if published_date:
            one_month_ago = datetime.now().date() - timedelta(days=30)
            if published_date > one_month_ago:
                raise serializers.ValidationError('Published date must be at least 1 month old')
            
        if price is not None and (price < 100 or price > 10000):
                raise serializers.ValidationError('Price must be between 100 to 10000.')
        return attrs
    
    def create(self, validated_data):
        author = validated_data.pop('author')
        author_serializer = AuthorSerializer(data= author)
        if author_serializer.is_valid():
            author_instance = author_serializer.save()
            validated_data['author'] = author_instance
        
        publisher = validated_data.pop('publisher')
        publisher_serializer = PublisherSerializer(data= publisher)
        if publisher_serializer.is_valid():
            publisher_instance = publisher_serializer.save()
            validated_data['publisher'] = publisher_instance
         

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        validated_data['updated_at'] = timezone.now()
        
        return super().update(instance, validated_data)


        


        
