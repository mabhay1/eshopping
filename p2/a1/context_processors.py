from .models import UserProfile,CartVariable
def func1(request):
    try:
        user_profile=UserProfile.objects.get(username=request.user.username)
        cart7=CartVariable.objects.get_or_create(user_id=user_profile.user_ptr_id)[0]
        return {'qty':cart7.total_qty}
    except:
        return {'qty':0}    