# 🧠 AI PDF Analyzer with Image-Based Question Generation 

This project is part of an AI/Python Internship task that involves analyzing a PDF file containing educational content (IMO Class 1 Maths Olympiad Sample Paper), extracting both text and images, and generating questions from the images using an offline transformer-based model.

---

## ✅ Features

- 📄 Extracts all **text and images** from a PDF file
- 📁 Saves images in a structured folder (`extracted_images/`)
- 🧠 Uses **BLIP** (Salesforce BLIP Transformer) to generate **captions**
- ❓ Creates **image-based questions** from captions
- 📦 Outputs results in structured JSON format

---

## 🗂️ Folder Structure
imo_pdf_ai_project/
├── extracted_images/ ← All images from PDF
├── imo_parser.py ← PDF text + image extractor
├── image_question_generator.py ← Caption + question generator (BLIP)
├── questions.json ← Extracted data (text + images)
├── questions_with_captions.json ← Final output with AI questions
├── requirements.txt ← Python dependencies
├── README.md
└── IMO class 1 Maths Olympiad Sample Paper 1 for the year 2024-25.pdf

## 📎 Sample Output Preview

> Run `questions_with_captions.json` for full output or see below:

```json
{
  "image": "page1_img1.png",
  "caption": "A set of geometric shapes",
  "question": "What is shown in the image? Caption: A set of geometric shapes"
}
