import mimetypes
from email.mime.image import MIMEImage
from pathlib import Path
from typing import IO

from django.core.mail import EmailMultiAlternatives as DjangoEmailMultiAlternatives
from PIL import Image


class EmailMultiAlternatives(DjangoEmailMultiAlternatives):
    def __init__(self, *args, **kwargs):
        """
        Extension of django's EmailMultiAlternatives supporting the following extra parameters: metadata, send_at,
        unique_hash and force_send

        @param metadata: a dict where each value is either a scalar (int, str, etc) or a list of scalars.
        @param send_at: date when to actually send the email.
        @param force_send: boolean indicating if email should be send even if it was already sent before
        @param unique_hash: string containing unique hash for duplicates detection
        """
        self.metadata = kwargs.pop('metadata', dict())
        self.send_at = kwargs.pop('send_at', None)
        self.force_send = kwargs.pop('force_send', False)
        self.unique_hash = kwargs.pop('unique_hash', None)

        super(EmailMultiAlternatives, self).__init__(*args, **kwargs)

    def attach_inline_image(self, filepath: str, cid: str) -> None:
        if not Path(filepath).exists():
            # TODO: shouldn't we raise something?
            return
        with Path(filepath).open(mode='rb') as fp:
            image_data = fp.read()
            image = Image.open(fp)
            _, mime_format = image.get_format_mimetype().split('/')
            msg_img = MIMEImage(image_data, _subtype=mime_format)
            msg_img.add_header('Content-ID', '<{}>'.format(cid))
            self.attach(msg_img)

    def add_image(self, directory: str, filename: str, alias: str) -> None:
        '''
        Wrapper for backward-compat with notification.models.EmailMultiAlternativesWithImages
        '''
        filepath = Path(directory, filename)
        self.attach_inline_image(filepath.as_posix(), alias)

    def add_attachment(self, _file: IO) -> None:
        content_type, encoding = mimetypes.guess_type(_file.name)
        self.attach(Path(_file.name).name, _file.read(), content_type)
