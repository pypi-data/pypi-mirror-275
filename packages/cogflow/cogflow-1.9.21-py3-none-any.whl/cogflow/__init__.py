from .plugin_config import (
    TRACKING_URI,
    TIMER_IN_SEC,
    ML_TOOL,
    ACCESS_KEY_ID,
    SECRET_ACCESS_KEY,
    S3_ENDPOINT_URL,
    ML_DB_USERNAME,
    ML_DB_PASSWORD,
    ML_DB_HOST,
    ML_DB_PORT,
    ML_DB_NAME,
    COGFLOW_DB_USERNAME,
    COGFLOW_DB_PASSWORD,
    COGFLOW_DB_HOST,
    COGFLOW_DB_PORT,
    COGFLOW_DB_NAME,
    MINIO_ENDPOINT_URL,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_ACCESS_KEY,
    API_BASEPATH,
)
import numpy as np
import pandas as pd
from typing import Union, Any, List, Optional
from mlflow.models.signature import ModelSignature
from scipy.sparse import csr_matrix, csc_matrix
from .pluginmanager import PluginManager
from .plugins.dataset_plugin import DatasetMetadata, DatasetPlugin
from .plugins.mlflowplugin import MlflowPlugin
from .plugins.kubeflowplugin import CogContainer, KubeflowPlugin

pyfunc = MlflowPlugin().pyfunc
mlflow = MlflowPlugin().mlflow
sklearn = MlflowPlugin().sklearn
cogclient = MlflowPlugin().cogclient
tensorflow = MlflowPlugin().tensorflow
pytorch = MlflowPlugin().pytorch
models = MlflowPlugin().models

add_model_access = CogContainer().add_model_access
kfp = KubeflowPlugin().kfp


def create_minio_client():
    """
    Creates a MinIO client object.

    Returns:
        Minio: The MinIO client object.
    """
    return DatasetPlugin().create_minio_client()


def query_endpoint_and_download_file(url, output_file, bucket_name):
    """
    Queries an endpoint and downloads a file from MinIO.

    Args:
        url (str): The URL to query.
        output_file (str): The output file path.
        bucket_name (str): The MinIO bucket name.

    Returns:
        bool: True if the file was successfully downloaded, False otherwise.
    """
    return DatasetPlugin().query_endpoint_and_download_file(
        url=url, output_file=output_file, bucket_name=bucket_name
    )


def save_to_minio(file_content, output_file, bucket_name):
    """
    Saves file content to MinIO.

    Args:
        file_content (bytes): The content of the file to save.
        output_file (str): The output file path.
        bucket_name (str): The MinIO bucket name.

    Returns:
        bool: True if the file was successfully saved, False otherwise.
    """
    return DatasetPlugin().save_to_minio(
        file_content=file_content, output_file=output_file, bucket_name=bucket_name
    )


def delete_from_minio(object_name, bucket_name):
    """
    Deletes an object from MinIO.

    Args:
        object_name (str): The name of the object to delete.
        bucket_name (str): The MinIO bucket name.

    Returns:
        bool: True if the object was successfully deleted, False otherwise.
    """
    return DatasetPlugin().delete_from_minio(object_name=object_name, bucket_name=bucket_name)


def register_dataset(details):
    """
    Registers a dataset with the given details.

    Args:
        details (dict): The details of the dataset to register.

    Returns:
        bool: True if the dataset was successfully registered, False otherwise.
    """
    return DatasetPlugin().register_dataset(details=details)


def delete_registered_model(model_name):
    """
    Deletes a registered model.

    Args:
        model_name (str): The name of the model to delete.

    Returns:
        bool: True if the model was successfully deleted, False otherwise.
    """
    return MlflowPlugin().delete_registered_model(model_name=model_name)


