import os
from flask import Flask, jsonify, request
from werkzeug.utils import secure_filename

# Model specific
# from Model_300.model import PDF_parser

UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload/documents', methods=['POST'])
def upload_documents():
    res = []
    files = request.files.getlist('files')
    for f in files:
        filename = secure_filename(f.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(path)


    return 'Good job'

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
