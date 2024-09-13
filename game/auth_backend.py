from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            # Try to fetch the user using the email field
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            return None
        
        # Check if the password is correct
        if user.check_password(password):
            return user
        return None
