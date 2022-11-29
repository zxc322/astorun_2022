# Generated by Django 3.2.9 on 2022-11-29 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, default='user', max_length=200, null=True)),
                ('order_price', models.IntegerField()),
                ('discount_percent', models.CharField(max_length=10)),
                ('customer_name', models.CharField(max_length=28)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(max_length=28)),
                ('delivery_region', models.CharField(choices=[('Вiнницька область', 'Вiнницька область'), ('Волинська область', 'Волинська область'), ('Днiпропетровська область', 'Днiпропетровська область'), ('Донецька область', 'Донецька область'), ('Житомирська область', 'Житомирська область'), ('Закарпатська область', 'Закарпатська область'), ('Запорiжська область', 'Запорiжська область'), ('Iвано-Франкiвська область', 'Iвано-Франкiвська область'), ('Київська область', 'Київська область'), ('Кiровоградська область', 'Кiровоградська область'), ('Луганська область', 'Луганська область'), ('Львiвська область', 'Львiвська область'), ('Миколаївська область', 'Миколаївська область'), ('Одеська область', 'Одеська область'), ('Полтавська область', 'Полтавська область'), ('Рiвненська область', 'Рiвненська область'), ('Сумська область', 'Сумська область'), ('Тернопiльська область', 'Тернопiльська область'), ('Харкiвська область', 'Харкiвська область'), ('Херсонська область', 'Херсонська область'), ('Хмельницька область', 'Хмельницька область'), ('Черкаська область', 'Черкаська область'), ('Чернiгiвська область', 'Чернiгiвська область'), ('Чернiвецька область', 'Чернiвецька область')], default=None, max_length=40)),
                ('delivery_district', models.CharField(blank=True, default=None, max_length=40)),
                ('delivery_city', models.CharField(default=None, max_length=40)),
                ('nova_poshta_departament', models.SmallIntegerField(default=None)),
                ('comment', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, default='user', max_length=200, null=True)),
                ('order_price', models.IntegerField()),
                ('delivery_price', models.IntegerField(default=0, null=True)),
                ('customer_name', models.CharField(max_length=28)),
                ('customer_email', models.EmailField(max_length=254)),
                ('customer_phone', models.CharField(max_length=28)),
                ('delivery_region', models.CharField(choices=[('Вiнницька область', 'Вiнницька область'), ('Волинська область', 'Волинська область'), ('Днiпропетровська область', 'Днiпропетровська область'), ('Донецька область', 'Донецька область'), ('Житомирська область', 'Житомирська область'), ('Закарпатська область', 'Закарпатська область'), ('Запорiжська область', 'Запорiжська область'), ('Iвано-Франкiвська область', 'Iвано-Франкiвська область'), ('Київська область', 'Київська область'), ('Кiровоградська область', 'Кiровоградська область'), ('Луганська область', 'Луганська область'), ('Львiвська область', 'Львiвська область'), ('Миколаївська область', 'Миколаївська область'), ('Одеська область', 'Одеська область'), ('Полтавська область', 'Полтавська область'), ('Рiвненська область', 'Рiвненська область'), ('Сумська область', 'Сумська область'), ('Тернопiльська область', 'Тернопiльська область'), ('Харкiвська область', 'Харкiвська область'), ('Херсонська область', 'Херсонська область'), ('Хмельницька область', 'Хмельницька область'), ('Черкаська область', 'Черкаська область'), ('Чернiгiвська область', 'Чернiгiвська область'), ('Чернiвецька область', 'Чернiвецька область')], default=None, max_length=40)),
                ('delivery_district', models.CharField(blank=True, default=None, max_length=40)),
                ('delivery_city', models.CharField(default=None, max_length=40)),
                ('nova_poshta_departament', models.SmallIntegerField(default=None)),
                ('comment', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=40)),
                ('status_en', models.CharField(max_length=40, null=True)),
                ('status_ru', models.CharField(max_length=40, null=True)),
                ('status_uk', models.CharField(max_length=40, null=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Status',
            },
        ),
        migrations.CreateModel(
            name='ProductInOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default='Universal', max_length=10)),
                ('color', models.CharField(default='white', max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price_per_item', models.IntegerField(default=0)),
                ('total_price', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
            options={
                'verbose_name': 'Product in Order',
                'verbose_name_plural': 'Products in Order',
            },
        ),
        migrations.CreateModel(
            name='ProductInCollectionOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(default='Universal', max_length=10)),
                ('color', models.CharField(default='white', max_length=20, null=True)),
                ('price_per_item', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('col_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.collectionorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInBasket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_key', models.CharField(max_length=140)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('size', models.CharField(max_length=30)),
                ('color', models.CharField(default='white', max_length=20, null=True)),
                ('price_per_item', models.IntegerField(default=0)),
                ('product_total_price', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('order', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'verbose_name': 'Product in Basket',
                'verbose_name_plural': 'Products in Basket',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.status'),
        ),
        migrations.AddField(
            model_name='collectionorder',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.status'),
        ),
    ]
