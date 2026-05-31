from ocr.azure_ocr import extract_text
from analyzer.report_analyzer import (
    extract_parameters,
    analyzer_parameters,
    generate_summary
)

text = extract_text("ocr/report.png")

print("OCR TEXT:")
print(text)

data = extract_parameters(text)

print("\nEXTRACTED DATA:")
print(data)

results = analyzer_parameters(data)

print("\nRESULTS:")
print(results)

for item in results:
    print(
        f"{item['parameter']} : "
        f"{item['value']} "
        f"--> {item['status']}"
    )

summary = generate_summary(results)

print("\nHealth Summary:")
print(summary)