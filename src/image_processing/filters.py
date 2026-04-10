from image_processing.transforms import ImageTransforms

class ImageFilters:
    @staticmethod
    def apply_mask(matrix, mask_func):
        """Helper to apply a frequency-domain mask to an image."""
        # 1. Move to frequency domain
        freqs = ImageTransforms.fft2d(matrix)
        h, w = len(freqs), len(freqs[0])
        
        # 2. Apply the mask
        for y in range(h):
            for x in range(w):
                # Calculate distance from the 'corners' (low frequencies)
                # Note: This is a simplified version for small images
                freqs[y][x] *= mask_func(x, y, w, h)
        
        # 3. Move back to spatial domain
        return ImageTransforms.ifft2d(freqs)

    @staticmethod
    def low_pass(matrix, radius=0.2):
        """Blurs the image by removing high-frequency details."""
        def mask(x, y, w, h):
            # Centered distance logic for simplicity
            dist = ((x/w - 0.5)**2 + (y/h - 0.5)**2)**0.5
            return 1.0 if dist <= radius else 0.0
        return ImageFilters.apply_mask(matrix, mask)

    @staticmethod
    def compress(matrix, threshold=0.1):
        """Basic JPEG-style compression by zeroing out small coefficients."""
        freqs = ImageTransforms.fft2d(matrix)
        # Find the max magnitude to set a relative threshold
        max_mag = max(max(abs(val) for val in row) for row in freqs)
        
        compressed_freqs = []
        for row in freqs:
            new_row = [val if abs(val) > max_mag * threshold else 0j for val in row]
            compressed_freqs.append(new_row)
            
        return ImageTransforms.ifft2d(compressed_freqs)