# Generated by Django 2.1.7 on 2019-04-30 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommsChannel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel_id', models.CharField(max_length=20)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='HeadlinePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_ts', models.CharField(max_length=20, null=True)),
                ('comms_channel', models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='slack.CommsChannel')),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=30)),
                ('time', models.DateTimeField()),
                ('repeat_count', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='PinnedMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.CharField(max_length=50)),
                ('message_ts', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Incident')),
            ],
        ),
        migrations.CreateModel(
            name='UserStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=50)),
                ('join_time', models.DateTimeField(null=True)),
                ('message_count', models.IntegerField(default=0)),
                ('incident', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Incident')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='userstats',
            unique_together={('incident', 'user_id')},
        ),
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together={('incident', 'key')},
        ),
    ]
