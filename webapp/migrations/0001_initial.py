# Generated by Django 4.1.7 on 2023-04-06 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.TextField(max_length=5000)),
                ('resposta', models.TextField(max_length=5000)),
                ('linguagem', models.CharField(max_length=50)),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('tipo', models.CharField(choices=[('criacao', 'criacao'), ('correcao', 'correcao'), ('geral', 'geral')], max_length=50, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='registros', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
