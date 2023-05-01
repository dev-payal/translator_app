# Generated by Django 4.2 on 2023-04-28 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslatorModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_lang', models.CharField(max_length=10)),
                ('target_lang', models.CharField(max_length=10)),
                ('text', models.TextField()),
                ('translation', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='TranslationCache',
        ),
    ]
