from kubernetes import client, config
from kubernetes.client.rest import ApiException


def create_config_map(namespace, config_map_name, data):
    # Load kubeconfig
    config.load_kube_config()

    # Create an instance of the API class
    api_instance = client.CoreV1Api()


    # Define the metadata for the ConfigMap
    metadata = client.V1ObjectMeta(name=config_map_name)

    # Define the body of the ConfigMap
    config_map = client.V1ConfigMap(
        api_version="v1",
        kind="ConfigMap",
        metadata=metadata,
        data=data
    )

    try:
        # Create the ConfigMap in the specified namespace
        api_response = api_instance.create_namespaced_config_map(
            namespace=namespace,
            body=config_map
        )
        print("ConfigMap created.")
    # except ApiException as e:
    #     print("Exception when creating ConfigMap: %s\n" % e)
    except Exception as e:
        raise e


def update_config_map(namespace, config_map_name, data):
    try:
        # Load kubeconfig
        config.load_kube_config()

        # Create an instance of the API class
        api_instance = client.CoreV1Api()

        # Fetch the existing ConfigMap
        existing_config_map = api_instance.read_namespaced_config_map(
            name=config_map_name,
            namespace=namespace
        )

        # Convert all values to strings
        string_data = {k: str(v) for k, v in data.items()}
        
        # Replace the data in the ConfigMap with the new data
        existing_config_map.data = string_data
        # Update the data in the ConfigMap
        # existing_config_map.data.update(data)

        # Send the updated ConfigMap to the API
        api_response = api_instance.replace_namespaced_config_map(
            name=config_map_name,
            namespace=namespace,
            body=existing_config_map
        )
        print("ConfigMap updated.")
    # except ApiException as e:
    #     if e.status == 404:
    #         print(f"ConfigMap {config_map_name} not found in namespace {namespace}.")
    #     else:
    #         print("Exception when updating ConfigMap: %s\n" % e)
    except Exception as e:
        raise e

