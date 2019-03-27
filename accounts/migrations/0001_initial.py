# Generated by Django 2.1.7 on 2019-03-27 14:24

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_normal_user', models.BooleanField(default=False)),
                ('is_employer', models.BooleanField(default=False)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(max_length=150, verbose_name='school')),
                ('school_url', models.URLField(verbose_name='School URL')),
                ('major', models.CharField(blank=True, max_length=50)),
                ('result', models.CharField(blank=True, max_length=150, verbose_name='result')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('completion_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('summary', models.TextField(blank=True, max_length=3000, verbose_name='Summary description')),
                ('is_current', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=150)),
                ('company', models.CharField(max_length=150)),
                ('company_url', models.URLField(verbose_name='Company URL')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('completion_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('description', models.TextField(verbose_name='description')),
                ('is_current', models.BooleanField(default=True, verbose_name='still in office')),
            ],
            options={
                'ordering': ['-completion_date', '-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Full names')),
                ('position', models.CharField(max_length=50, verbose_name='Position')),
                ('company', models.CharField(max_length=150)),
                ('phone', models.IntegerField(blank=True, null=True, verbose_name='phone')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='name')),
                ('description', models.TextField(blank=True, max_length=2000)),
                ('level', models.CharField(choices=[(None, 'unknown'), ('B', 'beginner'), ('S', 'skilled'), ('A', 'advanced'), ('E', 'expert')], max_length=1, verbose_name='level')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='NormalUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='users/thumbnail')),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('website', models.URLField(blank=True, max_length=300, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100)),
                ('instagram', models.CharField(blank=True, max_length=100)),
                ('twitter', models.CharField(blank=True, max_length=100)),
                ('linkedin', models.CharField(blank=True, max_length=100)),
                ('google', models.CharField(blank=True, max_length=100)),
                ('pinterest', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='user_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_from_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='user_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel_to_set', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='accounts.NormalUser'),
        ),
        migrations.AddField(
            model_name='referee',
            name='user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='referees', to='accounts.NormalUser'),
        ),
        migrations.AddField(
            model_name='normaluser',
            name='following',
            field=models.ManyToManyField(related_name='followers', through='accounts.Contact', to='accounts.NormalUser'),
        ),
        migrations.AddField(
            model_name='experience',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience', to='accounts.NormalUser'),
        ),
        migrations.AddField(
            model_name='education',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education', to='accounts.NormalUser'),
        ),
    ]
