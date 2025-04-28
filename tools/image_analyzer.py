def analyze_image(image):
    if image is None:
        print("[Image Analyzer] No image to analyze.")
        return None

    # For now, just simulate analysis by checking image size
    width, height = image.size
    print(f"[Image Analyzer] Image size - Width: {width}, Height: {height}")

    if width * height < 50000:
        return "small"
    elif width * height < 150000:
        return "medium"
    else:
        return "large"