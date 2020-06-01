# Generated by Django 3.0.5 on 2020-05-31 23:51

from django.conf import settings
import django.contrib.auth.models
import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import imagekit.models.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(db_index=True, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=50, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username')),
                ('email', models.EmailField(db_index=True, error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True, verbose_name='Email Address')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=150, null=True, verbose_name='Last Name')),
                ('photo', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='profiles/%Y/%m/%d', verbose_name='Photo')),
                ('lang', models.CharField(choices=[('es', 'Spanish'), ('en', 'English')], default='en', max_length=6, verbose_name='Language')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PhoneDevice',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='UUID')),
                ('token', models.TextField(blank=True, db_index=True, null=True, verbose_name='Device ID')),
                ('platform', models.CharField(choices=[('android', 'Android'), ('ios', 'iOS'), ('web', 'Web')], max_length=10)),
                ('model_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='Model Name')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='devices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Phone Device',
                'verbose_name_plural': 'Phone Devices',
                'db_table': 'phone_devices',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='PendingAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('confirm_email', 'Confirm e-mail'), ('reset_password', 'Reset Password')], db_index=True, max_length=50)),
                ('token', models.CharField(db_index=True, default=uuid.uuid4, max_length=150)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField(blank=True, null=True)),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder, help_text='This field changes according to the type of action', verbose_name='extra')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pending_actions', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Pending Action',
                'verbose_name_plural': 'Pending Actions',
                'db_table': 'pending_actions',
            },
        ),
    ]
