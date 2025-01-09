<<<<<<< HEAD
# Text Divider and Recognition

## Overview
The Text Divider and Recognition project is designed to process handwritten kyrgyz text through dividing kyrgyz text into words, dividing words into letters and recognizing them. This tool can be used for data preprocessing in natural language processing tasks, document analysis, and automation of text processing pipelines in kyrgyz language. This project is built with Django for the web interface.

## Project Structure
    ```bash
TextDivider/
├── manage.py                  
├── TextDivider/
│   ├── settings.py            
│   ├── urls.py                
│   └── wsgi.py                
├── apps/    
│   ├── Divider/  
│   │   ├── migrations/                             
│   │   ├── __init__.py      
│   │   ├── admin.py  
│   │   ├── apps.py         
│   │   ├── forms.py  
│   │   ├── models.py   
│   │   ├── tests.py   
│   │   └── views.py  
│   ├── extractor/  
│   │   └── extract.py  
│   └── recog/  
│       └── recog.py            
├── media/
├── templates/              
├── requirements.txt         
├── README.md             
└── LICENSE             
    ```

## Features
- **Kyrgyz Text Division**: Spliting handwritten text into sections based on predefined delimiters or custom rules.
- **Kyrgyz Word Division**: Spliting words into letters based on predefined delimiters or custom rules.
- **Pattern Recognition**: Identifies specified letter.
- **Web Interface**: Django one page web interface for uploading images and viewing results.
- **Input**: Input can be only image file such as PNG or JPG.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Tumbler-3/TextDivider.git
   ```
2. Navigate to the project directory:
   ```bash
   cd text-divider-recognition
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply Django migrations:
   ```bash
   python manage.py makemigrations
   ```
6. Apply Django migrations:
   ```bash
   python manage.py migrate
   ```

## Usage

### One page Web Interface
1. Start the Django server:
   ```bash
   python manage.py runserver
   ```
2. Open a web browser and navigate to `http://127.0.0.1:8000/`.
3. Upload a image with text for processing.
4. View the processed results.

## Contributing
Recognition model was taken from https://github.com/abdulra7ma/CyrillicSegNet 
Already created model can be taken from here https://drive.google.com/file/d/1t-uOUophlqNdqqV57fHF6luM_MnwMc92/view?usp=sharing

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions and support, please open an issue in the GitHub repository.
