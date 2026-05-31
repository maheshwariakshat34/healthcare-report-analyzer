from flask import Flask,render_template,request
import os
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

        return f"File Uploaded Successfully: {file.filename}"

    return "No File Uploaded"

if __name__ == "__main__":
    app.run(debug=True)