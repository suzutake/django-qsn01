from django.db import models

# Create your models here.
from django.core import validators


class Item(models.Model):

    name = models.CharField(
        verbose_name='name',
        max_length=50,
    )

    price_total = models.IntegerField(
        verbose_name='price_total',
        blank=True,
        null=True,
    )

    staff_1 = models.CharField(
        verbose_name='staff_1',
        max_length=50,
        blank=True,
    )
    price_1 = models.IntegerField(
        verbose_name='price_1',
        blank=True,
        null=True,
        default=0,
    )
    staff_2 = models.CharField(
        verbose_name='staff_2',
        max_length=50,
        blank=True,
    )
    price_2 = models.IntegerField(
        verbose_name='price_2',
        blank=True,
        null=True,
        default=0,
    )
    staff_3 = models.CharField(
        verbose_name='staff_3',
        max_length=50,
        blank=True,
    )
    price_3 = models.IntegerField(
        verbose_name='price_3',
        blank=True,
        null=True,
        default=0,
    )
    staff_4 = models.CharField(
        verbose_name='staff_4',
        max_length=50,
        blank=True,
    )
    price_4 = models.IntegerField(
        verbose_name='price_4',
        blank=True,
        null=True,
        default=0,
    )
    staff_5 = models.CharField(
        verbose_name='staff_5',
        max_length=50,
        blank=True,
    )
    price_5 = models.IntegerField(
        verbose_name='price_5',
        blank=True,
        null=True,
        default=0,
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )

    # 管理サイト上の表示設定
    def __str__(self):
        self.price_total=self.price_1
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'

    def save(self, **kwargs):
        u"""insertする直前に主キーの値をつくる"""
        if self.price_1 is not None:
            if self.price_2 is not None:
                if self.price_3 is not None:
                    if self.price_4 is not None:
                        if self.price_5 is not None:
                            self.price_total = self.price_1 + self.price_2 + self.price_3 + self.price_4 + self.price_5
                        else:
                            self.price_total = self.price_1 + self.price_2 + self.price_3 + self.price_4
                    else:
                        self.price_total = self.price_1 + self.price_2 + self.price_3
                else:
                    self.price_total = self.price_1 + self.price_2
            else:
                self.price_total = self.price_1

        super(Item, self).save(**kwargs)
