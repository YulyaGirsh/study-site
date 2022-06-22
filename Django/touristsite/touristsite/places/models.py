from django.db import models


class Places(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Текст')  # поле не обязательно к заполнению
    creates_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name='Тип локации')
    sale = models.ManyToManyField('Sales', null=True, verbose_name='Акция', blank=True)
    views = models.IntegerField(default=0)



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['-creates_at']


class Categories(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование', db_index=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class Sales(models.Model):
    FAMILY = 'Семейный'
    FRIEND = 'Приведи друга'
    TEACHER = 'Учитель'
    CURRENCY_CHOICES = [
        (FAMILY, 'Семейный'),
        (FRIEND,'Приведи друга'),
        (TEACHER, 'Учитель')
    ]
    title = models.CharField(max_length=150, verbose_name='Акция', db_index=True, choices=CURRENCY_CHOICES)
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class Review(models.Model):
    title = models.CharField(max_length=150, verbose_name='Краткое описание')
    content = models.TextField(blank=True, verbose_name='Текст')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Categories', on_delete=models.PROTECT, null=True, verbose_name='Тип локации')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
