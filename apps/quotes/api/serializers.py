from rest_framework import serializers

from ..models import Author, Quote


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'quotes']

    def validate_first_name(self, fname):
        print('fname: ' + fname)
        return fname

    def validate_last_name(self, lname):
        print('lname: ' + lname)
        return lname


class QuoteSerializer(serializers.ModelSerializer):
    # author = AuthorSerializer()

    class Meta:
        model = Quote
        fields = ['id', 'text', 'created_at', 'updated_at']

    def validate_text(self, text):
        print('text: ' + text)
        return text
