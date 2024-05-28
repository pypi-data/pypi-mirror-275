"""Abstract base class for email composers."""

from abc import ABCMeta, abstractmethod
from email.message import EmailMessage


class BaseEmail(metaclass=ABCMeta):
    """Generic email object that can generate an EmailMessage based on its contents."""

    def __init__(self, sender: str, subject: str):
        self.sender = sender
        self.subject = subject

    @abstractmethod
    def get_message(
        self,
        to: str | list[str],
        cc: str | list[str] | None = None,
        bcc: str | list[str] | None = None,
    ) -> EmailMessage:
        """Generate a message that can be sent using the SMTP.send_message method.

        Args:
            to: Address(es) of the email's intended recipient(s).
            cc: Address(es) to CC on the email.
            bcc: Address(es) to BCC on the email.
        """
        pass
