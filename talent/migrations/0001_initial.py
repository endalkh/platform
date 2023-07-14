# Generated by Django 4.2.2 on 2023-07-14 21:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=250)),
                ('preferred_name', models.CharField(max_length=150)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('headline', models.TextField()),
                ('test_user', models.BooleanField(blank=True, default=False)),
                ('overview', models.TextField(blank=True)),
                ('send_me_bounties', models.BooleanField(default=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'People',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(db_index=True, default=False)),
                ('selectable', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='talent.skill')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PersonWebsite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.CharField(max_length=200)),
                ('type', models.IntegerField(choices=[(0, 'Personal'), (1, 'Company')])),
                ('person', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='websites', to='talent.person')),
            ],
        ),
        migrations.CreateModel(
            name='PersonSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.JSONField(blank=True, null=True)),
                ('expertise', models.JSONField(blank=True, null=True)),
                ('person', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='talent.person')),
            ],
        ),
        migrations.CreateModel(
            name='Expertise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('selectable', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='expertise_children', to='talent.expertise')),
                ('skill', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skill_expertise', to='talent.skill')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
