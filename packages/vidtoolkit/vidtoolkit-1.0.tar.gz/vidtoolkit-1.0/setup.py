from setuptools import setup, find_packages

setup(
    name='vidtoolkit',
    version='1.0',
    author='Ali Miracle',
    author_email='alimiracle@riseup.net',
    description='A comprehensive toolkit for video processing, including subtitles, watermarks, trimming, thumbnails, and MP4 to HLS conversion.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://notabug.org/alimiracle/vidtoolkit',
    packages=find_packages(),
    install_requires=[
        'moviepy',
        'imageio',
        'Pillow',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
