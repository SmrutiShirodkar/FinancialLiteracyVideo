from google_images_download import google_images_download

def download_images(keywords):
    """
    Downloads images for a list of keywords.
    """
    response = google_images_download.googleimagesdownload()
    for keyword in keywords:
        arguments = {"keywords": keyword, "limit": 1, "print_urls": False}
        response.download(arguments)
