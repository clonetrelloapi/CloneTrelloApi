from django.shortcuts import render
from .serializers import *
from .models import Title, Card
from rest_framework import generics
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

# 메인 관련 뷰
class MainListView(generics.ListAPIView):
    """
        Main 화면과 관련된 정보를 모두 불러옵니다.

        ---
        # 내용
            - id : 목록(List)의 고유 ID
            - title : 목록(List)의 제목
            - listSort : 목록(List)의 현재 순서
            - cards : 카드(Card) 리스트
                - title : 카드(Card)가 속한 리스트의 고유 ID
                - id : 카드(Card)의 고유 ID
                - cardTitle : 카드(Card)의 제목
                - description : 카드(Card)의 상세 내용
                - comments : 코멘트(comment) 리스트
                    - id : 코멘트(comment)의 고유 ID
                    - comment : 코멘트(comment) 내용
                    - card : 코멘트(comment)가 속한 카드의 고유 ID
                - cardSort : 카드(Card)의 현재 순서
    """
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = MainListSerializer

# 목록 관련 뷰(리스트[GET] 및 생성[CREATE])
class TitleListCreateView(generics.ListCreateAPIView):
    """
        목록(List) 리스트를 불러오거나 생성합니다.

        ---
        [GET]

        # 내용
            - id : 목록(List)의 고유 ID
            - title : 목록(List)의 제목
            - listSort : 목록(List)의 현재 순서
            - cards : 카드(Card) 리스트
                - title : 카드(Card)가 속한 리스트의 고유 ID
                - id : 카드(Card)의 고유 ID
                - cardTitle : 카드(Card)의 제목
                - description : 카드(Card)의 상세 내용
                - comments : 코멘트(comment) 리스트
                    - id : 코멘트(comment)의 고유 ID
                    - comment : 코멘트(comment) 내용
                    - card : 코멘트(comment)가 속한 카드의 고유 ID
                - cardSort : 카드(Card)의 현재 순서

        [CREATE]

        다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - title : "생성할 목록(List)의 제목"
            - listSort : "생성할 목록(List)의 순서"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - id : 생성된 목록(List)의 고유 ID
            - title : 생성된 목록(List)의 제목
            - listSort : 생성된 목록(List)의 순서
            - cards : [](처음 생성했을 경우 빈 쿼리로 리턴)
    """
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = MainListSerializer

# 리스트 디테일 관련 뷰(GET, PUT, PATCH, DELETE)
class TitleDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
         목록(List) 리스트에서 특정 id를 가지는 데이터를 불러오거나 수정, 삭제합니다.

        ---
        [GET]

        # 내용
            - title : 목록(List)의 제목
            - listSort : 목록(List)의 순서

        [PUT, PATCH]

        다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - title : "수정할 목록(List)의 제목"
            - listSort : "수정할 목록(List)의 순서"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - title : "수정된 목록(List)의 제목"
            - listSort : "수정된 목록(List)의 순서"

        [DELETE]

        특정 id로 요청하면 삭제됩니다.
    """
    renderer_classes = [JSONRenderer]
    queryset = Title.objects.all()
    serializer_class = TitleSerializer

# 카드 관련 뷰(리스트[GET] 및 생성[CREATE])
class CardListCreateView(generics.ListCreateAPIView):
    """
        카드(Card) 리스트를 불러오거나 생성합니다.

        ---
        [GET]

        # 내용
            - title : 카드(Card)가 속한 목록(List)의 고유 ID
            - id : 카드(Card)의 고유 ID
            - cardTitle : 카드(Card)의 제목
            - description : 카드(Card)의 상세 내용
            - comments : 카드(Card)의 코멘트(comment) 리스트
                - id : 코멘트(comment)의 고유 ID
                - comment : 코멘트(comment)의 내용
                - card : 코멘트(comment)가 속한 카드(Card)의 고유 ID
            - cardSort : 카드(Card)의 순서

        [CREATE]

        다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - title : "카드(Card)가 속할 목록(List)의 고유 ID"
            - cardTitle : "생성할 카드(Card)의 제목"
            - cardSort : "생성할 카드(Card)의 순서"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - title : 카드(Card)가 속한 목록(List)의 고유 ID
            - id : 생성된 카드(Card)의 고유 ID
            - cardTitle : 생성된 카드(Card)의 제목
            - description : 생성된 카드(Card)의 상세내용(처음 생성했을 경우 null)
            - comments : 생성된 카드(Card)의 코멘트(comment) 리스트(처음 생성했을 경우 빈 쿼리로 리턴)
            - cardSort : 생성된 카드(Card)의 순서
    """
    renderer_classes = [JSONRenderer]
    queryset = Card.objects.all()
    serializer_class = CardListSerializer

# 카드 디테일 관련 뷰(GET, PUT, PATCH, DELETE)
class CardDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        카드(Card) 리스트에서 특정 id를 가지는 데이터를 불러오거나 수정, 삭제합니다.

        ---
        [GET]

        # 내용
            - title : 카드(Card)가 속한 목록(List)의 고유 ID
            - cardTitle : 카드(Card)의 제목
            - description : 카드(Card)의 상세 내용
            - comments : 카드(Card)의 코멘트(comment) 리스트
                - id : 코멘트(comment)의 고유 ID
                - comment : 코멘트(comment)의 내용
                - card : 코멘트(comment)가 속한 카드(Card)의 고유 ID
            - cardSort : 카드(Card)의 순서

        [PUT, PATCH]

            다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - title : "카드(Card)가 속한 목록(List)의 고유 ID"
            - cardTitle : "수정할 카드(Card)의 제목"
            - description : "수정할 카드(Card)의 상세 내용"
            - cardSort : "수정할 카드(Card)의 순서"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - title : 수정한 카드(Card)가 속한 목록(List)의 고유 ID
            - cardTitle : 수정한 카드(Card)의 제목
            - description : 수정한 카드(Card)의 상세 내용
            - comments : 카드(Card)의 코멘트(comment) 리스트
                - id : 코멘트(comment)의 고유 ID
                - comment : 코멘트(comment)의 내용
                - card : 코멘트(comment)가 속한 카드(Card)의 고유 ID
            - cardSort : 수정한 카드(Card)의 순서

        [DELETE]

        특정 id로 요청하면 삭제됩니다.
    """
    renderer_classes = [JSONRenderer]
    queryset = Card.objects.all()
    serializer_class = CardSerializer

