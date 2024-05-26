from traceback import TracebackException

from django.core.mail.backends.smtp import EmailBackend as EmailBackendBase
from opentelemetry import trace

tracer = trace.get_tracer(__name__)


class EmailBackend(EmailBackendBase):
    """
    A wrapper that instruments the default
    `django.core.mail.backends.smtp.EmailBackend`
    with open-telemetry.
    """

    def open(self) -> bool:
        with tracer.start_as_current_span("open"):
            span = trace.get_current_span()

            already_connected = bool(self.connection)

            span.set_attribute("fail_silently", self.fail_silently)
            span.set_attribute("connection_already_open", already_connected)
            span.set_attribute("raised", False)
            span.set_attribute("stack", None)

            try:
                opened = super().open()
                span.set_attribute("connection_opened", opened)
            except OSError as e:
                opened = False
                span.set_attribute("connection_opened", opened)

                if not self.fail_silently:
                    span.set_attribute("raised", True)
                    span.set_attribute(
                        "stack", "".join(TracebackException.from_exception(e).format())
                    )
                    raise e

            return opened
