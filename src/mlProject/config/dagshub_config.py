import os
import dagshub
import mlflow

def init_dagshub():
    repo_owner = "Pradip-Mane"
    repo_name = "End-to-end-ML-project-with-ml-flow"

    # 1. Init dagshub FIRST
    dagshub.init(repo_owner=repo_owner, repo_name=repo_name, mlflow=True)

    # 2. Set tracking URI AFTER init
    mlflow.set_tracking_uri(
        f"https://dagshub.com/{repo_owner}/{repo_name}.mlflow"
    )

    # 3. (IMPORTANT) Set experiment explicitly
    mlflow.set_experiment("End2End-ML-Project")