import falcon

from falcon_helpers.config import Config
from falcon_helpers.middlewares import multi as multimw


class App(falcon.App):
    __slots__ = (
        'config',
        'plugins',
        '_dynmw',
        'enable_dynamic_mw',
        '_initialized',
    )

    def __init__(self, middleware=None, enable_dynamic_mw=True, independent_middleware=True,
                 **kwargs):

        if enable_dynamic_mw and not independent_middleware:
            raise RuntimeError(
                f'Independent middleware must be enabled to use dynamic middleware. Either turn '
                'off dynamic middleware (enable_dynamic_mw=False) or enable independent middleware '
                '(independent_middleware=True).'
            )
        elif enable_dynamic_mw:
            self._dynmw = multimw.MultiMiddleware(middleware)
            kwargs['middleware'] = [self._dynmw]
            kwargs['independent_middleware'] = True
        else:
            kwargs['middleware'] = middleware

        self._initialized = False
        self.plugins = {}

        super().__init__(**kwargs)

        self._initialized = True

    def add_middleware(self, mw):
        if self._initialized and hasattr(self, '_dynmw'):
            self._dynmw.add_middleware(mw)
        else:
            super().add_middleware(mw)

    @classmethod
    def from_inis(cls, *paths, app_kwargs=None):
        """Create an instance of the app from configuration files"""

        app = cls(**(app_kwargs or {}))

        app.config = Config.from_inis(*paths)

        return app
