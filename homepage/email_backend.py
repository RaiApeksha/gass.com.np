import ssl
import certifi
from django.core.mail.backends.smtp import EmailBackend

class SecureEmailBackend(EmailBackend):
    def open(self):
        if self.connection:
            return False

        connection_class = self.connection_class
        try:
            self.connection = connection_class(
                self.host, self.port, timeout=self.timeout
            )

            context = ssl.create_default_context()
            context.load_verify_locations(cafile=certifi.where())

            self.connection.starttls(context=context)
            self.connection.login(self.username, self.password)
            return True
        except Exception as e:
            if self.fail_silently:
                return False
            raise e
