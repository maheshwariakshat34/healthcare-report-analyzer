from ocr.extractor import extract_text
from analyzer.report_analyzer import (
    extract_parameters,
    analyzer_parameters,
    generate_summary
)

text = extract_text("ocr/report.png")

data = extract_parameters(text)

results = analyzer_parameters(data)

for item in results:
    print(
        f"{item['parameter']} : "
        f"{item['value']} "
        f"--> {item['status']}"
    )
summary = generate_summary(results)

print("\nHealth Summary:")
print(summary)