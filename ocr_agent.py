from PIL import Image
import pytesseract
import os

class OCRParserAgent:
    def __init__(self):
        # You can customize the tesseract path if needed
        self.tesseract_cmd = 'tesseract'

    def extract_text_from_image(self, image_path):
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image not found at {image_path}")
        
        print(f"🔍 Extracting text from: {image_path}")
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()


# === Quick Test ===
if __name__ == "__main__":
    parser = OCRParserAgent()
    text = parser.extract_text_from_image("images/Sample_1.png")  # your image file name
    print("\n📝 Extracted Text:\n")
    print(text)
