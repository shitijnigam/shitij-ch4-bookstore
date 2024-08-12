# Generated by Django 4.0.10 on 2024-08-12 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_reviewsummaryoverall_reviewsummarygenre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=20)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genres', to='books.book')),
            ],
        ),
    ]
