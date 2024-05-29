import json
import spacy
import argparse
from pdfminer.high_level import extract_text
import warnings
import os
import urllib.request
import zipfile
from tqdm import tqdm
from spacy.language import Language
import site

# Suppress specific warnings
warnings.filterwarnings("ignore", message="torch.utils._pytree._register_pytree_node is deprecated")

model_name = "pyresumeparserV1"
MODEL_URL = f"https://huggingface.co/pkhan/resumeparser/resolve/main/{model_name}.zip"

def download_model():
    package_dir = site.getsitepackages()[0]
    model_dir = os.path.join(package_dir, 'pyresumeparser', model_name)
    model_zip_path = os.path.join(package_dir, 'pyresumeparser', f'{model_name}.zip')

    # print("*" * 50)
    # print("Downloading model...")
    # print("Package directory:", package_dir)
    # print("Model directory:", model_dir)
    # print("Model zip path:", model_zip_path)

    if not os.path.exists(model_dir) or not os.listdir(model_dir):
        os.makedirs(model_dir, exist_ok=True)
        # print(f"Downloading model to {model_zip_path}...")
        with urllib.request.urlopen(MODEL_URL) as response, open(model_zip_path, 'wb') as out_file:
            total_length = int(response.info().get('Content-Length').strip())
            block_size = 1024
            with tqdm(total=total_length, unit='B', unit_scale=True, desc="Downloading model") as pbar:
                while True:
                    buffer = response.read(block_size)
                    if not buffer:
                        break
                    out_file.write(buffer)
                    pbar.update(len(buffer))
        # print("Download complete. Extracting files...")
        with zipfile.ZipFile(model_zip_path, 'r') as zip_ref:
            zip_ref.extractall(model_dir)
        # print("Extraction complete!")
        os.remove(model_zip_path)
    else:
        pass
        # print("Model already exists.")

def load_model():
    site_packages_path = site.getsitepackages()[0]
    model_dir = os.path.join(site_packages_path, 'pyresumeparser', model_name)
    model_path = os.path.join(model_dir, model_name)

    # Ensure the model is downloaded
    download_model()

    # Load the spaCy model
    try:
        nlp = spacy.load(model_path)
    except ValueError:
        # In case the transformer is not registered, let's add it manually
        @Language.factory("transformer")
        def create_transformer_component(nlp, name):
            from spacy_transformers import Transformer
            return Transformer(nlp.vocab)
        
        nlp = spacy.load(model_path)
    
    return nlp

def pdf_to_text(filepath):
    """
    Extracts text from a PDF file.

    :param filepath: Path to the PDF file
    :return: Extracted text as a string
    """
    return extract_text(filepath)

def extract_entities(text, nlp):
    """
    Extracts entities from the text using a spaCy model.

    :param text: Input text
    :param nlp: spaCy NLP model
    :return: Dictionary of entities
    """
    doc = nlp(text)
    
    # Initialize a dictionary to hold entity lists
    entities = {
        'first_name': [],
        'last_name': [],
        'email': [],
        'phone': [],
        'country': [],
        'state': [],
        'city': [],
        'pincode': [],
        'college_name': [],
        'education': [],
        'designation': [],
        'position_held': [],
        'companies_worked': [],
        'projects_worked': [],
        'skills': [],
        'total_experience': [],
        'language': [],
        'linkedin': [],
        'github': []
    }
    
    # Populate the dictionary with entities from the document
    for ent in doc.ents:
        label = ent.label_.lower()
        if label in entities:
            entities[label].append(ent.text)
    
    # Remove duplicates by converting lists to sets and back to lists
    for key in entities:
        entities[key] = list(set(entities[key]))
    
    return entities

def parse_resume(filepath, nlp):
    """
    Converts a PDF file to a JSON object with extracted entities.

    :param filepath: Path to the PDF file
    :param nlp: spaCy NLP model
    :return: JSON object with extracted entities
    """
    text = pdf_to_text(filepath)
    entities = extract_entities(text, nlp)
    entities_json = json.dumps(entities, indent=4)
    return entities_json

def main():
    parser = argparse.ArgumentParser(description="Parse a resume PDF file and extract entities.")
    parser.add_argument("filepath", type=str, help="Path to the resume PDF file.")
    args = parser.parse_args()
    
    nlp = load_model()
    parsed_resume = parse_resume(args.filepath, nlp)
    print(parsed_resume)

if __name__ == "__main__":
    main()
