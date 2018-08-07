from django.db import models
from django.utils import timezone
from .validators import validate_image_extension


class Group(models.Model):
    parent = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='child_groups'
    )
    icon = models.ImageField(
        upload_to='Images/Groups/',
        default='Images/None/no-element-icon.jpg',
        validators=[validate_image_extension, ]
    )
    name = models.CharField(
        max_length=64
    )
    description = models.CharField(
        max_length=512,
        blank=True,
        default=''
    )

    def get_child_group_count(self):
        return self.child_groups.count()

    def get_child_elements_count(self):
        return self.elements.count()

    def __str__(self):
        return self.name


class Element(models.Model):
    parent = models.ForeignKey(
        Group,
        on_delete=models.PROTECT,
        related_name='elements'
    )
    icon = models.ImageField(
        upload_to='Images/Elements/',
        default='Images/None/no-group-icon.jpg',
        validators=[validate_image_extension, ]
    )
    name = models.CharField(
        max_length=64
    )
    description = models.CharField(
        max_length=512,
        blank=True,
        default=''
    )
    creation_name = models.DateField(
        default=timezone.now
    )
    verified = models.NullBooleanField()

    def __str__(self):
        return self.name
