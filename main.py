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


pregunta1 = "Soy recién egresado de mi carrera y el mundo de las inversionas me llama. Pero no tengo nada de información, hay algo que me puedas decir sobre esto en Banorte?"
pregunta2 = "¿Qué es la calificación en los fondos de inversion?"


pregunta3 = "¿Me puedes decir qué es el horizonte de inversion?"
pregunta4 = "Me puedes decir de qué trata el fondo de inversión Dolares+ de Banorte"
pregunta5 = "Me gustaria saber cuales son los mejores planes de inversion de Banorte para alguien con mucho capital, tolerante a los largos plazos y que acepta correr riesgos con su inversion"
pregunta6 = "Que plan de Banorte para invertir es para mi si quisiera empezar con poco capital y esperar un pequeño plazo. Tampoco me gustaria correr riesgos"
pregunta7 = "Me gustaria saber cuales son los mejores planes de inversion de Banorte para un recien egresado de la unviersidad con poco capital que busca crecer su dinero"



print(index.query(pregunta2))


