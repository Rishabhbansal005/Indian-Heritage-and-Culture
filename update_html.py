import os
import re

def update_html_files(directory):
    for root, _, files in os.walk(directory):
        if 'node_modules' in root or '.git' in root or '__pycache__' in root:
            continue
            
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace .png, .jpg, .jpeg with .webp IF .webp exists.
                # Actually, easier to use a regex to find all <img src="X">
                # and check if X.webp exists or X's extension replaced by .webp exists on disk.
                
                # Regex to find <img ...>
                img_pattern = re.compile(r'<img\s+([^>]*?)>', re.IGNORECASE)
                
                def img_replacer(match):
                    img_attrs = match.group(1)
                    
                    if 'loading=' not in img_attrs.lower():
                        img_attrs += ' loading="lazy"'
                        
                    return f'<img {img_attrs}>'
                
                new_content = img_pattern.sub(img_replacer, content)
                
                # Now find all .webp files and replace .png/.jpg references in HTML if they were converted
                # To be completely safe, we can just replace .png with .webp, .jpg with .webp for all files that actually exist as .webp
                webp_files = []
                for w_root, _, w_files in os.walk(base_dir):
                    if 'node_modules' in w_root or '.git' in w_root or '__pycache__' in w_root:
                        continue
                    for wf in w_files:
                        if wf.endswith('.webp'):
                            webp_files.append(wf)
                
                for wf in webp_files:
                    base_name = os.path.splitext(wf)[0]
                    # If html has base_name.png or base_name.jpg, replace it with base_name.webp
                    # But be careful with simple strings, maybe just replace occurrences of base_name + '.png'
                    new_content = re.sub(re.escape(base_name + '.png'), base_name + '.webp', new_content, flags=re.IGNORECASE)
                    new_content = re.sub(re.escape(base_name + '.jpg'), base_name + '.webp', new_content, flags=re.IGNORECASE)
                    new_content = re.sub(re.escape(base_name + '.jpeg'), base_name + '.webp', new_content, flags=re.IGNORECASE)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
    print("Updated HTML with loading='lazy'")

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    update_html_files(base_dir)
