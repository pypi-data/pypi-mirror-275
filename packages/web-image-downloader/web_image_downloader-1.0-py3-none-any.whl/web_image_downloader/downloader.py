from web_assets_downloader import download_html_and_asset

def download_images(url_list, save_folder, max_depth=None):
    download_html_and_asset(url_list, save_folder, max_depth, img=True, pdf=False, doc=False, xlx=False, html=False)

def main():
    import argparse

    parser = argparse.ArgumentParser(description='Download images from web pages.')
    parser.add_argument('urls', metavar='URL', type=str, nargs='+', help='URLs of the web pages to download images from')
    parser.add_argument('--save-folder', dest='save_folder', type=str, default='./downloaded', help='Folder to save the downloaded images')
    parser.add_argument('--max-depth', dest='max_depth', type=int, default=None, help='Max depth for following links (currently not implemented)')

    args = parser.parse_args()
    download_images(args.urls, args.save_folder, args.max_depth)

if __name__ == "__main__":
    main()
