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
    model = ReviewSummaryOverall
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
        ReviewStarAdmin,
        ReviewSummaryOverallAdmin,
        ReviewSummaryGenre,
        ReviewSummaryAuthor,
    ]
    list_display = (
        "title",
        "author",
        "price",
    )


admin.site.register(Book, BookAdmin)