def evaluate(
    model=None,
    data=None,
    *,
    model_type=None,
    targets=None,
    predictions=None,
    dataset_path=None,
    feature_names=None,
    evaluators=None,
    evaluator_config=None,
    custom_metrics=None,
    extra_metrics=None,
    custom_artifacts=None,
    validation_thresholds=None,
    baseline_model=None,
    env_manager="local",
    model_config=None,
    baseline_config=None,
    inference_params=None
):
    """
    Evaluates a model.

    Args:
        model: The model to evaluate.
        data: The data to evaluate the model on.
        model_type: The type of the model.
        targets: The targets of the model.
        predictions: The predictions of the model.
        dataset_path: The path to the dataset.
        feature_names: The names of the features.
        evaluators: The evaluators to use.
        evaluator_config: The configuration for the evaluator.
        custom_metrics: Custom metrics to use.
        extra_metrics: Extra metrics to use.
        custom_artifacts: Custom artifacts to use.
        validation_thresholds: Validation thresholds to use.
        baseline_model: The baseline model to compare against.
        env_manager: The environment manager to use.
        model_config: The configuration for the model.
        baseline_config: The configuration for the baseline.
        inference_params: The parameters for inference.

    Returns:
        dict: The evaluation results.
    """
    return MlflowPlugin().evaluate(
        model=model,
        data=data,
        model_type=model_type,
        targets=targets,
        predictions=predictions,
        dataset_path=dataset_path,
        feature_names=feature_names,
        evaluators=evaluators,
        evaluator_config=evaluator_config,
        custom_metrics=custom_metrics,
        extra_metrics=extra_metrics,
        custom_artifacts=custom_artifacts,
        validation_thresholds=validation_thresholds,
        baseline_model=baseline_model,
        env_manager=env_manager,
        model_config=model_config,
        baseline_config=baseline_config,
    )


def search_registered_models():
    """
    Searches for registered models.

    Returns:
        List[str]: List of registered model names.
    """
    return MlflowPlugin().search_registered_models()


def load_model(model_uri: str, dst_path=None):
    """
    Loads a model from the specified URI.

    Args:
        model_uri (str): The URI of the model to load.
        dst_path (str, optional): The destination path to load the model to.

    Returns:
        Any: The loaded model object.
    """
    return MlflowPlugin().load_model(model_uri=model_uri, dst_path=dst_path)


def register_model(model, model_uri):
    """
    Registers a model with the specified URI.

    Args:
        model: The model to register.
        model_uri (str): The URI of the model to register.

    Returns:
        str: The registered model's ID.
    """
    return MlflowPlugin().register_model(model=model, model_uri=model_uri)


def autolog():
    """
    Enables automatic logging of parameters, metrics, and models.
    """
    return MlflowPlugin().autolog()


def create_registered_model(name):
    """
    Creates a new registered model.

    Args:
        name (str): The name of the model to register.

    Returns:
        str: The created model's name.
    """
    return MlflowPlugin().create_registered_model(name=name)


def create_model_version(name, source):
    """
    Creates a new version of a registered model.

    Args:
        name (str): The name of the model.
        source (str): The source path of the model.

    Returns:
        str: The created model version's ID.
    """
    return MlflowPlugin().create_model_version(name=name, source=source)


def set_tracking_uri(tracking_uri):
    """
    Sets the tracking URI for MLflow.

    Args:
        tracking_uri (str): The tracking URI to set.
    """
    return MlflowPlugin().set_tracking_uri(tracking_uri=tracking_uri)


def set_experiment(experiment_name):
    """
    Sets the experiment name for MLflow.

    Args:
        experiment_name (str): The name of the experiment to set.
    """
    return MlflowPlugin().set_experiment(experiment_name=experiment_name)


def get_artifact_uri(run_id=None):
    """
    Gets the artifact URI for the specified run ID.

    Args:
        run_id (str, optional): The run ID to get the artifact URI for.

    Returns:
        str: The artifact URI corresponding to the provided run ID.
    """
    return MlflowPlugin().get_artifact_uri(run_id=run_id)


def start_run(run_name=None):
    """
    Starts a new MLflow run.

    Args:
        run_name (str, optional): The name of the run to start.

    Returns:
        str: The ID of the started run.
    """
    return MlflowPlugin().start_run(run_name=run_name)


def end_run():
    """
    Ends the current MLflow run.

    Returns:
        str: The ID of the ended run.
    """
    return MlflowPlugin().end_run()


def log_param(key: str, value: Any, synchronous: bool = True):
    """
    Logs a parameter to the current run.

    Args:
        key (str): The key of the parameter.
        value (Any): The value of the parameter.
        synchronous (bool, optional): Whether to log synchronously. Defaults to True.
    """
    return MlflowPlugin().log_param(key=key, value=value, synchronous=synchronous)


def log_metric(
    key: str,
    value: float,
    step: Optional[int] = None,
    synchronous: Optional[bool] = None,
    timestamp: Optional[int] = None,
    run_id: Optional[str] = None,
):
    """
    Logs a metric to the current run.

    Args:
        key (str): The key of the metric.
        value (float): The value of the metric.
        step (int, optional): The step at which the metric was logged.
        synchronous (bool, optional): Whether to log synchronously.
        timestamp (int, optional): The timestamp of the metric.
        run_id (str, optional): The run ID to log the metric to.
    """
    return MlflowPlugin().log_metric(
        key=key,
        value=value,
        step=step,
        synchronous=synchronous,
        timestamp=timestamp,
        run_id=run_id,
    )


