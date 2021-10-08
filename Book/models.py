from django.db import models
from django.db.models.fields import IntegerField
from django.db.models.manager import Manager


class ActiveBookManager(models.Manager):
    def get_queryset(self):  # Book.objects.all().filter(is_deleted="N")
	    return super().get_queryset().filter(is_deleted="N")


class InActiveBookManager(models.Manager):
    def get_queryset(self):  # Book.objects.all().filter(is_deleted="N")
	    return super().get_queryset().filter(is_deleted="Y")


# id, name, qty, price, is_published, author

class Book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_published = models.BooleanField(default=False)
    published_date = models.DateField(null=True)
    is_deleted = models.CharField(max_length=1, default="N")  # 0
    active_books = ActiveBookManager()  # custom manager substitute of objects
    inactive_books = InActiveBookManager()  # custom manager substitute of objects
    objects = Manager()


    def __str__(self):
        return f"{self.__dict__}"

    class Meta:
        db_table = "book"