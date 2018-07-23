# Generated by Django 2.0 on 2018-07-22 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('turma', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60, verbose_name='Nome')),
                ('matricula', models.CharField(max_length=11, unique=True, verbose_name='matricula')),
                ('turma', models.ForeignKey(blank=True, on_delete=False, to='turma.Turma')),
            ],
            options={
                'verbose_name_plural': 'Alunos',
                'verbose_name': 'Aluno',
                'ordering': ['nome', 'matricula'],
            },
        ),
    ]
