from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth import update_session_auth_hash
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from .forms import NewsletterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page
from django.utils import timezone 
from .models import footer, Turnaments, Leaderboard, ContactMessage, CustomUser, SocialMediaLinks,TournamentEnrollment,Badge,WhyJoinUs,how_it_works
# Home page view
 # 24 hours chaching
def home(request):
    why_join_us_items = WhyJoinUs.objects.all()
    how_work = how_it_works.objects.first()
    leaderboard = Leaderboard.objects.order_by('-id').first()
    
    return render(request, 'home.html', {'leaderboard': leaderboard,'why_join_us_items': why_join_us_items,'how_work':how_work})


# 24 hours chaching
def about(request):
    return render(request, 'aboutus.html')

# Leaderboard view

def leaderboard(request):
    leaderboard = Leaderboard.objects.order_by('-id').first()
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard})

# Tournaments view
def turnaments(request):
    turnaments = Turnaments.objects.all()
    return render(request, 'turnament.html', {'turnaments': turnaments})

# Contact page view

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Validate the form fields manually
        if not name or not email or not message:
            messages.error(request, 'All fields are required.')
        else:
            try:
                validate_email(email)  # Validate email format
            except ValidationError:
                messages.error(request, 'Please enter a valid email address.')
            else:
                ContactMessage.objects.create(name=name, email=email, message=message)
                messages.success(request, 'Your message has been sent successfully!')
                return redirect('contact')

    return render(request, 'contact.html')

# Tournament description view
def turnament_description(request, slug):
    tournament = get_object_or_404(Turnaments, slug=slug)
    now = timezone.now()
    has_started = tournament.datetime <= now

    # Check if the user is already enrolled
    if request.user.is_authenticated:
        is_enrolled = TournamentEnrollment.objects.filter(user=request.user, tournament=tournament).exists()
    else:
        is_enrolled = False

    return render(request, 'turnament_description.html', {
        'turnament': tournament,
        'has_started': has_started,
        'is_enrolled': is_enrolled
    })

# Newsletter signup view
def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
        else:
            messages.error(request, "There was a problem with your submission.")
    return redirect(request.META.get('HTTP_REFERER', 'home')) 

# Login page view

