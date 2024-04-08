# Generated by Django 5.0.4 on 2024-04-07 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('numero_parcelas', models.IntegerField(max_length=2)),
                ('preco_parcela', models.DecimalField(decimal_places=2, max_digits=10)),
                ('preco_vista', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imagem', models.ImageField(upload_to='cursos/images')),
                ('tipo', models.CharField(max_length=100)),
                ('avaliacoes', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
        ),
    ]