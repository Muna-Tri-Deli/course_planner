# Generated by Django 2.2 on 2022-11-18 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200520_2028'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='action',
            options={'verbose_name': 'Activities', 'verbose_name_plural': 'Activities'},
        ),
        migrations.AlterModelOptions(
            name='boardcomment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comment'},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Course'},
        ),
        migrations.AlterModelOptions(
            name='collectboard',
            options={'verbose_name': 'Collections and likes', 'verbose_name_plural': 'Collections and likes'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comments', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='messageboard',
            options={'verbose_name': 'Comments', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='num',
            options={'verbose_name': 'Statistics', 'verbose_name_plural': 'Statistics'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Rating Information', 'verbose_name_plural': 'Rating Information'},
        ),
        migrations.AlterModelOptions(
            name='tags',
            options={'verbose_name': 'Tag', 'verbose_name_plural': 'Tag'},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'User'},
        ),
        migrations.AlterField(
            model_name='action',
            name='content',
            field=models.TextField(verbose_name='Activity Content'),
        ),
        migrations.AlterField(
            model_name='action',
            name='one',
            field=models.ImageField(upload_to='media', verbose_name='First'),
        ),
        migrations.AlterField(
            model_name='action',
            name='status',
            field=models.BooleanField(verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='action',
            name='three',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Third'),
        ),
        migrations.AlterField(
            model_name='action',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Activity title'),
        ),
        migrations.AlterField(
            model_name='action',
            name='two',
            field=models.ImageField(null=True, upload_to='media', verbose_name='Second'),
        ),
        migrations.AlterField(
            model_name='action',
            name='user',
            field=models.ManyToManyField(blank=True, to='user.User', verbose_name='Participants'),
        ),
        migrations.AlterField(
            model_name='actioncomment',
            name='action',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Action', verbose_name='Activities'),
        ),
        migrations.AlterField(
            model_name='actioncomment',
            name='comment',
            field=models.TextField(verbose_name='Activity Comments'),
        ),
        migrations.AlterField(
            model_name='actioncomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='boardcomment',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='boardcomment',
            name='message_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.MessageBoard', verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='boardcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user.User', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=32, verbose_name='Instructor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='collect',
            field=models.ManyToManyField(blank=True, to='user.User', verbose_name='Collector'),
        ),
        migrations.AlterField(
            model_name='book',
            name='good',
            field=models.CharField(max_length=32, verbose_name='Course Number'),
        ),
        migrations.AlterField(
            model_name='book',
            name='intro',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='num',
            field=models.IntegerField(default=0, verbose_name='Views'),
        ),
        migrations.AlterField(
            model_name='book',
            name='pic',
            field=models.FileField(max_length=64, upload_to='book_cover', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='book',
            name='rate_num',
            field=models.IntegerField(default=0, verbose_name='Number of Ratings'),
        ),
        migrations.AlterField(
            model_name='book',
            name='sump',
            field=models.IntegerField(default=0, verbose_name='Collections'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='user.Tags', verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=32, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='collectboard',
            name='is_collect',
            field=models.BooleanField(default=False, verbose_name='Collect?'),
        ),
        migrations.AlterField(
            model_name='collectboard',
            name='is_like',
            field=models.BooleanField(default=False, verbose_name='Like?'),
        ),
        migrations.AlterField(
            model_name='collectboard',
            name='message_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.MessageBoard', verbose_name='Comments'),
        ),
        migrations.AlterField(
            model_name='collectboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='Users'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Book', verbose_name='Courses'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='good',
            field=models.IntegerField(default=0, verbose_name='Likes'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='Users'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='collect_num',
            field=models.IntegerField(default=0, verbose_name='Collections'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='feebback_num',
            field=models.IntegerField(default=0, verbose_name='Replies'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='like_num',
            field=models.IntegerField(default=0, verbose_name='Likes'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='look_num',
            field=models.IntegerField(default=1, verbose_name='Clicks'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='messageboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='num',
            name='actions',
            field=models.IntegerField(default=0, verbose_name='Activities Summary'),
        ),
        migrations.AlterField(
            model_name='num',
            name='books',
            field=models.IntegerField(default=0, verbose_name='Number of Courses'),
        ),
        migrations.AlterField(
            model_name='num',
            name='comments',
            field=models.IntegerField(default=0, verbose_name='Number of Comments'),
        ),
        migrations.AlterField(
            model_name='num',
            name='message_boards',
            field=models.IntegerField(default=0, verbose_name='Comments Summary'),
        ),
        migrations.AlterField(
            model_name='num',
            name='rates',
            field=models.IntegerField(default=0, verbose_name='Ratings Summary'),
        ),
        migrations.AlterField(
            model_name='num',
            name='users',
            field=models.IntegerField(default=0, verbose_name='Number of Users'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Book', verbose_name='Course id'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publish time'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='mark',
            field=models.FloatField(verbose_name='Rate'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='User id'),
        ),
        migrations.AlterField(
            model_name='tags',
            name='name',
            field=models.CharField(max_length=32, verbose_name='Tag'),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=32, verbose_name='Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email Address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=32, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=32, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=32, verbose_name='Phone NUmber'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=32, unique=True, verbose_name='Account'),
        ),
    ]