import json
import logging
import os
import pickle
from pathlib import Path

import joblib

logging.basicConfig(level=logging.INFO)

SUPPORTED_METHODS = {
    "joblib": joblib.dump,
    "pickle": pickle.dump,
    # "keras": tf.keras.models.save_model,
}

def get_project_root(filepath: str) -> str:
    """
    Determine the project root directory from a given file path.

    Args:
        filepath (str): The file path to evaluate.

    Returns:
        str: The project root directory path.

    Raises:
        ValueError: If the filepath is empty or None, or if an error occurs during processing.
    """
    if not filepath:
        raise ValueError("Empty or None filepath provided.")
    try:
        paths = [
            "src",
            "src/scripts/ingest",
            "src/scripts/tests",
            "src/notebooks",
            "src/outputs",
            "src/datasets",
        ]
        for path in paths:
            if filepath.endswith(path.replace("/", os.path.sep)):
                return str(Path(filepath).parents[len(path.split(os.path.sep)) - 1])
    except Exception as e:
        raise ValueError(f"Error in get_project_root: {e}") from e
    return filepath

def get_path(dir: str) -> str:
    """
    Retrieve a specific path from a configuration file.

    Args:
        dir (str): The key of the path to retrieve.

    Returns:
        str: The path associated with the provided key.

    Raises:
        ValueError: If any errors occur during the path retrieval process.
    """
    try:
        homedir = get_project_root(os.getcwd())
        config_path = os.path.join(homedir, ".datahelprc")
        if not os.path.isfile(config_path):
            raise FileNotFoundError(f"No config file found at {config_path}")
        with open(config_path) as configfile:
            try:
                config = json.load(configfile)
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON in config file {config_path}: {e}") from e
        if dir not in config:
            raise KeyError(f"No key {dir} in config file {config_path}")
        path = os.path.join(homedir, config[dir].replace("/", os.path.sep))
        return path
    except Exception as e:
        raise ValueError(f"Error in get_path: {e}") from e

def create_directory(path: Path):
    """
    Create a directory if it does not exist already.

    Args:
        path (Path): The path of the directory to create.
    """
    path.mkdir(parents=True, exist_ok=True)

def create_project(project_name: str):
    """
    Create a standard data science project directory structure.

    Args:
        project_name (str): The name of the project.
    """
    base_path = Path.cwd() / project_name
    data_path = base_path / "datasets"
    output_path = base_path / "outputs"
    models_path = output_path / "models"
    src_path = base_path / "src"
    scripts_path = src_path / "scripts"
    ingest_path = scripts_path / "ingest"
    test_path = scripts_path / "tests"
    notebooks_path = src_path / "notebooks"

    dirs = [
        base_path,
        data_path,
        output_path,
        models_path,
        src_path,
        scripts_path,
        ingest_path,
        test_path,
        notebooks_path,
    ]

    for dir in dirs:
        create_directory(dir)

    config = {
        "description": "Holds the project config settings",
        "base_path": str(base_path),
        "data_path": str(data_path),
        "output_path": str(output_path),
        "models_path": str(models_path),
    }

    config_path = base_path / ".datahelprc"
    with open(config_path, "w") as config_file:
        json.dump(config, config_file, indent=4)

    readme_path = base_path / "README.rst"
    with open(readme_path, "w") as readme:
        readme.write("Creates a standard data science project directory structure.")

def model_save(model, name="model", method="joblib"):
    """
    Save a model using the specified method.

    Args:
        model: The model to save.
        name (str): The name of the model file.
        method (str): The method to use for saving the model.

    Raises:
        ValueError: If the model is None or the method is not supported.
    """
    if model is None:
        raise ValueError("Expecting a binary model file, got 'None'")
    if method not in SUPPORTED_METHODS:
        raise ValueError(f"Method {method} not supported. Supported methods are: {list(SUPPORTED_METHODS.keys())}")
    try:
        model_path = get_path("models_path")
        file_name = f"{model_path}/{name}.{method}"
        SUPPORTED_METHODS[method](model, file_name)
        logging.info(f"Model saved successfully at {file_name}")
    except FileNotFoundError:
        logging.warning(f"Models folder does not exist. Saving model to the {name} folder.")
        file_name = f"{name}.{method}"
        SUPPORTED_METHODS[method](model, file_name)
    except PermissionError as e:
        logging.error(f"Permission error while saving model. Check file permissions. {e}")
    except Exception as e:
        logging.error(f"Failed to save model due to {e}")
