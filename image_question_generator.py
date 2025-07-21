from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os
import json

# Load BLIP captioning model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Load image paths from previously generated questions.json
with open("questions.json", "r") as f:
    data = json.load(f)

# Function to caption an image
def generate_caption(image_path):
    try:
        image = Image.open(image_path).convert('RGB')
        inputs = processor(images=image, return_tensors="pt")
        output = model.generate(**inputs)
        caption = processor.decode(output[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        print(f"❌ Error processing {image_path}: {e}")
        return "Could not generate caption."

# Add questions based on captions
for entry in data:
    entry["generated_questions"] = []

    for image_path in entry["images"]:
        caption = generate_caption(image_path)
        question = f"What is shown in the image? Caption: {caption}"
        entry["generated_questions"].append({
            "image": image_path,
            "caption": caption,
            "question": question
        })

# Save to new output
with open("questions_with_captions.json", "w") as f:
    json.dump(data, f, indent=2)

print("✅ Image-based questions saved in questions_with_captions.json")
