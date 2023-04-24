from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email, phone, password, **kwargs):
        if not email:
            raise ValueError("Email is required")

        email = self.normalize_email(email) # приводим в правильный вид email
        # self.model == User
        user = self.model(email=email, phone=phone, **kwargs) # создаем обьект от класса User (его пока нет в бд)
        user.set_password(password) # хеширует пароль
        user.save(using=self._db) # сохраняем в бд
        return user

    def create_superuser(self, email, password, phone, **kwargs):
        if not email:
            raise ValueError("Email is required")

        kwargs['is_staff'] = True #даем права суперадмина
        kwargs['is_superuser'] = True
        kwargs['is_active'] = True

        email = self.normalize_email(email)
        user = self.model(email=email, phone=phone, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    username = None # убираем username из полей
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=50)
    bio = models.TextField()

    USERNAME_FIELD = 'email' #указываем какое поле использовать при логине
    REQUIRED_FIELDS = ['phone']

    objects = UserManager() # указываем нового менеджера
