import os
from PIL import Image
from pathlib import Path

def optimize_images(directory, max_width=1920):
    image_extensions = {'.png', '.jpg', '.jpeg'}
    count = 0
    
    for root, _, files in os.walk(directory):
        if 'node_modules' in root or '.git' in root or '__pycache__' in root:
            continue
            
        for file in files:
            ext = Path(file).suffix.lower()
            if ext in image_extensions:
                file_path = os.path.join(root, file)
                
                try:
                    # Check size. Only bother with files > 200KB to save time, unless it's a huge PNG
                    size_kb = os.path.getsize(file_path) / 1024
                    
                    if size_kb > 300:
                        img = Image.open(file_path)
                        
                        # Downscale if too large
                        if img.width > max_width:
                            ratio = max_width / float(img.width)
                            new_height = int((float(img.height) * float(ratio)))
                            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                        
                        # Save as WebP
                        webp_path = os.path.splitext(file_path)[0] + '.webp'
                        
                        # Use quality 90 to be visually lossless
                        img.save(webp_path, 'WEBP', quality=90)
                        print(f"Converted {file_path} ({size_kb:.1f} KB) -> {webp_path}")
                        count += 1
                        
                        # Remove original file to save space
                        os.remove(file_path)
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

    print(f"Finished processing {count} images.")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Folders to process
    folders = ['assets', 'categories', 'states', 'story', 'home', 'static']
    for f in folders:
        folder_path = os.path.join(base_dir, f)
        if os.path.exists(folder_path):
            optimize_images(folder_path)
