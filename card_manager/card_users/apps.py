from django.apps import AppConfig


class CardUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'card_users'

    def ready(self) -> None:
        import card_users.signals
