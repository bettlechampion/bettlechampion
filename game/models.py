from django.db import models
from django.core.validators import URLValidator

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class footer(models.Model):
    instagram = models.TextField(validators=[URLValidator()])
    twitter = models.TextField(validators=[URLValidator()])
    youtube = models.TextField(validators=[URLValidator()])
    whatsapp = models.TextField(validators=[URLValidator()])
    facebook = models.TextField(validators=[URLValidator()])

    def __str__(self):
        return f"Social Media Links"


class FAQ(models.Model):
    question = models.CharField(max_length=800)
    answer = models.TextField()

    def __str__(self):
        return self.question


class Partner(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='partners/')
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class NewsletterSubscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Turnaments(models.Model):
    name = models.CharField(max_length=100)
    game_image = models.ImageField(upload_to='turnaments/')
    banner_image = models.ImageField(upload_to='turnaments/')
    prize_pool = models.IntegerField()
    prize_1 = models.IntegerField()
    prize_2 = models.IntegerField()
    prize_3 = models.IntegerField()
    game_overview = models.TextField()
    game_format = models.TextField()
    game_rules = models.TextField()
    matchmaking = models.TextField()
    reamaining_seats = models.IntegerField()
    reserved_seats = models.IntegerField()
    total_seats = models.IntegerField()
    entry_fee = models.CharField(max_length=5)
    datetime = models.DateTimeField()
    
    link = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True)
    game_paas = models.TextField()

        # SEO Fields
    meta_title = models.CharField(max_length=200, blank=True, null=True)  # Meta title for SEO
    meta_description = models.TextField(blank=True, null=True)  # Meta description for SEO
    meta_keywords = models.CharField(max_length=300, blank=True, null=True)  # Meta keywords for SEO

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            # Automatically generate slug from name
            self.slug = slugify(self.name)
        super(Turnaments, self).save(*args, **kwargs)


class CustomUser(AbstractUser):
    fullname = models.CharField(max_length=255, verbose_name="Full Name")
    mobile = models.CharField(max_length=15, unique=True,
                              verbose_name="Mobile Number")  # Unique mobile number
    city = models.CharField(max_length=100, blank=True,
                            null=True, verbose_name="City")
    
    email = models.EmailField(
        unique=True, verbose_name="Email")  # Unique email address
    # New profile picture field
    profile_image = models.ImageField(upload_to='profile_pics/', blank=True, null=True, verbose_name="Profile Picture")

    def __str__(self):
        return self.username


class Leaderboard(models.Model):
    game_name_with_date =  models.CharField( max_length=500)
    first_place = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='first_place',
        verbose_name='1st Place'
    )
    second_place = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='second_place',
        verbose_name='2nd Place'
    )
    third_place = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='third_place',
        verbose_name='3rd Place'
    )
    first_prize = models.CharField(max_length=50)
    second_prize = models.CharField(max_length=50)
    third_prize = models.CharField(max_length=50)

    def __str__(self):
        return "game_name_with_date"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"



class SocialMediaLinks(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="social_media_links")
    facebook = models.URLField(validators=[URLValidator()], blank=True, null=True)
    instagram = models.URLField(validators=[URLValidator()], blank=True, null=True)
    twitter = models.URLField(validators=[URLValidator()], blank=True, null=True)
    youtube = models.URLField(validators=[URLValidator()], blank=True, null=True)

    def __str__(self):
        return f"Social Media Links for {self.user.username}"
    

class TournamentEnrollment(models.Model):
    WIN_CHOICES = [
        ('win', 'Win'),
        ('loss', 'Loss'),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="enrollments")
    tournament = models.ForeignKey('Turnaments', on_delete=models.CASCADE, related_name="enrolled_users")
    enrolled_on = models.DateTimeField(auto_now_add=True)
    in_top_three = models.BooleanField(default=False)  # To track if the user made it to the top 3
    win = models.CharField(max_length=4, choices=WIN_CHOICES, default='loss') 
    placement = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.tournament.name}"

    class Meta:
        unique_together = ('user', 'tournament') 
        
        

class Badge(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='badges')
    title = models.CharField(max_length=100)
    badge_image = models.ImageField(upload_to='badges/')
    status = models.CharField(max_length=100, blank=True, null=True)  # Example: "Won: Yes" or "Won: No"

    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    

class WhyJoinUs(models.Model):
    title = models.CharField(max_length=100)  # The title of the feature (e.g. "Find Local Players")
    description = models.TextField()          # The description text of the feature
    image = models.ImageField(upload_to='why_join_us/')  # Image for the feature (upload path set)

    def __str__(self):
        return self.title 
    
class how_it_works(models.Model):
    step_1 =  models.CharField(max_length=100)     
    step_1_description =  models.CharField(max_length=100)    
    step_1_image = models.ImageField(upload_to='how_it_works/')  
    step_2 =  models.CharField(max_length=100)     
    step_2_description =  models.CharField(max_length=100)    
    step_2_image = models.ImageField(upload_to='how_it_works/')  
    step_3 =  models.CharField(max_length=100)   
    step_3_description =  models.CharField(max_length=100)   
    step_3_image = models.ImageField(upload_to='how_it_works/')  
    
    
    

    def __str__(self):
        return f'{self.step_1} - {self.step_2} - {self.step_3}'
    

class CTA(models.Model):
    title = models.CharField(max_length=100)  # The title of the feature (e.g. "Find Local Players")
    description = models.TextField()          # The description text of the feature
    image = models.ImageField(upload_to='why_join_us/')  # Image for the feature (upload path set)

    def __str__(self):
        return self.title 