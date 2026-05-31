from ocr.azure_ocr import extract_text

text = extract_text("report.png")

print(text)