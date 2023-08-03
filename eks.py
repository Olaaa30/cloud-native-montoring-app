from kubernetes import client, config

config.load_kube_config()

api_client = clieint.ApiClient()