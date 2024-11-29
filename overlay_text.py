import cv2

def overlay_text_on_image(image_path, text):
    """
    Overlays text on the provided image.
    """
    img = cv2.imread(image_path)
    img = cv2.resize(img, (800, 800))
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_color = (255, 255, 255)
    thickness = 2
    y_offset = 750

    for line in text.splitlines():
        cv2.putText(img, line, (10, y_offset), font, 1, font_color, thickness, cv2.LINE_AA)
        y_offset -= 30

    return img
