from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        unique_together = (('first_name', 'last_name'),)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Quote(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='quotes')
    text = models.TextField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}. {} - {}'.format(self.id, self.text, self.author)
