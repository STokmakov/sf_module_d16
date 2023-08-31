from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from utils.transliteration import transliteration_rus_eng
from django.conf import settings
User = settings.AUTH_USER_MODEL


class Advert(models.Model):
    """Объявления"""
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildemaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    category = models.CharField(
        max_length=20,
        verbose_name="Категория",
        choices=TYPE,
        default='tank',
    )
    subject = models.CharField("Тема", max_length=200)
    description = models.TextField("Объявление", max_length=10000)

    images = models.ForeignKey(
        'gallery.Gallery',
        verbose_name="Изображения",
        blank=True,
        null=True,
        on_delete=models.SET_NULL
    )
    file = models.FileField("Файл", upload_to="callboard_file/", blank=True, null=True)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=200,  blank=True, null=True)

    def save(self, *args, **kwargs):

        self.slug = transliteration_rus_eng(self.subject) + "_" + str(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("advert-detail", kwargs={"category": self.category, "slug": self.slug})


    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class UserResponse(models.Model):
    """Отзовы"""
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)
    advert = models.ForeignKey(Advert, verbose_name="Объявление", on_delete=models.CASCADE)
    subject = models.CharField("Тема", max_length=200)
    description = models.TextField("Объявление", max_length=10000)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.subject
    def save(self, *args, **kwargs):
        super(UserResponse, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Отзов"
        verbose_name_plural = "Отзовы"


