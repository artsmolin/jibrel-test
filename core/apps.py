from django.apps import AppConfig


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        print('App ready:', self.name)

        from core.services import currensy_updater

        # В реальном проекте это вынеслись бы в отдельную команду, вызывающуюся при деплое.
        # А пока здесь, при старте приложения (для удобства тестирования).
        if currensy_updater.is_need_to_update():
            currensy_updater.update()
