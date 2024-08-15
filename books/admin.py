from django.contrib import admin

# Register your models here.

from .models import *


class ReviewInline(admin.TabularInline):
    model = Review


class GenreInlineAdmin(admin.StackedInline):
    model = Genre
    extra = 3
    max_num = 3


class ReviewStarAdmin(admin.StackedInline):
    model = ReviewStar
    extra = 1
    max_num = 1


class ReviewSummaryOverallAdmin(admin.StackedInline):
    model = ReviewSummaryOverall  # contains good, bad
    extra = 1
    max_num = 1


class ReviewSummaryGoodreadsAdmin(admin.StackedInline):
    model = ReviewSummaryGoodreads  # contains goodreads summary and rating
    extra = 1
    max_num = 1


class ReviewSummaryAmazonAdmin(admin.StackedInline):
    model = ReviewSummaryAmazon  # contains amazon summary and rating
    extra = 1
    max_num = 1


class ReviewSummaryGenre(admin.StackedInline):
    model = ReviewSummaryGenre
    extra = 1
    max_num = 1


class ReviewSummaryAuthor(admin.StackedInline):
    model = ReviewSummaryAuthor
    extra = 1
    max_num = 1


class BookAdmin(admin.ModelAdmin):
    inlines = [
        GenreInlineAdmin,
        # ReviewStarAdmin,
        ReviewSummaryOverallAdmin,
        ReviewSummaryGoodreadsAdmin,
        ReviewSummaryAmazonAdmin,
        # ReviewSummaryGenre,
        # ReviewSummaryAuthor,
        ReviewInline,
    ]
    list_display = (
        "title",
        "author",
        # "price",
        "description",
    )


admin.site.register(Book, BookAdmin)
