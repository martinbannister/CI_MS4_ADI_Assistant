from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings
from django.db import models
from datetime import date


class Customer(models.Model):

    class CustomerType(models.IntegerChoices):
        LEARNER = 1, _('Learner')
        TRAINEE = 2, _('Trainee (PDI)')

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    google_contact_id = models.CharField(max_length=20)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    customer_type = models.IntegerField(choices=CustomerType.choices)
    hourly_rate = models.DecimalField(max_digits=5, decimal_places=2)
    balance_hours = models.DecimalField(max_digits=3, decimal_places=1)
    balance_payment = models.DecimalField(max_digits=5, decimal_places=2)
    phone = models.CharField(max_length=14)
    email = models.EmailField()
    address1 = models.CharField(max_length=80, null=False, blank=False)
    address2 = models.CharField(max_length=80, null=True, blank=True)
    town = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    active = models.BooleanField()

    def __str__(self):
        """String for representing the Customer Model object."""
        return f'{self.firstname} {self.lastname}'


class SubjectCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Subject Categories'

    category_name = models.CharField(max_length=50)

    def __str__(self):
        """String for representing the Subject Category Model object."""
        return self.category_name


class Subject(models.Model):
    category = models.ForeignKey(SubjectCategory, verbose_name=_("Category"),
                                 on_delete=models.CASCADE)
    subject_name = models.CharField(_("Subject"), max_length=50)

    def __str__(self):
        """String for representing the Subject Model object."""
        return self.subject_name


class Progress(models.Model):

    class Meta:
        verbose_name_plural = 'Progress'

    customer = models.ForeignKey(Customer, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='progressrecord')
    date_of_lesson = models.DateField(null=False, blank=False,
                                      default=date.today)
    time_of_lesson = models.TimeField(null=False, blank=False,
                                      default=timezone.now)
    hours = models.DecimalField(max_digits=2, decimal_places=1)
    payment_taken = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        """String for representing the Progress Model object."""
        return f'{self.customer} - {self.date_of_lesson}'


class ProgressItem(models.Model):
    progress = models.ForeignKey(Progress, null=False, blank=False,
                                 on_delete=models.CASCADE,
                                 related_name='progressitems')
    subject = models.ForeignKey(Subject, null=False, blank=False,
                                on_delete=models.CASCADE,
                                related_name='subjects')
    score = models.IntegerField()
    comments = models.TextField()
    practice_next_lesson = models.BooleanField()

    def __str__(self):
        """String for representing the ProgressItem Model object."""
        return self.subject
