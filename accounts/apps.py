from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'

    #after creating signals , then do it
    def ready(self):
        import accounts.signals
