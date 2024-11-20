# Check Master Branch for Code
# MCQ-Generator-using-AI-Auto-Create-Questions-from-Text-Files-Flask-Web-App

This project is a Flask web application that automatically generates multiple-choice questions (MCQs) from text files using Google Generative AI. It supports file handling for PDF, DOCX, and TXT formats, allowing you to upload a file and generate MCQs based on the content. The generated questions can be downloaded in both text and PDF formats, making it a useful tool for educators and developers who want to automate the process of creating quizzes and tests.

## Features

- **Automatic MCQ Generation**: Generate multiple-choice questions from text files using the Gemini model (Google Generative AI).
- **File Handling**: Upload and extract text from PDF, DOCX, and TXT files.
- **Download Options**: Download generated MCQs in both text and PDF formats.
- **Flask Web App**: Easy-to-use interface to upload files and generate MCQs.
- **Google AI Integration**: Leverages Google's Generative AI to create accurate and meaningful questions from the uploaded text.

## Technologies Used

- **Flask**: Python web framework to build the app.
- **Google Generative AI (Gemini)**: AI model used for generating MCQs.
- **Python PDF Libraries**: Used to create downloadable PDF files.
- **Python Libraries**:
  - `python-docx`: For extracting text from DOCX files.
  - `PyPDF2`: For extracting text from PDF files.
  - `Flask`: Web framework.
  - `os`, `io`: File handling utilities.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/HelpRam/MCQ-Generator-using-AI-Auto-Create-Questions-from-Text-Files-Flask-Web-App.git
   cd MCQ-Generator-using-AI-Auto-Create-Questions-from-Text-Files-Flask-Web-App
   ```

2. **Create and activate a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google Generative AI API**:
   - Follow the instructions on [Google Cloud](https://cloud.google.com/docs/authentication/getting-started) to set up authentication and obtain an API key.
   - Set your environment variable for the API key:
     ```bash
     export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/credentials.json"
     ```

5. **Run the Flask application**:
   ```bash
   flask run
   ```

   This will start the web app locally at `http://127.0.0.1:5000/`.

## Usage

1. **Upload a file**: Choose a PDF, DOCX, or TXT file that contains the text you want to generate MCQs from.
2. **Generate MCQs**: Once the file is uploaded, the AI will process the content and generate a set of multiple-choice questions based on the text.
3. **Download MCQs**: After the questions are generated, you can download them in either text or PDF format.

## File Formats Supported

- **PDF**: Upload PDF files, and the app will extract the text to generate MCQs.
- **DOCX**: Upload Word documents, and the app will extract the content to create MCQs.
- **TXT**: Upload plain text files to create questions from the text.

## Example Workflow

1. Upload a PDF document containing educational content (e.g., a chapter from a textbook).
2. The system processes the content and generates multiple-choice questions.
3. You can download the questions in your preferred format (text or PDF).
4. Use the questions for quizzes, assignments, or practice tests.



## Contributions

Feel free to fork this repository and contribute! Submit any issues or pull requests related to bug fixes, feature requests, or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

By using this app, educators and developers can automate the creation of quizzes and tests, saving valuable time while ensuring that MCQs are generated effectively and accurately from various document formats.
