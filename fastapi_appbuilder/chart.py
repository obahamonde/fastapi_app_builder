from fastapi_appbuilder.typed import *
from prisma.models import ApiReq

class Chart(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = '/chart'

        @self.get('/')
        async def chart():
            status_200 = await ApiReq.prisma().find_many(where={'status': {'gte': 200,'lte': 299}, 'createdAt': {'gte': datetime.now() - timedelta(days=1)}}, order={'createdAt': 'desc'})
            status_300 = await ApiReq.prisma().find_many(where={'status': {'gte': 300,'lte': 399}, 'createdAt': {'gte': datetime.now() - timedelta(days=1)}}, order={'createdAt': 'desc'})
            status_400 = await ApiReq.prisma().find_many(where={'status': {'gte': 400,'lte': 499}, 'createdAt': {'gte': datetime.now() - timedelta(days=1)}}, order={'createdAt': 'desc'})
            status_500 = await ApiReq.prisma().find_many(where={'status': {'gte': 500,'lte': 599}, 'createdAt': {'gte': datetime.now() - timedelta(days=1)}}, order={'createdAt': 'desc'})
            return {
                'ok': {'count': len(status_200),'data': status_200},
                'redirect': {'count': len(status_300),'data': status_300},
                'clienterror': {'count': len(status_400),'data': status_400},
                'servererror': {'count': len(status_500),'data': status_500}
            }