"""Tracing extension for Flask."""

import logging

logger = logging.getLogger("impact_stack.observability")


class Tracing:
    """Tracing extension."""

    # pylint: disable=too-few-public-methods

    def __init__(self, app=None):
        """Initialize the extension."""
        self.resource = None
        self.tracer_provider = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Initialize a Flask application for use with this extension instance."""
        if "tracing" in app.extensions:
            raise RuntimeError(
                "A 'Tracing' instance has already been registered on this Flask app."
            )
        app.extensions["tracing"] = self
