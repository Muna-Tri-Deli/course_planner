# Generated by Django 2.0.1 on 2020-03-20 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one', models.ImageField(upload_to='media', verbose_name='第一')),
                ('two', models.ImageField(null=True, upload_to='media', verbose_name='第二')),
                ('three', models.ImageField(null=True, upload_to='media', verbose_name='第三')),
                ('title', models.CharField(max_length=64, verbose_name='活动标题')),
                ('content', models.TextField(verbose_name='活动内容')),
                ('status', models.BooleanField(verbose_name='状态')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
            },
        ),
        migrations.CreateModel(
            name='ActionComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='活动评论')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Action', verbose_name='活动')),
            ],
        ),
        migrations.CreateModel(
            name='BoardComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '子留言',
                'verbose_name_plural': '子留言',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sump', models.IntegerField(default=0, verbose_name='收藏人数')),
                ('title', models.CharField(max_length=32, verbose_name='书名')),
                ('author', models.CharField(max_length=32, verbose_name='作者')),
                ('intro', models.TextField(verbose_name='描述')),
                ('num', models.IntegerField(default=0, verbose_name='浏览量')),
                ('pic', models.FileField(max_length=64, upload_to='book_cover', verbose_name='封面图片')),
                ('good', models.CharField(choices=[('诺贝尔文学奖', '诺贝尔文学奖'), ('茅盾文学奖', '茅盾文学奖'), ('None', 'None')], default=None, max_length=32, verbose_name='获奖')),
            ],
            options={
                'verbose_name': '图书',
                'verbose_name_plural': '图书',
            },
        ),
        migrations.CreateModel(
            name='CollectBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('is_collect', models.BooleanField(default=False, verbose_name='是否收藏')),
                ('is_like', models.BooleanField(default=False, verbose_name='是否点赞')),
            ],
            options={
                'verbose_name': '收藏/点赞留言',
                'verbose_name_plural': '收藏/点赞留言',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='内容')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('good', models.IntegerField(default=0, verbose_name='点赞')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Book', verbose_name='书籍')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='MessageBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('look_num', models.IntegerField(default=1, verbose_name='点击数')),
                ('like_num', models.IntegerField(default=0, verbose_name='点赞数')),
                ('feebback_num', models.IntegerField(default=0, verbose_name='回复数')),
                ('collect_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': '留言',
                'verbose_name_plural': '留言',
            },
        ),
        migrations.CreateModel(
            name='Num',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.IntegerField(default=0, verbose_name='用户数量')),
                ('books', models.IntegerField(default=0, verbose_name='书本数量')),
                ('comments', models.IntegerField(default=0, verbose_name='评论数量')),
                ('rates', models.IntegerField(default=0, verbose_name='评分汇总')),
                ('actions', models.IntegerField(default=0, verbose_name='活动汇总')),
                ('message_boards', models.IntegerField(default=0, verbose_name='留言汇总')),
            ],
            options={
                'verbose_name': '数据统计',
                'verbose_name_plural': '数据统计',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.FloatField(verbose_name='评分')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Book', verbose_name='图书id')),
            ],
            options={
                'verbose_name': '评分信息',
                'verbose_name_plural': '评分信息',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='标签')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='账号')),
                ('password', models.CharField(max_length=32, verbose_name='密码')),
                ('phone', models.CharField(max_length=32, verbose_name='手机号码')),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='名字')),
                ('address', models.CharField(max_length=32, verbose_name='地址')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
            ],
            options={
                'verbose_name': '用户',
                'verbose_name_plural': '用户',
            },
        ),
        migrations.AddField(
            model_name='rate',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户id'),
        ),
        migrations.AddField(
            model_name='messageboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='collectboard',
            name='message_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.MessageBoard', verbose_name='留言'),
        ),
        migrations.AddField(
            model_name='collectboard',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='book',
            name='collect',
            field=models.ManyToManyField(blank=True, to='user.User', verbose_name='收藏者'),
        ),
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='user.Tags', verbose_name='标签'),
        ),
        migrations.AddField(
            model_name='boardcomment',
            name='message_board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.MessageBoard', verbose_name='留言'),
        ),
        migrations.AddField(
            model_name='boardcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='user.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='actioncomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User', verbose_name='用户'),
        ),
        migrations.AddField(
            model_name='action',
            name='user',
            field=models.ManyToManyField(blank=True, to='user.User', verbose_name='参加用户'),
        ),
    ]
