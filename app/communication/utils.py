from oscar.apps.communication.utils import *


class Dispatcher(Dispatcher):
    def send_user_email_messages(self, user, messages, attachments=None):
        """
        Send message to the registered user / customer and collect data in database.
        """
        if not user.email:
            self.logger.warning("Unable to send email messages as user #%d has"
                                " no email address", user.id)
            return None

        # email = self.send_email_messages(user.email, messages, attachments=attachments)

        # if settings.OSCAR_SAVE_SENT_EMAILS_TO_DB:
        #     self.create_email(user, messages, email)

        # return email

        return None
