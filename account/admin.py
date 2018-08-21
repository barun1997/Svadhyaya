from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.utils.translation import ugettext_lazy as _
from account.models import CustomUser

@admin.register(CustomUser)

#We need to create a custom admin for the new Custom User Model we created

class UserAdmin(DjangoUserAdmin):

     fieldsets= (
     (None, {'fields': ('email', 'password')}),
     (_('Personal info'), {'fields': ('first_name', 'last_name')}),
     (_('Permissions'), {'fields': ('is_active', 'is_superuser', 'groups', 'user_permissions')}),
     )

     add_fieldsets= (
     (None, {
     'classes': ('wide', ),
     'fields': ('email', 'password1', 'password2'),
     }),
     )
     list_display = ('email', 'first_name', 'last_name', 'is_superuser')
     search_fields = ('email', 'first_name', 'last_name')
     ordering = ('email',)
'''

To learn about what I did here: https://www.fomfus.com/articles/how-to-use-email-as-username-for-django-authentication-removing-the-username#Register%20your%20new%20User%20model%20with%20Django%20admin '''
