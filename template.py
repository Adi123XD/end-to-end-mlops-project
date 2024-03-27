# this template.py script is used to create the folder structures used for my project
import os
import logging
from pathlib import Path
logging.basicConfig(level=logging.INFO , format='[%(asctime)s]: %(message)s')

project_name = 'mlProject'
list_of_files =[
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__inti__.py',
    f'src/{project_name}/utils/common.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/entity/config_entity.py',
    f'src/{project_name}/constants/__init.py',
    'config/config.yaml',
    'params.yaml',
    'schema.yaml',
    'main.py',
    'app.py',
    'Dockerfile',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'template/index.html'
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir , filename = os.path.split(filepath)
    if (filedir!=""):
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory {filedir} for file {filename}')
    if (not (os.path.exists(filepath)) or (os.path.getsize(filepath))==0):
        with open (filepath ,"w"):
            pass
        logging.info(f'creating empty file {filepath}')
    else:
        logging.info(f'{filepath} already exists')