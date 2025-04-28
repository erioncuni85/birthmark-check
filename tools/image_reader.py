from PIL import Image

def read_image(image_path):
    try:
        image = Image.open(image_path)
        print(f"[Image Reader] Successfully loaded image: {image_path}")
        return image
    except Exception as e:
        print(f"[Image Reader] Failed to load image: {e}")
        return None