from setuptools import setup, find_packages
import upyunstorage

setup(
    name = 'django-upyun-storage',
    version = upyunstorage.__version__,
    packages = find_packages(),

    author = 'Fei Tao',
    author_email = 'filia.tao@gmail.com',
    license = 'BSD',
    description = 'Upyun storage backend for Django pluggable storage system',
    url='https://github.com/ftao/django-upyun-storage',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    #test_suite='tests.main',
    zip_safe = False,
)
