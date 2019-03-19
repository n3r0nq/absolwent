# Generated by Django 2.1.7 on 2019-03-12 13:40

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
            name='Absolwent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Klasa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(default='', max_length=3, verbose_name='nazwa klasy')),
                ('rok_matury', models.IntegerField(default=0, verbose_name='rok matury')),
                ('rok_naboru', models.IntegerField(default=0, verbose_name='rok naboru')),
            ],
        ),
        migrations.AddField(
            model_name='absolwent',
            name='klasa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='uczniowie', to='osoby.Klasa'),
        ),
        migrations.AddField(
            model_name='absolwent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]