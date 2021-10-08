# Generated by Django 3.2.6 on 2021-08-14 14:28

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='book',
            managers=[
                ('active_books', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='is_deleted',
            field=models.CharField(default='N', max_length=1),
        ),
    ]