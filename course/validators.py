import re

from rest_framework.exceptions import ValidationError


class UrlValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        reg = re.compile(r'^(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/')
        video_url = dict(value).get(self.field)
        if not bool(reg.match(video_url)):
            raise ValidationError('Url is not ok')