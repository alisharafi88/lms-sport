from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from courses.models import Course


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PAID = 'p', _('Paid')
        UNPAID = 'u', _('Unpaid')
        CANCELED = 'c', _('Canceled')

    class AccessStatus(models.TextChoices):
        ONLINE = 'o', _('Online')
        DVD = 'd', _('DVD')

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name=_('customer')
    )
    status = models.CharField(
        _('status'),
        max_length=1,
        choices=OrderStatus.choices,
        default=OrderStatus.UNPAID
    )
    access_status = models.CharField(
        _('access status'),
        max_length=1,
        choices=AccessStatus.choices,
        default=AccessStatus.ONLINE
    )
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)
    total_price = models.DecimalField(_('total price'), max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.customer.username


class DVDOrderDetail(models.Model):
    class DeliveryStatus(models.TextChoices):
        PENDING = 'p', _('Pending')
        SENT = 's', _('Sent')
        REJECTED = 'r', _('Rejected')
        CANCELED = 'c', _('Canceled')

    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name='dvd_detail', verbose_name=_('order'),)
    address = models.CharField(_('address'), max_length=255,)
    postal_code = models.CharField(_('postal code'), max_length=20,)
    order_note = models.CharField(_('order note'), max_length=255, null=True, blank=True,)

    delivery_status = models.CharField(_('delivery status'), max_length=1, choices=DeliveryStatus.choices,
                                       default=DeliveryStatus.PENDING,)

    date_created = models.DateTimeField(_('date created'), auto_now_add=True,)

    def __str__(self):
        return f'{self.order} - DVD Details'

    def save(self, *args, **kwargs):
        super().save()
        self.order.access_status = self.order.AccessStatus.DVD


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name=_('order')
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        related_name='order_items',
        verbose_name=_('course')
    )
    unit_price = models.DecimalField(_('unit price'), max_digits=6, decimal_places=2)

    class Meta:
        unique_together = ('order', 'course')

    def __str__(self):
        return f'{self.order} - {self.course}'
