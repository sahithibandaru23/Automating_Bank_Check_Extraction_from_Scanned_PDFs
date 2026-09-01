import os
import io
import fitz  # PyMuPDF
from PIL import Image

def parse_pdf(file_path, output_folder, fixed_width, fixed_height):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the PDF file
    pdf_document = fitz.open(file_path)
    num_pages = pdf_document.page_count

    for page_num in range(num_pages):
        page = pdf_document.load_page(page_num)
        images = page.get_images(full=True)

        print(f"Page {page_num + 1}:")
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]

            # Debug: Print the type and size of the image stream
            print(f"Image {img_index + 1}: xref={xref}, size={len(image_bytes)} bytes")

            try:
                # Open the image stream with Pillow
                image_pil = Image.open(io.BytesIO(image_bytes))

                # Resize the image
                resized_image = image_pil.resize((fixed_width, fixed_height), Image.Resampling.LANCZOS)

                # Save the resized image
                image_path = os.path.join(output_folder, f"page_{page_num + 1}_image{img_index + 1}.png")
                resized_image.save(image_path)
                print(f"Saved resized image to {image_path}")
            except Exception as e:
                print(f"Error processing image {img_index + 1} on page {page_num + 1}: {e}")

# Example usage
file_path = r"cheque24.pdf"
output_folder = r"cheque_img"
fixed_width = 1000
fixed_height = 600

parse_pdf(file_path, output_folder, fixed_width, fixed_height)
