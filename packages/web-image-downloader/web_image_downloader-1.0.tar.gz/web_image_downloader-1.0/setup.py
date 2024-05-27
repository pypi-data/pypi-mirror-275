from setuptools import setup, find_packages

setup(
    name='web_image_downloader',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'web-assets-downloader'
    ],
    entry_points={
        'console_scripts': [
            'download_images=web_image_downloader.downloader:main'
        ]
    },
    author='Ariffudin',
    author_email='sudo.ariffudin@gmail.com',
    description='A package to download images from the web using web_assets_downloader.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arif-x/web-image-downloader',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    dependency_links=[
        'git+https://github.com/arif-x/web-image-downloader.git'
    ],
    project_urls={
        'Source': 'https://github.com/arif-x/web-image-downloader',
        'Source Code': 'https://github.com/arif-x/web-image-downloader'
    }
)
