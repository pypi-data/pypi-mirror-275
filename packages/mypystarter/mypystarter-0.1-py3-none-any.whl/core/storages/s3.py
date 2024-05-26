import os

from django.conf import settings
from django.utils.encoding import filepath_to_uri
from storages.backends.s3boto3 import S3Boto3Storage
from storages.utils import clean_name, is_seekable, ReadBytesWrapper


class S3Storage(S3Boto3Storage):
    ACL = None
    bucket_name = None
    region_name = None
    endpoint_url = None
    prefix = None

    def get_default_settings(self):
        params = super().get_default_settings()
        params['bucket_name'] = self.bucket_name
        params['region_name'] = self.region_name
        params['endpoint_url'] = self.endpoint_url
        if self.ACL:
            params['ACL'] = self.ACL
        return params

    def get_save_key(self, name):
        return name

    def _save(self, name, content):
        cleaned_name = clean_name(name)
        name = self._normalize_name(cleaned_name)
        params = self._get_write_parameters(name, content)

        if is_seekable(content):
            content.seek(0, os.SEEK_SET)

        # wrap content so read() always returns bytes. This is required for passing it
        # to obj.upload_fileobj() or self._compress_content()
        content = ReadBytesWrapper(content)

        if (
                self.gzip
                and params["ContentType"] in self.gzip_content_types
                and "ContentEncoding" not in params
        ):
            content = self._compress_content(content)
            params["ContentEncoding"] = "gzip"

        # Workaround file being closed errantly see: https://github.com/boto/s3transfer/issues/80
        original_close = content.close
        content.close = lambda: None
        try:
            self.bucket.put_object(
                Key=self.get_save_key(name),
                Body=content,
            )
        finally:
            content.close = original_close
        return cleaned_name


class S3PublicStorage(S3Storage):
    bucket_name = settings.AWS_PUBLIC_STORAGE_BUCKET_NAME
    region_name = settings.AWS_PUBLIC_STORAGE_REGION
    endpoint_url = settings.AWS_PUBLIC_STORAGE_ENDPOINT_URL
    ACL = 'public-read'
    prefix = 'public'

    def get_save_key(self, name):
        return f"{self.prefix}/{name}"

    def url(self, name, parameters=None, expire=None, http_method=None):
        # Preserve the trailing slash after normalizing the path.
        name = self._normalize_name(clean_name(name))
        url = "{}{}{}".format(
            settings.AWS_PUBLIC_STORAGE_SERVE_URL,
            f'/{self.prefix}/',
            filepath_to_uri(name),
        )
        return url


class S3StaticStorage(S3PublicStorage):
    prefix = 'static'


class S3PrivateStorage(S3Storage):
    bucket_name = settings.AWS_PRIVATE_STORAGE_BUCKET_NAME
    region_name = settings.AWS_PRIVATE_STORAGE_REGION
    endpoint_url = settings.AWS_PRIVATE_STORAGE_ENDPOINT_URL
    querystring_expire = settings.AWS_QUERYSTRING_EXPIRE

    def url(self, name, parameters=None, expire=None, http_method=None):
        if expire is None:
            expire = self.querystring_expire
        return super().url(name, parameters, expire, http_method)
