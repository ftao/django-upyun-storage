=====================
django-upyun-storage
=====================

Upyun storage backend for Django pluggable storage system



Usage 
=====================

settings
---------------------

``UPYUN_BUCKET_NAME``

Your upyun bucket name 

``UPYUN_OPERATOR_NAME``

Operator name for your upyun bucket 

``UPYUN_OPERATOR_PASSWORD``

Operator password for your upyun bucket 


``DEFAULT_FILE_STORAGE``

If you want to make upyun storage as your default file storage .

    DEFAULT_FILE_STORAGE = 'upyunstorage.backends.upyun.UpYunStorage'

