from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.urls import reverse


class ProgramEdu(models.Model):
    """Конкретная программа обучения."""

    name = models.CharField(
        max_length=40,
        db_index=True,
        unique=True,
        verbose_name='Название'
        )
    slug = models.SlugField(
        max_length=40,
        db_index=True,
        unique=True,
        verbose_name='URL'
        )
    min_age = models.PositiveIntegerField(
        default=0,
        verbose_name='Минимальный возраст'
    )
    max_age = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(18),
            MinValueValidator(1)
        ],
        verbose_name='Максимальный возраст'
    )
    about = models.TextField(
        blank=True,
        verbose_name='О программе'
        )
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/',
        verbose_name='Фото программы'
    )
    price = models.IntegerField(
        blank=True,
        verbose_name='Стоимость обучения'
        )

    def get_absolute_url(self):
        return reverse('programm', kwargs={'prog_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Программу'
        verbose_name_plural = 'Программы'
        ordering = ['id']


class ScheduleEdu(models.Model):
    """Расписание занятий."""

    class WeekDay(models.TextChoices):
        """Дни недели."""

        MONDAY = "1", _("Понедельник")
        TUESDAY = "2", _("Вторник")
        WEDNESDAY = "3", _("Среда")
        THURSDAY = "4", _("Четверг")
        FRIDAY = "5", _("Пятница")
        SATURDAY = "6", _("Суббота")
        SUNDAY = "7", _("Воскресенье")

    name_id = models.ForeignKey(
        'ProgramEdu',
        on_delete=models.CASCADE,
        default=1,
        verbose_name='ID программы'
    )
    week_day = models.CharField(
        max_length=3,
        choices=WeekDay.choices,
        default=WeekDay.MONDAY,
        verbose_name='День недели'
    )
    start_edu = models.TimeField(
        auto_now=False,
        verbose_name='Начало урока'
        )
    finish_edu = models.TimeField(
        auto_now=False,
        verbose_name='Конец урока'
        )

    def __str__(self):
        return self.week_day

    class Meta:
        verbose_name = 'Расписание занятий'
        verbose_name_plural = 'Расписание занятий'
        ordering = ['id']


class PersonForm(models.Model):
    """Для форм обратной связи."""

    person = models.CharField(
        max_length=255,
        db_index=True,
        verbose_name='Имя пользователя'
        )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Почта'
        )
    phone_number = models.CharField(
        max_length=16,
        unique=True,
        verbose_name='Телефон'
        )
    add_text = models.TextField(
        blank=True,
        verbose_name='Сообщение'
        )

    def __str__(self):
        return self.person

    class Meta:
        verbose_name = 'Форму обратной связи'
        verbose_name_plural = 'Форма обратной связи'
        ordering = ['id']
