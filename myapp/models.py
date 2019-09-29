from django.db import models

# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ContactMessage(TimeStampMixin):
    name = models.CharField(max_length=100, editable=False)
    email = models.EmailField(editable=False)
    message = models.TextField(max_length=2047, editable=False)

    def __str__(self):
        return self.name
