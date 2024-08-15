import uuid
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.


class Book(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )

    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="covers/", blank=True)
    description = models.TextField(default="<Empty>")

    class Meta:
        indexes = [
            models.Index(fields=["id"], name="id_index"),
        ]
        permissions = [
            ("special_status", "Can read all books"),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", args=[str(self.id)])


class ReviewStar(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="review_star",
    )
    review_star = models.DecimalField(max_digits=6, decimal_places=2)
    review_total_Ratings = models.DecimalField(
        max_digits=20, decimal_places=0, default=0
    )

    def __float__(self):
        return self.review_star


class Review(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    review = models.CharField(max_length=255)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    review_url = models.CharField(max_length=500, default="https://www.google.com/")
    reviewer_name = models.CharField(max_length=200, default="SampleReviewer")

    def __str__(self):
        return self.review


class Genre(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="genres",
    )
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre


class ReviewSummaryOverall(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="review_summary",
    )
    review_summary = models.TextField()
    review_good = models.TextField(default="")
    review_bad = models.TextField(default="")

    def __str__(self):
        return self.review_summary


class ReviewSummaryGoodreads(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="review_goodreads",
    )
    review_goodreads = models.TextField()
    review_goodreads_star = models.DecimalField(
        max_digits=6, decimal_places=2, default=2.5
    )
    review_goodreads_ratings = models.DecimalField(
        max_digits=20, decimal_places=0, default=0
    )

    def __str__(self):
        return self.review_goodreads


class ReviewSummaryAmazon(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="review_amazon",
    )
    review_amazon = models.TextField()
    review_amazon_star = models.DecimalField(
        max_digits=6, decimal_places=2, default=2.5
    )
    review_amazon_ratings = models.DecimalField(
        max_digits=20, decimal_places=0, default=0
    )

    def __str__(self):
        return self.review_amazon


class ReviewSummaryGenre(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="review_genre",
    )
    review_genre = models.TextField()

    def __str__(self):
        return self.review_genre


class ReviewSummaryAuthor(models.Model):
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name="review_author",
    )
    review_author = models.TextField()

    def __str__(self):
        return self.review_author
