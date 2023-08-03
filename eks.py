#create deployment and service
from kubernetes import client, config

# Load Kubernetes configuration
config.load_kube_config()

# Create a Kubernetes API client
api_client = client.ApiClient()

# Define the deployment
deployment = client.V1Deployment(
    metadata=client.V1ObjectMeta(name="flaskapp"),
    spec=client.V1DeploymentSpec(
        replicas=1,
        selector=client.V1LabelSelector(
            match_labels={"app": "flaskapp2"}
        ),
        template=client.V1PodTemplateSpec(
            metadata=client.V1ObjectMeta(
                labels={"app": "flaskapp2"}
            ),
            spec=client.V1PodSpec(
                containers=[
                    client.V1Container(
                        name="flask-container2",
                        image="775495980804.dkr.ecr.us-east-1.amazonaws.com/cloud-native-monitoring-app",
                        ports=[client.V1ContainerPort(container_port=5000)]
                    )
                ]
            )
        )
    )
)

# Create the deployment
api_instance = client.AppsV1Api(api_client)
api_instance.create_namespaced_deployment(
    namespace="default",
    body=deployment
)


# Define the service
service = client.V1Service(
    metadata=client.V1ObjectMeta(name="flaskservice"),
    spec=client.V1ServiceSpec(
        selector={"app": "flaskapp2"},
        ports=[client.V1ServicePort(port=5000)]
    )
)

# Create the service
api_instance = client.CoreV1Api(api_client)
api_instance.create_namespaced_service(
    namespace="default",
    body=service
)