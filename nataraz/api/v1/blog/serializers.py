from rest_framework import serializers
from .models import Blog, Category, Paragraph

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ['id', 'title', 'content']

class BlogSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    paragraphs = ParagraphSerializer(many=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'cover', 'author', 'categories', 'paragraphs']
