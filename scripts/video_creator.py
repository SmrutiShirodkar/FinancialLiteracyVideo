import os
import numpy as np
import skvideo.io
from summarizer import summarize_article
from keyword_extractor import extract_keywords
from image_downloader import download_images
from overlay_text import overlay_text_on_image

def create_video(input_path, output_path):
    """
    Creates a video by summarizing text, downloading relevant images,
    overlaying text, and stitching frames.
    """
    with open(input_path, 'r') as file:
        article = file.read()

    summary = summarize_article(article)
    keywords, sentences = extract_keywords(summary)
    download_images(keywords)

    frames = []
    for keyword, sentence in zip(keywords, sentences):
        image_path = f"images/downloaded/{keyword}/1.jpg"
        if os.path.exists(image_path):
            frame = overlay_text_on_image(image_path, sentence)
            frames.extend([frame] * 30)  # Add each frame for 1 second (30 FPS)

    skvideo.io.vwrite(output_path, np.array(frames, dtype=np.uint8))
    print(f"Video created at: {output_path}")

if __name__ == "__main__":
    create_video("data/input.txt", "output/video.mp4")
