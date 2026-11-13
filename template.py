import os
from pathlib import Path

project_name="Customer_segement"

list_of_files=[
    f"{project_name}/__init__.py",
    f"{project_name}/components/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_validation.py",
    f"{project_name}/components/data_transformation.py",
    f"{project_name}/components/model_trainer.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/components/model_pusher.py",
    f"{project_name}/configuration/__init__.py",
    f"{project_name}/constants/__init__.py",
    f"{project_name}/entity/__init__.py",
    f"{project_name}/entity/config.py",
    f"{project_name}/entity/artifacts.py",
    f"{project_name}/exception/__init__.py",
    f"{project_name}/logger/__init__.py",
    f"{project_name}/pipeline/__init__.py",
    f"{project_name}/pipeline/training_pipeline.py",
    f"{project_name}/pipeline/prediction_pipeline.py",
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/main_utils.py",
    f"{project_name}/data_access/__init__.py",
    f"{project_name}/data_access/customer_data.py",
    f"{project_name}/cloud_storage/__init__.py",
    f"{project_name}/cloud_storage/aws_storage.py",
    "app.py",
    "setup.py",
    "requirements.txt",
    "config/model.yaml",
    "config/schema.yaml",
    ".dockerignore",
    "Dockerfile",
    "demo.py"
]
for file in list_of_files:
    file_path=file
    file_dir,filename=os.path.split(file)
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,"w") as f:
            pass
    else:
        print(f"File is already present at :{file_path}")



    













    

    
