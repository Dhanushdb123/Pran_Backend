from django.contrib import admin

# # Register your models here.
class CustomAdminSite(admin.AdminSite):
    site_title = 'PranAdmin'  # Change this to your custom title
    site_header = 'PranAdmin'  # Change this to your custom header

# # Replace the default admin site with your custom admin site
# admin.site = CustomAdminSite(name='admin')