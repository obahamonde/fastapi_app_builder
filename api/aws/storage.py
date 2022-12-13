from boto3 import Session
from api.typed import *

class Aws(Session):
    def __init__(self):
        super().__init__(
            aws_access_key_id=env.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
            region_name=env.AWS_REGION
        )

    @property
    def s3(self):
        return self.client("s3")

    @property
    def ses(self):
        return self.client("ses")
    
class S3Resource(APIRouter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.s3 = Aws().s3
        
        @self.post('/upload')
        async def upload_file(key: str, file: UploadFile = File(...)):
            """Uploads file to bucket"""
            try:
                self.s3.put_object(
                    Bucket=env.AWS_S3_BUCKET,
                    Key=key,
                    Body=await file.read(),
                    ContentType=file.content_type,
                    ACL="public-read"
                )
                return PlainTextResponse(f"https://s3.amazonaws.com/{env.AWS_S3_BUCKET}/{key}")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        @self.get('/upload')
        async def list_uploads(key: str):
            """Lists uploads"""
            try:
                response = self.s3.list_objects_v2(
                    Bucket=env.AWS_S3_BUCKET,
                    Prefix=key
                )
                return [f"https://s3.amazonaws.com/{env.AWS_S3_BUCKET}/{obj['Key']}" for obj in response["Contents"]]
            except Exception as e:
                return []

        @self.delete('/upload')
        async def delete_upload(key: str):
            """Deletes upload"""
            try:
                self.s3.delete_object(
                    Bucket=env.AWS_S3_BUCKET,
                    Key=key
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

