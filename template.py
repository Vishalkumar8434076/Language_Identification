
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "Language"


list_of_files = [
    ".github/workflows/.gitkeep",
    '.github/workflows/main.yaml',
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_preprocessing.py",
    f"src/components/custom_dataset.py",
    f"src/components/model_trainer.py",
    f"src/components/model_evaluation.py",
    f"src/components/model_pusher.py",
    f"src/cloud_storage/__init__.py",
    f"src/cloud_storage/s3_operations.py",
    f"src/utils/__init__.py",
    f"src/utils/gpu_functions.py",
    f"src/model/__init__.py",
    f"src/model/base_model.py",
    f"src/model/final_model.py",
    f"src/pipeline/__init__.py",
    f"src/pipeline/training_pipeline.py",
    f"src/pipeline/prediction_pipeline.py",
    f"src/entity/__init__.py",
    f"src/entity/config_entity.py",
    f"src/entity/artifact_entity.py",
    f"src/constants/__init__.py",
    f"src/exception/__init__.py",
    f"src/logger/__init__.py",
    "app.py",
    "Dockerfile",
    '.dockerignore',
    "requirements.txt",
    "setup.py",
    "templates/index.html",
    'static/css/style.css',
    'bestmodel/__init__.py',
    'download/__init__.py',
    "prediction_dataset/__init__.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
