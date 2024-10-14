import os
import comtypes.client
import pythoncom
from flask import Flask, request, send_file, jsonify

from flask_cors import CORS


# Enable CORS for all routes



app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'])


# Define directories for uploads and converted files
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
CONVERTED_FOLDER = os.path.join(os.getcwd(), 'converted')

# Create the directories if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(CONVERTED_FOLDER, exist_ok=True)

def convert_to_pdf(docx_path, pdf_path):
    # Initialize the COM library
    pythoncom.CoInitialize()
    
    try:
        # Create a Word application object
        word = comtypes.client.CreateObject('Word.Application')
        word.Visible = False

        # Open the .docx file
        doc = word.Documents.Open(docx_path)

        # Save as PDF
        doc.SaveAs(pdf_path, FileFormat=17)

        # Close the Word document and quit the application
        doc.Close()
        word.Quit()
    finally:
        # Uninitialize the COM library
        pythoncom.CoUninitialize()


import os
from flask import abort

@app.route('/convert', methods=['POST'])
def upload_and_convert():
    file = request.files.get('file')
    if file:
        try:
            # Save the uploaded file to the 'uploads' folder
            input_filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(input_filepath)
            
            # Define output file path in the 'converted' folder
            output_filename = file.filename.replace('.docx', '.pdf')
            output_filepath = os.path.join(CONVERTED_FOLDER, output_filename)
            
            # Convert the DOCX file to PDF
            convert_to_pdf(input_filepath, output_filepath)

            # Check if the output file was successfully created
            if not os.path.exists(output_filepath):
                return jsonify({'error': 'PDF conversion failed'}), 500
            
            # Return the converted PDF file as a download
            return send_file(output_filepath, as_attachment=True, mimetype='application/pdf')
        except Exception as e:
            return jsonify({'error': str(e)}), 500
        finally:
            # Optionally delete the input file
            if os.path.exists(input_filepath):
                os.remove(input_filepath)
    else:
        return jsonify({'error': 'No file uploaded'}), 400


if __name__ == "__main__":
    app.run(debug=True)
