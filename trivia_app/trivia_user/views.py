from trivia_user.mixins import UserMixin
from trivia_user.models import User


class UserViewSet(UserMixin):
    queryset = User.objects.all()
