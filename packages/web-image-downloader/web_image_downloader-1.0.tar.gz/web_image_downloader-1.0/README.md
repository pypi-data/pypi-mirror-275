# Web Image Downloader

A Python package to download images from web pages using the `web_assets_downloader` package.

## Installation

```bash
pip install web_image_downloader
```

## Usage
### With command line
```commandline
download_images https://example.com --save-folder ./downloaded
```
### As Python module
```python
import web_image_downloader

urls = ['https://example.com']
save_folder = './downloaded'
web_image_downloader.download_images(urls, save_folder)
```