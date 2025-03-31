from transformers import LayoutLMv3Processor, LayoutLMv3ForTokenClassification
from PIL import Image
import os

def parse_document(file_path):
    processor = LayoutLMv3Processor.from_pretrained("microsoft/layoutlmv3-base", apply_ocr=True)
    model = LayoutLMv3ForTokenClassification.from_pretrained("microsoft/layoutlmv3-base")
    
    image = Image.open(file_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    outputs = model(**inputs)
    print("Parsed document successfully.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=True, help="Path to input PDF/image")
    args = parser.parse_args()
    parse_document(args.input)
