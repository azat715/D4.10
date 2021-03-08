from django.db import models

# Create your models here.


class Author(models.Model):
    full_name = models.TextField()
    birth_year = models.SmallIntegerField()
    country = models.CharField(max_length=2)

    def __repr__(self):
        return 'Author({self.full_name}, {self.birth_year}, {self.country})'.format(self=self)

    def __str__(self):
        return str(self.full_name)


class Publisher(models.Model):
    name = models.TextField()
    description = models.TextField()

    def __repr__(self):
        return 'Publisher({self.name}, {self.description},)'.format(self=self)

    def __str__(self):
        return str(self.name)

class Friend(models.Model):
    name = models.TextField()

    def __repr__(self):
        return 'FriendBookReader({self.name},)'.format(self=self)

    def __str__(self):
        return str(self.name)


class Book(models.Model):
    ISBN = models.CharField(max_length=13)
    title = models.TextField()
    description = models.TextField()
    year_release = models.SmallIntegerField()
    price = models.FloatField()
    copy_count = models.PositiveSmallIntegerField(default=1)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    book_reader = models.ManyToManyField(Friend, through='BookReader')

    def __repr__(self):
        return 'Book({self.ISBN}, {self.title}, {self.description}, {self.year_release}, {self.price}, {self.copy_count}, {self.author})'.format(self=self)

    def __str__(self):
        return str(self.title)

class BookReader(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)
    date_send = models.DateField()
    copy_count_send = models.PositiveSmallIntegerField(default=1)