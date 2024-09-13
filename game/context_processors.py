from .models import footer,FAQ,Partner,CTA

from .forms import NewsletterForm

def social_media_links(request):
    # Fetch the first (or only) social media links entry
    social_links = footer.objects.first()
    return {
        'social_links': social_links  # The key here will be available in all templates
    }
    
def faqs(request):
    return {
        'faqs': FAQ.objects.all()  # This will return all FAQs
    }
def partners(request):
    return {
        'partners': Partner.objects.all()
    }
def cta(request):
    return {
        'cta': CTA.objects.first()
    }


def newsletter_form(request):
    form = NewsletterForm()
    return {'newsletter_form': form}
