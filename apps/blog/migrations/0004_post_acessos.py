# Generated by Django 5.0.3 on 2024-04-02 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_data_publicação_post_data_publicacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='acessos',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
