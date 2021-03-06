from django.contrib import admin

from apps.line_app.models import LineChannel, LineUserProfile, LineChannelMembership


@admin.register(LineChannel)
class LineChannelAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'line_bot_callback_uri',
        'bot_id',
        'numeric_id',
    )
    readonly_fields = ['id']
    date_hierarchy = 'created_at'


@admin.register(LineUserProfile)
class LineUserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'line_user_id',
        'name',
        'line_username_id',
        'language',
    )
    date_hierarchy = 'created_at'

@admin.register(LineChannelMembership)
class LineChannelMembershipAdmin(admin.ModelAdmin):
    list_display = (
        'line_user_profile',
        'line_channel',
        'is_staff',
    )
    date_hierarchy = 'created_at'
