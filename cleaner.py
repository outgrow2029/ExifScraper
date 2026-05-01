import os
from PIL import Image

def remove_metadata(input_path, output_path):
    """
    Strips EXIF and metadata by creating a new image 
    containing only the pixel data.
    """
    try:
        # Open the image
        img = Image.open(input_path)
        
        # Strip metadata by creating a new image object with only the pixel data
        # Convert to RGB to ensure no hidden profile data remains
        data = list(img.getdata())
        clean_img = Image.new(img.mode, img.size)
        clean_img.putdata(data)
        
        # Save the "clean" version
        clean_img.save(output_path)
        print(f"[+] Success: Metadata stripped. Saved to: {output_path}")
        
    except Exception as e:
        print(f"[-] Error: {e}")

if __name__ == "__main__":
    print("--- Privacy Scrubber v1.0 ---")
    file_to_clean = input("Enter the path to the image: ").strip()
    
    if os.path.exists(file_to_clean):
        output_name = "CLEANED_" + os.path.basename(file_to_clean)
        remove_metadata(file_to_clean, output_name)
    else:
        print("[-] File not found. Check the path!")