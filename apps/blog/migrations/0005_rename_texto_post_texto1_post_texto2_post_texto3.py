# Generated by Django 5.0.3 on 2024-04-05 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_acessos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='texto',
            new_name='texto1',
        ),
        migrations.AddField(
            model_name='post',
            name='texto2',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='texto3',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