def log_model(
    sk_model,
    artifact_path,
    conda_env=None,
    code_paths=None,
    serialization_format="cloudpickle",
    registered_model_name=None,
    signature: ModelSignature = None,
    input_example: Union[
        pd.DataFrame,
        np.ndarray,
        dict,
        list,
        csr_matrix,
        csc_matrix,
        str,
        bytes,
        tuple,
    ] = None,
    await_registration_for=300,
    pip_requirements=None,
    extra_pip_requirements=None,
    pyfunc_predict_fn="predict",
    metadata=None,
):
    """
    Logs a model to MLflow.

    Args:
        sk_model: The scikit-learn model to log.
        artifact_path (str): The artifact path to log the model to.
        conda_env (str, optional): The conda environment to use.
        code_paths (list, optional): List of paths to include in the model.
        serialization_format (str, optional): The format to use for serialization.
        registered_model_name (str, optional): The name to register the model under.
        signature (ModelSignature, optional): The signature of the model.
        input_example (Union[pd.DataFrame, np.ndarray, dict, list, csr_matrix, csc_matrix, str, bytes, tuple], optional): Example input.
        await_registration_for (int, optional): Time to wait for registration.
        pip_requirements (list, optional): List of pip requirements.
        extra_pip_requirements (list, optional): List of extra pip requirements.
        pyfunc_predict_fn (str, optional): The prediction function to use.
        metadata (dict, optional): Metadata for the model.
    """
    return MlflowPlugin().log_model(
        sk_model=sk_model,
        artifact_path=artifact_path,
        conda_env=conda_env,
        code_paths=code_paths,
        serialization_format=serialization_format,
        registered_model_name=registered_model_name,
        signature=signature,
        input_example=input_example,
        await_registration_for=await_registration_for,
        pip_requirements=pip_requirements,
        extra_pip_requirements=extra_pip_requirements,
        pyfunc_predict_fn=pyfunc_predict_fn,
        metadata=metadata,
    )


def log_model_with_dataset(
    sk_model,
    artifact_path,
    dataset: DatasetMetadata,
    conda_env=None,
    code_paths=None,
    serialization_format="cloudpickle",
    registered_model_name=None,
    signature: ModelSignature = None,
    input_example: Union[
        pd.DataFrame,
        np.ndarray,
        dict,
        list,
        csr_matrix,
        csc_matrix,
        str,
        bytes,
        tuple,
    ] = None,
    await_registration_for=300,
    pip_requirements=None,
    extra_pip_requirements=None,
    pyfunc_predict_fn="predict",
    metadata=None,
):
    """
    Logs a model along with its dataset to MLflow.

    Args:
        sk_model: The scikit-learn model to log.
        artifact_path (str): The artifact path to log the model to.
        dataset (DatasetMetadata): The dataset metadata.
        conda_env (str, optional): The conda environment to use.
        code_paths (list, optional): List of paths to include in the model.
        serialization_format (str, optional): The format to use for serialization.
        registered_model_name (str, optional): The name to register the model under.
        signature (ModelSignature, optional): The signature of the model.
        input_example (Union[pd.DataFrame, np.ndarray, dict, list, csr_matrix, csc_matrix, str, bytes, tuple], optional): Example input.
        await_registration_for (int, optional): Time to wait for registration.
        pip_requirements (list, optional): List of pip requirements.
        extra_pip_requirements (list, optional): List of extra pip requirements.
        pyfunc_predict_fn (str, optional): The prediction function to use.
        metadata (dict, optional): Metadata for the model.
    """
    return MlflowPlugin().log_model_with_dataset(
        sk_model=sk_model,
        artifact_path=artifact_path,
        dataset=dataset,
        conda_env=conda_env,
        code_paths=code_paths,
        serialization_format=serialization_format,
        registered_model_name=registered_model_name,
        signature=signature,
        input_example=input_example,
        await_registration_for=await_registration_for,
        pip_requirements=pip_requirements,
        extra_pip_requirements=extra_pip_requirements,
        pyfunc_predict_fn=pyfunc_predict_fn,
        metadata=metadata,
    )


def link_model_to_dataset(dataset_id, model_id):
    """
    Links a model to a dataset.

    Args:
        dataset_id (str): The ID of the dataset.
        model_id (str): The ID of the model.
    """
    return MlflowPlugin().link_model_to_dataset(dataset_id=dataset_id, model_id=model_id)