def login_user(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate the user using email
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home or any other page
        else:
            messages.error(request, 'Invalid email or password.')  # Error message for invalid credentials

    return render(request, 'registeration_login/login.html')

# User registration view


def register(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        email = request.POST['email']
        mobile = request.POST['mobile']
        username = request.POST['username']
        password = request.POST['password']
        city = request.POST['city']

        # Check for existing users
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'registeration_login/register.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email is already registered.')
            return render(request, 'registeration_login/register.html')

        if CustomUser.objects.filter(mobile=mobile).exists():
            messages.error(request, 'Mobile number is already registered.')
            return render(request, 'registeration_login/register.html')

        # Create new user
        user = CustomUser.objects.create_user(
            email=email,
            username=username,
            fullname=fullname,
            mobile=mobile,
            city=city,
            password=password
        )
        user.save()

        login(request, user)  # Log the user in after registration
        messages.success(request, "Your account has been created successfully!")
        return redirect('home')
    
    return render(request, 'registeration_login/register.html')

# Profile update view

@login_required
def profile_update_view(request):
    
    user = request.user
    enrollments = TournamentEnrollment.objects.filter(user=user).select_related('tournament')
    # Fetch badges for the user
    badges = Badge.objects.filter(user=user)
    now = timezone.now()
    if request.method == 'POST':
        # Update user profile information
        user.username = request.POST.get('username')
        user.fullname = request.POST.get('fullname')
        user.email = request.POST.get('email')
        user.mobile = request.POST.get('mobile')
        user.city = request.POST.get('city')

        # Update profile image if provided
        if request.FILES.get('profile_image'):
            user.profile_image = request.FILES.get('profile_image')

        # Update password if provided
        password = request.POST.get('password')
        if password:
            user.set_password(password)

        user.save()  # Save the user profile changes

        # Keep the user logged in if password is changed
        if password:
            update_session_auth_hash(request, user)

        messages.success(request, 'Profile updated successfully!')
        return redirect('profile_update')

    # Fetch user's social media links
    social_links, _ = SocialMediaLinks.objects.get_or_create(user=user)

    return render(request, 'user/profile.html', {'user': user, 'social_links': social_links,'enrollments': enrollments,'badges': badges,'now': now })

# Social media links update view
@login_required
def social_links_update_view(request):
    user = request.user

    # Ensure the user has a SocialMediaLinks instance, create one if not
    social_links, created = SocialMediaLinks.objects.get_or_create(user=user)
    

    if request.method == 'POST':
        # Debugging: Print request.POST to see if the form is sending data
        print(request.POST)

        # Update social media links
        social_links.facebook = request.POST.get('facebook')
        social_links.instagram = request.POST.get('instagram')
        social_links.twitter = request.POST.get('twitter')
        social_links.youtube = request.POST.get('youtube')

        # Save the social media links
        social_links.save()

        messages.success(request, 'Social media links updated successfully!')
        return redirect('profile_update')

    # If GET request, just render the template
    return render(request, 'user/profile.html', {'user': user, 'social_links': social_links})




def user_report(request, username):
    # Fetch the user by their username
    profile_user = get_object_or_404(CustomUser, username=username)

    # Fetch the user's social media links (assuming a one-to-one relationship)
    social_links, created = SocialMediaLinks.objects.get_or_create(user=profile_user)
    
    badges = Badge.objects.filter(user=profile_user)

    # Get all tournaments the user has enrolled in
    tournament_enrollments = TournamentEnrollment.objects.filter(user=profile_user).select_related('tournament')

    # Calculate total tournaments, wins (top 3), and losses
    total_tournaments = tournament_enrollments.count()
    total_wins = tournament_enrollments.filter(win='win').count()
    total_losses = tournament_enrollments.filter(win='loss').count()
    # Calculate total earnings based on placement
    total_earnings = 0
    for enrollment in tournament_enrollments:
        if enrollment.placement == 1:
            total_earnings += enrollment.tournament.prize_1
        elif enrollment.placement == 2:
            total_earnings += enrollment.tournament.prize_2
        elif enrollment.placement == 3:
            total_earnings += enrollment.tournament.prize_3
        else:
            total_earnings = total_earnings + 0
    # Render the report page with the user's information
    return render(request, 'user/report.html', {
        'profile_user': profile_user,
        'social_links': social_links,
        'tournament_enrollments': tournament_enrollments,
        'total_tournaments': total_tournaments,
        'total_wins': total_wins,
        'total_losses': total_losses,
        'badges': badges,
        'total_earnings': total_earnings
    })
    
    
    

def custom_404_view(request, exception):
    return render(request, 'errors/404.html', {}, status=404)

def custom_500_view(request):
    return render(request, 'errors/500.html', {}, status=500)


def custom_400_view(request, exception):
    return render(request, 'errors/400.html', status=400)


# legal 

def privacy(request ):
    return render(request, 'legal/privacy.html',)


def terms_conditon(request ):
    return render(request, 'legal/terms_condition.html',)


def cancellation(request ):
    return render(request, 'legal/cancellation_refund.html',)




@login_required
def join_tournament(request, tournament_id):
    tournament = get_object_or_404(Turnaments, id=tournament_id)

    # Check if the user is already enrolled
    if TournamentEnrollment.objects.filter(user=request.user, tournament=tournament).exists():
        messages.info(request, 'You are already enrolled in this tournament!')
    else:
        # Enroll the user
        TournamentEnrollment.objects.create(user=request.user, tournament=tournament)
        messages.success(request, 'You have successfully enrolled in the tournament!')

    return redirect('turnament_description', slug=tournament.slug)


@login_required
def game_paas(request):
    if request.user.is_authenticated:
        # Get all tournaments the current user is enrolled in
        enrollments = TournamentEnrollment.objects.filter(user=request.user).select_related('tournament')
        enrolled_tournaments = [enrollment.tournament for enrollment in enrollments]
    else:
        enrolled_tournaments = []

    return render(request, 'user/game_paas.html', {'enrolled_tournaments': enrolled_tournaments})
