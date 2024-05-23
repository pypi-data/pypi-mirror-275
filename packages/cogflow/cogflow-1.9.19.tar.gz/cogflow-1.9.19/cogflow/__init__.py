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
    DatasetPlugin().create_minio_client()


def query_endpoint_and_download_file(url, output_file, bucket_name):
    DatasetPlugin().query_endpoint_and_download_file(
        url=url, output_file=output_file, bucket_name=bucket_name
    )


def save_to_minio(file_content, output_file, bucket_name):
    DatasetPlugin().save_to_minio(
        file_content=file_content, output_file=output_file, bucket_name=bucket_name
    )


def delete_from_minio(object_name, bucket_name):
    DatasetPlugin().delete_from_minio(object_name=object_name, bucket_name=bucket_name)


def register_dataset(details):
    DatasetPlugin().register_dataset(details=details)


def delete_registered_model(model_name):
    MlflowPlugin().delete_registered_model(model_name=model_name)


def search_registered_models():
    MlflowPlugin().search_registered_models()


def load_model(model_uri: str, dst_path=None):
    MlflowPlugin().load_model(model_uri=model_uri, dst_path=dst_path)


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
    MlflowPlugin().evaluate(
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
        inference_params=inference_params,
    )


def register_model(model, model_uri):
    MlflowPlugin().register_model(model=model, model_uri=model_uri)


def autolog():
    MlflowPlugin().autolog()


def create_registered_model(name):
    MlflowPlugin().create_registered_model(name=name)


def create_model_version(name, source):
    MlflowPlugin().create_model_version(name=name, source=source)


def set_tracking_uri(tracking_uri):
    MlflowPlugin().set_tracking_uri(tracking_uri=tracking_uri)


def set_experiment(experiment_name):
    MlflowPlugin().set_experiment(experiment_name=experiment_name)


def get_artifact_uri(run_id=None):
    MlflowPlugin().get_artifact_uri(run_id=run_id)


def start_run(run_name=None):
    MlflowPlugin().start_run(run_name=run_name)


def end_run():
    MlflowPlugin().end_run()


def log_param(key: str, value: Any, synchronous: bool = True):
    MlflowPlugin().log_param(key=key, value=value, synchronous=synchronous)


def log_metric(
    key: str,
    value: float,
    step: Optional[int] = None,
    synchronous: Optional[bool] = None,
    timestamp: Optional[int] = None,
    run_id: Optional[str] = None,
):
    MlflowPlugin().log_metric(
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
    MlflowPlugin().log_model(
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
    MlflowPlugin().log_model_with_dataset(
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
    MlflowPlugin().link_model_to_dataset(dataset_id=dataset_id, model_id=model_id)


def save_dataset_details(dataset):
    MlflowPlugin().save_dataset_details(dataset=dataset)


def save_model_details_to_db(registered_model_name):
    MlflowPlugin().save_model_details_to_db(registered_model_name=registered_model_name)


def get_model_latest_version(registered_model_name):
    MlflowPlugin().get_model_latest_version(registered_model_name=registered_model_name)


def search_model_versions(
    filter_string: Optional[str] = None,
    order_by: Optional[List[str]] = None,
):
    MlflowPlugin().search_model_versions(filter_string=filter_string, order_by=order_by)


def pipeline(name=None, description=None):
    KubeflowPlugin().pipeline(name=name, description=description)


def create_component_from_func(
    func,
    output_component_file=None,
    base_image=None,
    packages_to_install=None,
):
    KubeflowPlugin().create_component_from_func(
        func=func,
        output_component_file=output_component_file,
        base_image=base_image,
        packages_to_install=packages_to_install,
    )


def client():
    KubeflowPlugin().client()


def load_component_from_url(url):
    KubeflowPlugin().load_component_from_url(url=url)


def input_path(label: str):
    KubeflowPlugin().input_path(label=label)


def output_path(label: str):
    KubeflowPlugin().output_path(label=label)


def serve_model_v2(model_uri: str, name: str = None):
    KubeflowPlugin().serve_model_v2(model_uri=model_uri, name=name)


def serve_model_v1(model_uri: str, name: str = None):
    KubeflowPlugin().serve_model_v2(model_uri=model_uri, name=name)


def get_model_url(model_name: str):
    KubeflowPlugin().get_model_url(model_name=model_name)


def delete_served_model(model_name: str):
    KubeflowPlugin().delete_served_model(model_name=model_name)


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
