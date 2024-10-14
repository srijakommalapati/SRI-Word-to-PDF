Asri Doc to PDF Converter
Asri Doc to PDF Converter is a simple web-based application that allows users to upload .docx files and convert them to PDF format. The app is built with a Flask backend for file conversion and a React-based frontend for user interaction.

Features
DOCX to PDF Conversion: Upload .docx files, and the app converts them to PDF format.
Responsive Design: The frontend is responsive and user-friendly, styled for an aesthetically pleasing experience.
Error Handling: Provides appropriate error messages for file size limits or conversion failures.
Download Converted Files: Once conversion is complete, users can download the converted PDF.
Table of Contents
Features
Installation
Backend Setup
Frontend Setup
Usage
Contributing
License
Installation
Prerequisites
Ensure you have the following installed on your system:

Node.js and npm (for the frontend)
Python 3.x (for the backend)
Flask
comtypes
Microsoft Word installed on the system for COM-based .docx to PDF conversion.
Backend Setup
Clone the repository:

 

git clone https://github.com/yourusername/asri-doc-to-pdf-converter.git
Navigate to the backend directory:

 
 
cd asri-doc-to-pdf-converter/backend
Create a virtual environment and activate it (optional, but recommended):

 
 
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

 
 
pip install -r requirements.txt
Run the Flask backend:

 
 
flask run
The backend should now be running on http://localhost:5000/.

Frontend Setup
Navigate to the frontend directory:

 
 
cd asri-doc-to-pdf-converter/frontend
Install the required npm packages:

 
 
npm install
Start the development server:

 
 
npm start
The frontend should now be running on http://localhost:3000/.

Usage
Open your browser and navigate to http://localhost:3000/.
Upload a .docx file by clicking the Choose File button.
Click the Convert to PDF button.
Once the conversion is complete, a Download Converted PDF link will appear. Click it to download your PDF.
Project Structure
The project is organized as follows:

 
 
asri-doc-to-pdf-converter/
│
├── backend/                  # Flask-based backend
│   ├── uploads/              # Folder where uploaded DOCX files are stored
│   ├── converted/            # Folder where converted PDF files are stored
│   ├── app.py                # Flask server with file conversion logic
│   ├── requirements.txt      # Backend Python dependencies
│
└── frontend/                 # React-based frontend
    ├── public/               # Public assets
    ├── src/                  # Source code for the frontend
    │   ├── App.js            # Main React component
    │   ├── App.css           # CSS for styling
    │   └── index.js          # Entry point for the React app
    ├── package.json          # Frontend npm dependencies