# 카드의 코멘트 생성 뷰(리스트[GET] 및 생성[CREATE])
class CommentsListCreateView(generics.ListCreateAPIView):
    """
        코멘트(comment) 리스트를 불러오거나 생성합니다.

        ---
        [GET]

        # 내용
            - id : 코멘트(comment)의 고유 ID
            - comment : 코멘트(comment)의 내용
            - card : 코멘트(comment)가 속한 카드(Card)의 고유 ID

        [CREATE]

        다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - comment : "생성할 코멘트(comment)의 내용"
            - card : "코멘트(comment)가 속한 카드(Card)의 고유 ID"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - id : 생성된 코멘트(comment)의 고유 ID
            - comment : 생성된 코멘트(comment)의 내용
            - card : 코멘트(comment)가 속한 카드(Card)의 고유 ID
    """
    renderer_classes = [JSONRenderer]
    queryset = Comments.objects.all()
    serializer_class = CommentsListSerializer

# 카드의 코멘트 디테일 뷰(GET, PUT, PATCH, DELETE)
class CommentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
        코멘트(comment) 리스트에서 특정 id를 가지는 데이터를 불러오거나 수정, 삭제합니다.

        ---
        [GET]

        # 내용
            - comment : 코멘트(comment)의 내용

        [PUT, PATCH]

            다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - comment : "수정할 코멘트(comment)의 내용"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - comment : 수정된 코멘트(comment)의 내용

        [DELETE]

        특정 id로 요청하면 삭제됩니다.
    """
    renderer_classes = [JSONRenderer]
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

# 트렐로 메인 배경 관련 뷰(GET, PUT, PATCH)
class BackgroundcolorDetailView(generics.RetrieveUpdateAPIView):
    """
        미리 등록해둔 배경화면(background) 데이터를 불러오거나 수정합니다.

        ---
        [GET]

        # 내용
            - id : 배경화면(background)의 고유 ID
            - background_color : 배경화면(background)의 RGB Code ex) #FFFFFF

        [PUT, PATCH]

        다음과 같은 내용으로 요청할 수 있습니다.

        # 내용
            - background_color : "배경화면(background)의 RGB Code"

        다음과 같은 내용으로 리턴됩니다.

        # 내용
            - background_color : 수정된 배경화면(background)의 RGB Code
    """
    renderer_classes = [JSONRenderer]
    queryset = Backgroundcolor.objects.all()
    serializer_class = BackgroundcolorSerializer

