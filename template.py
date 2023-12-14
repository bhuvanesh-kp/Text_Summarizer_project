import os
from pathlib import Path
import logging

project_name = "textsummarizer"

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

listfile =[
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "congif/config.yaml",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "main.py",
    "requirements.txt",
    "setup.py",
    "research/trails.ipynb",
    "test.py"
]


for filepath in listfile:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating file directory {filedir} for {filename}")
    

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating a empty file: {filepath}")
    else:
        logging.info(f"{filepath} already exists")