import os
import cv2

# Define paths and regions of interest
base_image_directory = r"cheque_images"
regions_of_interest = {
    'date': (754, 40, 970, 88),
    'payee': (70, 120, 760, 175),
    'name': (825, 440, 990, 475),
    'amount_digits': (735, 225, 970, 290),
    'account_number': (115, 300, 320, 335)
}
regions_output_directory = r"cheque_regions"

# Function to extract regions of interest from check images
def extract_interest_regions(base_image_directory, regions_of_interest, regions_output_directory):
    os.makedirs(regions_output_directory, exist_ok=True)
    
    for image_file in os.listdir(base_image_directory):
        image_path = os.path.join(base_image_directory, image_file)
        if image_file.lower().endswith(('png', 'jpg', 'jpeg')):
            image = cv2.imread(image_path)
            if image is not None:
                image_name = os.path.splitext(image_file)[0]
                output_page_dir = os.path.join(regions_output_directory, image_name)
                os.makedirs(output_page_dir, exist_ok=True)
                
                for field, (x0, y0, x1, y1) in regions_of_interest.items():
                    region_of_interest = image[y0:y1, x0:x1]
                    output_image_path = os.path.join(output_page_dir, f"{field}_region.png")
                    cv2.imwrite(output_image_path, region_of_interest)
                    print(f"Saved {field} region for {image_file} at {output_image_path}")

# Main function to process images and extract regions of interest
def process_workflow(base_image_directory, regions_of_interest, regions_output_directory):
    os.makedirs(regions_output_directory, exist_ok=True)

    # Extract regions of interest from the check images
    extract_interest_regions(base_image_directory, regions_of_interest, regions_output_directory)

# Run the workflow
process_workflow(base_image_directory, regions_of_interest, regions_output_directory)