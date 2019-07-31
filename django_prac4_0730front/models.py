from django.db import models


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # 자동으로 디비에 인스턴스 들어간 상황을 체크해서 데잇타임 만드는 속성

    # 타임 스탬프, 타임 마킹용, 용도가 다양하니 별도의 클래스로 뺀다
    # 별도의 디렉토리로도 빼면 헷갈릴 일을 줄일 수 있드

    class Meta:
        abstract = True  # 추상화