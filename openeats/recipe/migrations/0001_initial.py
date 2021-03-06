# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 19:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('recipe_groups', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NoteRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='note')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Recipe Title')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=b'title', unique=True, verbose_name='slug')),
                ('photo', models.ImageField(blank=True, upload_to=b'upload/recipe_photos', verbose_name='photo')),
                ('info', models.TextField(help_text=b'enter information about the recipe', verbose_name='info')),
                ('cook_time', models.IntegerField(help_text=b'enter time in minutes', verbose_name='cook time')),
                ('servings', models.IntegerField(help_text=b'enter total number of servings', verbose_name='servings')),
                ('directions', models.TextField(verbose_name='directions')),
                ('shared', models.IntegerField(choices=[(0, 'Share'), (1, 'Private')], default=0, help_text=b'share the recipe with the community or mark it private', verbose_name='shared')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('rating_votes', models.PositiveIntegerField(blank=True, default=0, editable=False)),
                ('rating_score', models.IntegerField(blank=True, default=0, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_groups.Course', verbose_name='course')),
                ('cuisine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe_groups.Cuisine', verbose_name='cuisine')),
                ('related', models.OneToOneField(blank=True, help_text=b'relate another recipe', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='RecipeRelated', to='recipe.Recipe', verbose_name='related')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=b'separate with commas', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
            ],
            options={
                'ordering': ['pub_date', 'title'],
            },
        ),
        migrations.CreateModel(
            name='ReportedRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe', verbose_name='recipe')),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='author')),
            ],
            options={
                'ordering': ['pub_date', 'recipe'],
            },
        ),
        migrations.CreateModel(
            name='StoredRecipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe', verbose_name='recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.AddField(
            model_name='noterecipe',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.Recipe', verbose_name='recipe'),
        ),
    ]
