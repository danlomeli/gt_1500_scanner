import logging
from PIL import Image
import pytesseract
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.utils import ImageReader

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_searchable_pdf(image_path, output_pdf_path):
    try:
        # Open the image file
        logging.info(f"Opening image file: {image_path}")
        image = Image.open(image_path)

        # Perform OCR on the image
        logging.info("Performing OCR on the image")
        text = pytesseract.image_to_string(image)

        # Create a PDF with the image
        logging.info(f"Creating PDF: {output_pdf_path}")
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        c.drawImage(ImageReader(image), 0, 0, width=letter[0], height=letter[1])

        # Add the text layer
        logging.info("Adding text layer to PDF")
        c.setFont("Helvetica", 10)
        c.setFillColorRGB(1, 1, 1, alpha=0)  # Invisible text
        text_lines = text.split('\n')
        y = letter[1] - 10
        for line in text_lines:
            c.drawString(10, y, line)
            y -= 12

        c.save()
        logging.info("PDF creation completed successfully")
    except IOError as e:
        logging.error(f"Error opening image file: {e}")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    create_searchable_pdf('path_to_your_scanned_image_file.png', 'output_searchable.pdf')
