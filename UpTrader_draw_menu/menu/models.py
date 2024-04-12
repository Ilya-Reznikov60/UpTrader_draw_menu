from django.db import models


class MenuItem(models.Model):
    """
    Модель для хранения пунктов меню.
    """
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок'
    )
    url = models.CharField(
        max_length=100,
        verbose_name='URL',
        help_text='URL пункта меню'
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        verbose_name='Родительский элемент'
    )
    named_url = models.CharField(
        max_length=250,
        null=True,
        blank=True,
        verbose_name='Именованный URL'
    )

    class Meta:
        ordering = ('title',)
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return self.title
