from HeZe.models import User


def islog(UserPhone, SecretKey):
    try:
        u = User.objects.filter(UserPhone=UserPhone, SecretKey=SecretKey).first()
        if u:
            state = 1
            user = u
        else:
            state = 0
            user = None
    except Exception as e:
        state = 0
        user = None
        print(e)
    array = {
        'state': state,
        'user': user
    }
    return array