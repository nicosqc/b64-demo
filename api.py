from flask import Flask, jsonify
import base64

app = Flask(__name__)

@app.route('/getpdf', methods=['GET'])
def get_pdf():
    pdf_path = 'files/sample.pdf'  # Path to the PDF file

    with open(pdf_path, 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()
        pdf_base64 = base64.b64encode(pdf_bytes).decode('utf-8')

    return jsonify({'pdf_base64': pdf_base64})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