def save_dataset_details(dataset):
    """
    Saves dataset details.

    Args:
        dataset: The dataset details to save.

    Returns:
        str: Information message confirming the dataset details are saved.
    """
    return MlflowPlugin().save_dataset_details(dataset=dataset)


def save_model_details_to_db(registered_model_name):
    """
    Saves model details to the database.

    Args:
        registered_model_name (str): The name of the registered model.

    Returns:
        str: Information message confirming the model details are saved.
    """
    return MlflowPlugin().save_model_details_to_db(registered_model_name=registered_model_name)


def get_model_latest_version(registered_model_name):
    """
    Gets the latest version of a registered model.

    Args:
        registered_model_name (str): The name of the registered model.

    Returns:
        str: The latest version of the registered model.
    """
    return MlflowPlugin().get_model_latest_version(registered_model_name=registered_model_name)


def search_model_versions(
        filter_string: Optional[str] = None,
        order_by: Optional[List[str]] = None,
):
    """
    Searches for versions of a model.

    Args:
        filter_string (str, optional): The filter string to use.
        order_by (list, optional): List of fields to order by.

    Returns:
        List: List of model versions that match the search criteria.
    """
    return MlflowPlugin().search_model_versions(filter_string=filter_string, order_by=order_by)


def pipeline(name=None, description=None):
    """
    Creates a new Kubeflow pipeline.

    Args:
        name (str, optional): The name of the pipeline.
        description (str, optional): The description of the pipeline.

    Returns:
        str: Information message confirming the pipeline creation.
    """
    return KubeflowPlugin().pipeline(name=name, description=description)


def create_component_from_func(
        func,
        output_component_file=None,
        base_image=None,
        packages_to_install=None,
):
    """
    Creates a Kubeflow component from a function.

    Args:
        func: The function to create the component from.
        output_component_file (str, optional): The output file for the component.
        base_image (str, optional): The base image to use.
        packages_to_install (list, optional): List of packages to install.

    Returns:
        str: Information message confirming the component creation.
    """
    return KubeflowPlugin().create_component_from_func(
        func=func,
        output_component_file=output_component_file,
        base_image=base_image,
        packages_to_install=packages_to_install,
    )


def client():
    """
    Gets the Kubeflow client.

    Returns:
        KubeflowClient: The Kubeflow client object.
    """
    return KubeflowPlugin().client()


def load_component_from_url(url):
    """
    Loads a Kubeflow component from a URL.

    Args:
        url (str): The URL to load the component from.

    Returns:
        Component: The loaded Kubeflow component.
    """
    return KubeflowPlugin().load_component_from_url(url=url)


def input_path(label: str):
    """
    Gets the input path for a Kubeflow component.

    Args:
        label (str): The label for the input path.

    Returns:
        str: The input path.
    """
    return KubeflowPlugin().input_path(label=label)


def output_path(label: str):
    """
    Gets the output path for a Kubeflow component.

    Args:
        label (str): The label for the output path.

    Returns:
        str: The output path.
    """
    return KubeflowPlugin().output_path(label=label)


def serve_model_v2(model_uri: str, name: str = None):
    """
    Serves a model using Kubeflow V2.

    Args:
        model_uri (str): The URI of the model to serve.
        name (str, optional): The name of the model to serve.

    Returns:
        str: Information message confirming the model serving.
    """
    return KubeflowPlugin().serve_model_v2(model_uri=model_uri, name=name)


def serve_model_v1(model_uri: str, name: str = None):
    """
    Serves a model using Kubeflow V1.

    Args:
        model_uri (str): The URI of the model to serve.
        name (str, optional): The name of the model to serve.

    Returns:
        str: Information message confirming the model serving.
    """
    return KubeflowPlugin().serve_model_v2(model_uri=model_uri, name=name)


def get_model_url(model_name: str):
    """
    Gets the URL of a served model.

    Args:
        model_name (str): The name of the served model.

    Returns:
        str: The URL of the served model.
    """
    return KubeflowPlugin().get_model_url(model_name=model_name)


def delete_served_model(model_name: str):
    """
    Deletes a served model.

    Args:
        model_name (str): The name of the model to delete.

    Returns:
        str: Information message confirming the deletion of the served model.
    """
    return KubeflowPlugin().delete_served_model(model_name=model_name)


__all__ = [
    # Methods from MlflowPlugin class
    "pyfunc",
    "mlflow",
    "sklearn",
    "cogclient",
    "tensorflow",
    "pytorch",
    "models",
    # Method from CogContainer class
    "add_model_access",
    "kfp",
]
