from setuptools import setup

from oioswift import __version__


setup(
    name='oioswift',
    version=__version__,
    author='OpenIO',
    author_email='support@openio.io',
    description='OpenIO Swift Gateway',
    url='https://github.com/open-io/oio-swift',
    license='Apache License (2.0)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 2.7',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
    ],
    packages=[
        'oioswift',
        'oioswift.common',
        'oioswift.common.middleware',
        'oioswift.proxy',
        'oioswift.proxy.controllers'],
    entry_points={
        'paste.app_factory': [
            'main=oioswift.server:app_factory',
        ],
        'paste.filter_factory': [
            'autocontainer=oioswift.autocontainer:filter_factory',
            'hashedcontainer=oioswift.hashedcontainer:filter_factory',
            'versioned_writes=oioswift.common.middleware.versioned_writes:filter_factory',
        ],
    },
    install_requires=['swift>=2.10.0', 'oio>=3.3.0']
)
