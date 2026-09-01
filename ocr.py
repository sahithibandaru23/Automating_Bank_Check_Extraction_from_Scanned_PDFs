import os
import logging
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
from PIL import Image
import pandas as pd

# Set up logging for better traceability
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define the base directory path
BASE_IMAGE_DIRECTORY = r"cheque_regions"

# Load the processor and model
processor = TrOCRProcessor.from_pretrained('microsoft/trocr-large-stage1')
model = VisionEncoderDecoderModel.from_pretrained(
    'microsoft/trocr-large-stage1',
    device_map=None
)
model.to("cpu")
model.eval()

def extract_text_from_image(image_path):
    """Extracts text from a given image using the TrOCR model."""
    try:
        image = Image.open(image_path).convert("RGB")
        pixel_values = processor(image, return_tensors="pt").pixel_values
        generated_ids = model.generate(pixel_values, max_new_tokens=50)  # Set max_new_tokens explicitly
        generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
        return generated_text.strip()
    except Exception as e:
        logging.error(f"Error processing image {image_path}: {e}")
        return ""

def process_all_folders(base_dir, output_file):
    """Processes all image folders and extracts text into a tabular format."""
    if not os.path.exists(base_dir):
        logging.error(f"Base directory does not exist: {base_dir}")
        return

    # Initialize a list to store folder-level data
    data = []

    for folder_name in os.listdir(base_dir):
        folder_path = os.path.join(base_dir, folder_name)
        if os.path.isdir(folder_path):
            logging.info(f"Processing folder: {folder_name}")

            # Initialize a dictionary to store extracted data for the folder
            folder_data = {"Folder": folder_name}

            # Process each image in the folder
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('png', 'jpg', 'jpeg')):
                    image_path = os.path.join(folder_path, file_name)
                    extracted_text = extract_text_from_image(image_path)
                    # Use the file name (without extension) as the column name
                    column_name = os.path.splitext(file_name)[0]
                    folder_data[column_name] = extracted_text

            # Append folder data to the list
            data.append(folder_data)

    # Convert data to a DataFrame
    df = pd.DataFrame(data)

    # Save DataFrame to a CSV file
    df.to_csv(output_file, index=False)
    logging.info(f"Data successfully saved to {output_file}")

# Run the function to process all folders and save data to a CSV
if __name__ == "__main__":
    OUTPUT_FILE = r"extracted_data.csv"
    process_all_folders(BASE_IMAGE_DIRECTORY, OUTPUT_FILE)
