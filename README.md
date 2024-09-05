# DJANGO ACCOUNTS APP
A basic accounts app with login and logout functionlity wired up using django's default stuff.

Steps:
1. Clone it.
2. Copy the accounts directory to your project's directory.
3. Include in installed apps list in settings.py and project's urls.py.
4. Add following to settings.py:  `AUTH_USER_MODEL = 'accounts.User'`  `LOGIN_URL = '/accounts/log-in/'`  `CRISPY_TEMPLATE_PACK = 'bootstrap4'`

Dependencies:
- Django, obviously.
- django-crispy-forms
- crispy-bootstrap4

Urls:
- log-in/ - login page.
- log-out/ - logout.
- update/ - edit profile.
- change-password/ - update password.
