from flask import Flask,render_template,request
import os
from ocr.azure_ocr import extract_text
from analyzer.report_analyzer import (
    extract_parameters,
    analyzer_parameters,
    generate_summary
)
app=Flask(__name__)
UPLOAD_FOLDER=('uploads')
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/upload',methods=['POST'])
def upload():
    file = request.files['report']

    if file:
        filepath = os.path.join(
            app.config['UPLOAD_FOLDER'],
            file.filename
        )

        file.save(filepath)
        text = extract_text(filepath)

        data = extract_parameters(text)

        results = analyzer_parameters(data)

        summary = generate_summary(results)

        return render_template(
            "result.html",
            results=results,
            summary=summary
        )

    return "No File Uploaded"


if __name__ == "__main__":
    app.run(debug=True)