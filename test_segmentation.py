from src.flow.applications.image_seg import segment_simple_image

def test_vision():
    # A "row" of pixels: Dark, Dark, Light, Light, Dark
    pixels = [10, 20, 230, 240, 15] 
    
    result = segment_simple_image(pixels)
    
    print("--- Part 2: Image Segmentation Application ---")
    print(f"Original Intensities: {pixels}")
    print(f"Segmented Result:     {result}")

if __name__ == "__main__":
    test_vision()