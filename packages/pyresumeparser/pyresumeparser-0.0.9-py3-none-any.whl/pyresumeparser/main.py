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
from pyresumeparser._version import __version__

# Suppress specific warnings
warnings.filterwarnings("ignore", message="torch.utils._pytree._register_pytree_node is deprecated")

model_name = "pyresumeparserV1"
MODEL_URL = f"https://huggingface.co/pkhan/resumeparser/resolve/main/{model_name}.zip"

def download_model():
    package_dir = site.getsitepackages()[0]
    model_dir = os.path.join(package_dir, 'pyresumeparser', model_name)
    model_zip_path = os.path.join(package_dir, 'pyresumeparser', f'{model_name}.zip')

    if not os.path.exists(model_dir) or not os.listdir(model_dir):
        os.makedirs(model_dir, exist_ok=True)
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
        with zipfile.ZipFile(model_zip_path, 'r') as zip_ref:
            zip_ref.extractall(model_dir)
        os.remove(model_zip_path)

def load_model():
    site_packages_path = site.getsitepackages()[0]
    model_dir = os.path.join(site_packages_path, 'pyresumeparser', model_name)
    model_path = os.path.join(model_dir, model_name)

    download_model()

    try:
        nlp = spacy.load(model_path)
    except ValueError:
        @Language.factory("transformer")
        def create_transformer_component(nlp, name):
            from spacy_transformers import Transformer
            return Transformer(nlp.vocab)
        nlp = spacy.load(model_path)
    
    return nlp

def pdf_to_text(filepath):
    return extract_text(filepath)

def extract_entities(text, nlp):
    doc = nlp(text)
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
    
    for ent in doc.ents:
        label = ent.label_.lower()
        if label in entities:
            entities[label].append(ent.text)
    
    for key in entities:
        entities[key] = list(set(entities[key]))
    
    return entities

def parse_resume(filepath):
    nlp = load_model()
    text = pdf_to_text(filepath)
    entities = extract_entities(text, nlp)
    entities_json = json.dumps(entities, indent=4)
    return entities_json

def main():
    parser = argparse.ArgumentParser(description="Parse a resume PDF file and extract entities.")
    parser.add_argument("filepath", type=str, help="Path to the resume PDF file.")
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    args = parser.parse_args()
    
    parsed_resume = parse_resume(args.filepath)
    print(parsed_resume)

if __name__ == "__main__":
    main()
