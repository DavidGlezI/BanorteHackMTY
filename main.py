from langchain.document_loaders import UnstructuredPDFLoader
from langchain.indexes import VectorstoreIndexCreator



# Instalar dependencias 

"""
# Activar venv: source venv/bin/activate

pip3 install langchain
pip3 install unstructured
pip3 install openai
pip3 install chromadb
pip3 install Cython
pip3 install tiktoken
pip3 install pdf2image
pip3 install pdfminer-six

"""

import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv('MY_OPENAI_KEY')


pdf_folder_path = "/Users/david/Desktop/BanorteHackMTY/files" # Folder estatico, cambiar al implementarlo

os.listdir(pdf_folder_path)


loaders = [UnstructuredPDFLoader(os.path.join(pdf_folder_path, fn)) for fn in os.listdir(pdf_folder_path)]

index = VectorstoreIndexCreator().from_loaders(loaders)


print(index.query("Que es la calificacion en los fondos de inversion"))


