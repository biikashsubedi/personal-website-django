from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField


# Create your models here.


class Profile(models.Model):
    name = models.CharField(_("Name"), max_length=200, default='Bikash Subedi')
    introduction = RichTextField(blank=True, null=True)
    job_title = models.CharField(_("Job Title"), max_length=200, null=True, blank=True, default='Developer')
    image = models.ImageField(_('Image'), default='default/image.png', upload_to='profile')
    resume = models.FileField(_('Resume'), default='default/image.png', upload_to='profile/resume')
    location = models.CharField(_("Location"), max_length=200, null=True, blank=True, default='Kathmandu, Nepal')
    phone1 = models.IntegerField(_("Phone 1"), null=True, blank=True, default=+9779869286303)
    phone2 = models.IntegerField(_("Phone 2"), null=True, blank=True)
    completed_project = models.IntegerField(_("Completed Project"), null=True, blank=True)
    company_linked = models.IntegerField(_("Company Linked"), null=True, blank=True)
    love = models.IntegerField(_("Love"), default=1)

    email1 = models.CharField(_("Email 2"), max_length=200, default='biikashsubedi@gmail.com')
    email2 = models.CharField(_("Email 2"), max_length=200, default='biikashsubedi@outlook.com')

    website = models.CharField(_("Website"), max_length=200, default='bikashsubedi.com.np')
    facebook_link = models.CharField(_("Facebook Link"), max_length=200, null=True, blank=True)
    linkedin_link = models.CharField(_("Linkedin Link"), max_length=200, null=True, blank=True)
    instagram_link = models.CharField(_("Instagram Link"), max_length=200, null=True, blank=True)
    twitter_link = models.CharField(_("Twitter Link"), max_length=200, null=True, blank=True)
    tor_link = models.CharField(_("Tor Link"), max_length=200, null=True, blank=True)
    gmap_link = models.CharField(_("Google Map Link"), max_length=500, null=True, blank=True)

    status = models.BooleanField(_('status'), default=True)
    details = models.JSONField(_("details"), blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'profiles'
        verbose_name_plural = 'Profile'
