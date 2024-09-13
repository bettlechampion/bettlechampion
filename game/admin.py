from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from . models import footer,FAQ,Partner,NewsletterSubscriber,Turnaments,Leaderboard,ContactMessage,CustomUser,SocialMediaLinks,how_it_works,TournamentEnrollment,Badge,WhyJoinUs,CTA
# Register your models here.

@admin.register(footer)
class FooterAdmin(admin.ModelAdmin):
    # Disable the "Add" button by overriding `has_add_permission`
    def has_add_permission(self, request):
        # If there's already an instance, return False to disable the "Add" button
        if footer.objects.exists():
            return False
        return True
    
    
@admin.register(how_it_works)
class FooterAdmin(admin.ModelAdmin):
    # Disable the "Add" button by overriding `has_add_permission`
    def has_add_permission(self, request):
        # If there's already an instance, return False to disable the "Add" button
        if how_it_works.objects.exists():
            return False
        return True
    
@admin.register(CTA)
class FooterAdmin(admin.ModelAdmin):
    # Disable the "Add" button by overriding `has_add_permission`
    def has_add_permission(self, request):
        # If there's already an instance, return False to disable the "Add" button
        if CTA.objects.exists():
            return False
        return True

admin.site.register(FAQ)

admin.site.register(Partner)
@admin.register(Turnaments)
class TurnamentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'datetime', 'prize_pool', 'meta_title')
    prepopulated_fields = {"slug": ("name",)}
admin.site.register(ContactMessage)
admin.site.register(SocialMediaLinks)

@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_on')  # Specify fields to display
    search_fields = ('email',)  # Allow searching by email
    list_filter = ('subscribed_on',) 
    
    
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Customize as needed; this allows you to manage users in the admin
    list_display = ['username', 'email', 'fullname', 'mobile', 'city']
    

@admin.register(Leaderboard)
class LeaderboardAdmin(admin.ModelAdmin):
    list_display = ['game_name_with_date','first_place', 'second_place', 'third_place', 'first_prize', 'second_prize', 'third_prize']
    search_fields = ['game_name_with_date','first_place__username', 'second_place__username', 'third_place__username']
    
    
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'status')
    list_filter = ('user', 'title')

admin.site.register(Badge, BadgeAdmin)



class TournamentEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'tournament', 'enrolled_on', 'in_top_three', 'win','placement')  # Include the 'win' field
    list_filter = ('in_top_three', 'win','placement')  # Add filters for 'win' and 'in_top_three'

admin.site.register(TournamentEnrollment, TournamentEnrollmentAdmin)



admin.site.register(WhyJoinUs)