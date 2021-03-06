# Generated by Django 2.1.4 on 2019-02-13 07:33

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
            name='Backup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_name', models.CharField(max_length=15)),
                ('goods_type', models.IntegerField(choices=[(0, '手机'), (1, '配件'), (3, '其它')])),
                ('dadian_count', models.IntegerField()),
                ('guoaodian_count', models.IntegerField()),
                ('hongweidian_count', models.IntegerField()),
                ('is_lastet', models.BooleanField(default=True)),
                ('save_datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChangePrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_price', models.FloatField()),
                ('new_price', models.FloatField()),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('price', models.FloatField()),
                ('goods_type', models.IntegerField(choices=[(0, '手机'), (1, '配件'), (3, '其它')])),
                ('code', models.CharField(blank=True, max_length=20)),
                ('unsalable', models.BooleanField(default=False)),
                ('update_date', models.DateField(auto_now_add=True)),
                ('recent_sell', models.DateField(blank=True, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('add_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='add_people', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GoodsRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_num', models.IntegerField()),
                ('remark', models.TextField(blank=True, null=True)),
                ('is_delete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='GoodsShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remain', models.IntegerField()),
                ('last_update_date', models.DateTimeField(auto_now=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Goods')),
                ('last_updater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updater_goodsshop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ReturnRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('type', models.IntegerField(choices=[(0, '操作失误'), (1, '退货')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='SellRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('is_delete', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now=True)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Goods')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('principal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='principal_shop', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShopPhoneColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now=True)),
                ('goodsshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.GoodsShop')),
            ],
        ),
        migrations.CreateModel(
            name='TransferGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_num', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('from_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_shop', to='meizu.Shop')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Goods')),
                ('to_shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_name', to='meizu.Shop')),
                ('updater', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updater_transfergoods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='sellrecord',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Shop'),
        ),
        migrations.AddField(
            model_name='sellrecord',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updater_sellrecord', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='returnrecord',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Shop'),
        ),
        migrations.AddField(
            model_name='returnrecord',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updater_returnrecord', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='goodsshop',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Shop'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='sell_record',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='meizu.SellRecord'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Shop'),
        ),
        migrations.AddField(
            model_name='goodsrecord',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updater_goodsrecord', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='changeprice',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meizu.Goods'),
        ),
        migrations.AddField(
            model_name='changeprice',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='updater_changeprice', to=settings.AUTH_USER_MODEL),
        ),
    ]
