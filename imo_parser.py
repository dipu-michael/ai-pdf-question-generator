import fitz  # PyMuPDF
import os
import json

# Constants
PDF_FILE = "IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf"
OUTPUT_DIR = "extracted_images"
OUTPUT_JSON = "questions.json"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
doc = fitz.open(PDF_FILE)
output = []

for page_num in range(len(doc)):
    page = doc[page_num]
    text = page.get_text("text")
    image_list = []

    for img_index, img in enumerate(page.get_images(full=True)):
        xref = img[0]
        base_image = doc.extract_image(xref)
        img_bytes = base_image["image"]
        ext = base_image["ext"]
        image_filename = f"page{page_num+1}_img{img_index+1}.{ext}"
        image_path = os.path.join(OUTPUT_DIR, image_filename)

        with open(image_path, "wb") as f:
            f.write(img_bytes)

        image_list.append(image_path)

    output.append({
        "page_number": page_num + 1,
        "text": text.strip(),
        "images": image_list
    })

# Save as JSON
with open(OUTPUT_JSON, "w") as f:
    json.dump(output, f, indent=2)

print(f"✅ PDF processing complete. Output saved to {OUTPUT_JSON}")
