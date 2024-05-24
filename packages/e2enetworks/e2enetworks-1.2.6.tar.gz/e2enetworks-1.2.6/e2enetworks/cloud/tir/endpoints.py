import json
from typing import Optional

import requests

from e2enetworks.cloud.tir.skus import Plans, client
from e2enetworks.cloud.tir.helpers import plan_to_sku_id
from e2enetworks.cloud.tir.utils import prepare_object
from e2enetworks.constants import (BASE_GPU_URL, INFERENCE, PYTORCH, TRITON,TENSORRT,PRIVATE,REGISTRY,
                                   headers, TIR_CUSTOM_FRAMEWORKS)

containers = {
    "llma": "registry.e2enetworks.net/aimle2e/meta-7b",
    "llma_eos": "registry.e2enetworks.net/aimle2e/meta-7b-chat",
    "codellama": "registry.e2enetworks.net/aimle2e/codellama",
    "codellama_eos": "registry.e2enetworks.net/aimle2e/codellama-eos",
    "mpt": "registry.e2enetworks.net/aimle2e/mpt-7b-chat:hf-v3",
    "mpt_eos": "registry.e2enetworks.net/aimle2e/mpt-7b-chat:eos-v2",
    "stable_diffusion": "registry.e2enetworks.net/aimle2e/stable-diffusion-2-1:hf-v1",
    "stable_diffusion_eos": "registry.e2enetworks.net/aimle2e/stable-diffusion-2-1:eos-v1"
}


class EndPoints:
    def __init__(
            self,
            team: Optional[str] = "",
            project: Optional[str] = ""
    ):
        client_not_ready = (
            "Client is not ready. Please initiate client by:"
            "\n- Using e2enetworks.cloud.tir.init(...)"
        )
        if not client.Default.ready():
            raise ValueError(client_not_ready)

        if project:
            client.Default.set_project(project)

        if team:
            client.Default.set_team(team)

    def list_plans(self,framework):
        if framework not in TIR_CUSTOM_FRAMEWORKS:
            raise ValueError(f"framework {framework} is not supported. framework should be one of: %s" % TIR_CUSTOM_FRAMEWORKS)
        return Plans().list_endpoint_plans(framework=framework)
    
    def list_frameworks(self):
        print(TIR_CUSTOM_FRAMEWORKS)
        return TIR_CUSTOM_FRAMEWORKS


    def get_container_name(self, container_name, model_id, framework):
        if framework == "custom":
            return container_name
        if model_id:
            return containers[framework+'_eos'] if framework+'_eos' in containers else None
        else:
            return containers[framework] if framework in containers else None

    def create_triton(self, endpoint_name, plan, server_version, model_id=None, container_name=None, container_type="public",
                                        model_path='', is_auto_scale_enabled=False, 
                                        metric="cpu", replicas=1, commands=[], value=12, disk_size=30, env_variables=[], 
                                        world_size=1, mount_path='', min_replicas=1, max_replicas=2):
        if not endpoint_name:
            raise ValueError(endpoint_name)
        if not plan:
            raise ValueError(plan)
        if not model_id:
            raise ValueError(model_id)
        
        args=[
                "mpirun",
                "--allow-run-as-root",
                "-n",
                "3",
                "tritonserver",
                "--exit-on-error=false",
                "--model-store=/mnt/models",
                "--grpc-port=9000",
                "--http-port=8080",
                "--metrics-port=8082",
                "--allow-grpc=true",
                "--allow-http=true"
            ]

        return self.create_inference_for_framework(endpoint_name=endpoint_name,
                                                   plan=plan,
                                                   model_path=model_path,
                                                   model_id=model_id,
                                                   server_version=server_version,
                                                   commands=commands,
                                                   value=value,
                                                   disk_size=disk_size,
                                                   env_variables=env_variables,
                                                   world_size=world_size,
                                                   mount_path=mount_path,
                                                   min_replicas=min_replicas,
                                                   max_replicas=max_replicas,
                                                   replicas=replicas,
                                                   framework=TRITON,
                                                   container_name=container_name,
                                                   container_type=container_type,
                                                   metric=metric,
                                                   args=args,
                                                   is_auto_scale_enabled=is_auto_scale_enabled)
    
    def create_tensorrt(self, endpoint_name, plan, server_version, HF_TOKEN, model_id=None, container_name=None, container_type="public",
                                        model_path='', is_auto_scale_enabled=False, 
                                        metric="cpu", replicas=1, commands=[], value=12, disk_size=30, env_variables=[], 
                                        world_size=1, mount_path='', min_replicas=1, max_replicas=2):
        if not endpoint_name:
            raise ValueError(endpoint_name)
        if not plan:
            raise ValueError(plan)
        if not model_id:
            raise ValueError(model_id)
        
        new_env_variable = {
        "key": "HF_TOKEN",
        "value": HF_TOKEN,
        "required": False,
        "disabled": {
            "key": True,
            "value": False
        }
        }
        env_variables.append(new_env_variable)
        
        args=[
                "mpirun",
                "--allow-run-as-root",
                "-n",
                "3",
                "tritonserver",
                "--exit-on-error=false",
                "--model-store=/mnt/models",
                "--grpc-port=9000",
                "--http-port=8080",
                "--metrics-port=8082",
                "--allow-grpc=true",
                "--allow-http=true"
            ]

        return self.create_inference_for_framework(endpoint_name=endpoint_name,
                                                   plan=plan,
                                                   model_path=model_path,
                                                   model_id=model_id,
                                                   server_version=server_version,
                                                   commands=commands,
                                                   value=value,
                                                   disk_size=disk_size,
                                                   env_variables=env_variables,
                                                   world_size=world_size,
                                                   mount_path=mount_path,
                                                   min_replicas=min_replicas,
                                                   max_replicas=max_replicas,
                                                   replicas=replicas,
                                                   framework=TENSORRT,
                                                   container_name=container_name,
                                                   container_type=container_type,
                                                   metric=metric,
                                                   args=args,
                                                   is_auto_scale_enabled=is_auto_scale_enabled)

    def create_pytorch(self, endpoint_name, plan, server_version, model_id=None, container_name=None, container_type="public",
                                        model_path='', is_auto_scale_enabled=False, 
                                        metric="cpu", replicas=1, commands=[], value=12, disk_size=30, env_variables=[], 
                                        world_size=1, mount_path='', min_replicas=1, max_replicas=2):
        if not endpoint_name:
            raise ValueError(endpoint_name)
        if not plan:
            raise ValueError(plan)
        if not model_id:
            raise ValueError(model_id)
        
        args=[
        "torchserve",
        "--start",
        "--model-store=/mnt/models/model-store",
        "--ts-config=/mnt/models/config/config.properties"
    ]

        return self.create_inference_for_framework(endpoint_name=endpoint_name,
                                                   container_name=container_name,
                                                   container_type=container_type,
                                                   server_version=server_version,
                                                   metric=metric,
                                                   args=args,
                                                   commands=commands,
                                                   value=value,
                                                   disk_size=disk_size,
                                                   env_variables=env_variables,
                                                   world_size=world_size,
                                                   mount_path=mount_path,
                                                   min_replicas=min_replicas,
                                                   max_replicas=max_replicas,
                                                   plan=plan,
                                                   model_path=model_path,
                                                   model_id=model_id,
                                                   replicas=replicas,
                                                   framework=PYTORCH,
                                                   is_auto_scale_enabled=is_auto_scale_enabled)

    def create_inference_for_framework(self, endpoint_name, container_name, container_type, plan,
                                        model_path, model_id, framework, is_auto_scale_enabled, 
                                        args, server_version="", metric="cpu", replicas=1, commands=[], value=12, disk_size=30, env_variables=[], 
                                        world_size=1, mount_path='', min_replicas=1, max_replicas=2):
        skus = Plans().get_skus_list(INFERENCE)
        sku_id = plan_to_sku_id(skus=skus, plan=plan)

        if not sku_id:
            raise ValueError(plan)
        

        payload = json.dumps({
            "name": endpoint_name or "",
            "path": model_path,
            "custom_endpoint_details": {
                "container": {
                    "container_name": container_name,
                    "container_type": container_type,
                    },
                "public_ip": "no",
                "resource_details": {
                    "disk_size": disk_size,
                    "env_variables": env_variables,
                    "mount_path": mount_path
                }
            },
            "model_id": model_id,
            "sku_id": sku_id,
            "replica": replicas,
            "framework": framework,
            "server_version": server_version,
            "is_auto_scale_enabled": is_auto_scale_enabled,
            "world_size": world_size,
            "detailed_info":{
                "args": args,
                "commands": commands,
            }
        })

        new_payload = json.loads(payload)
        
        if is_auto_scale_enabled:
            rules = [
                {
                    "metric": metric,
                    "condition_type": "limit",
                    "value": value,
                    "watch_period": "60"
                }
            ]
            
            auto_scale_policy = {
                "min_replicas": min_replicas,
                "max_replicas": max_replicas,
                "rules": rules,
                "stability_period": "300"
            }

            new_payload["auto_scale_policy"] = auto_scale_policy

        payload = json.dumps(new_payload)




           

        headers['Authorization'] = f'Bearer {client.Default.access_token()}'
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/serving/inference/?" \
              f"apikey={client.Default.api_key()}"
        response = requests.post(url=url, headers=headers, data=payload)
        print(f"To check the Inference Status and logs, PLease visit "
              f"https://gpu-notebooks.e2enetworks.com/projects/{client.Default.project()}/model-endpoints")
        return prepare_object(response)
    
    def registry_namespace_list(self):
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/container_registry/"
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return prepare_object(response)
    
    def registry_detail(self, registry_namespace_id):
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/container_registry/{registry_namespace_id}/namespace-repository/"
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def create(self, endpoint_name, framework, plan, is_auto_scale_enabled=False, 
               registry_namespace_id=None, model_id=None, container_name=None, container_type="public",command=[],args=[],
               replicas=1, server_version="", disc_size=30, world_size=1, model_path="", env_variables=[], mount_path="", metric="cpu", value=12, min_replicas=1,max_replicas=2):
        if not endpoint_name:
            raise ValueError(endpoint_name)
        if not framework:
            raise ValueError(framework)
        if not plan:
            raise ValueError(plan)

        skus = Plans().get_skus_list(INFERENCE)
        sku_id = plan_to_sku_id(skus=skus, plan=plan)

        if not sku_id:
            raise ValueError(plan)

        container_name = self.get_container_name(container_name=container_name, model_id=model_id, framework=framework)

        if framework not in ["pytorch", "triton", "tensorrt"] and not container_name:
            raise ValueError(container_name)
        
        private_image_details={}
        if container_type == PRIVATE :
            private_image_details = {"registry_namespace_id": registry_namespace_id}
            container_name = REGISTRY+"/"+container_name
        

        payload = json.dumps({
            "name": endpoint_name or "",
            "path": model_path,
            "custom_endpoint_details": {
                "container": {
                    "container_name": container_name,
                    "container_type": container_type,
                    "private_image_details": private_image_details
                },
                "public_ip": "no",
                "resource_details": {
                    "disk_size": disc_size,
                    "mount_path": mount_path,
                    "env_variables": env_variables
                },
            },
            "detailed_info": {
                "command": command,
                "args": args,
            },
            "model_id": model_id,
            "is_auto_scale_enabled": is_auto_scale_enabled,
            "sku_id": sku_id,
            "replica": replicas or 1,
            "framework": framework,
            "world_size": world_size,
            "server_version=": server_version
        })

        new_payload = json.loads(payload)
        
        if is_auto_scale_enabled:
            rules = [
                {
                    "metric": metric,
                    "condition_type": "limit",
                    "value": value,
                    "watch_period": "60"
                }
            ]
            
            auto_scale_policy = {
                "min_replicas": min_replicas,
                "max_replicas": max_replicas,
                "rules": rules,
                "stability_period": "300"
            }

            new_payload["auto_scale_policy"] = auto_scale_policy

        payload = json.dumps(new_payload)

        headers['Authorization'] = f'Bearer {client.Default.access_token()}'
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/serving/inference/?" \
              f"apikey={client.Default.api_key()}"
        response = requests.post(url=url, headers=headers, data=payload)
        print(f"To check the Inference Status and logs, PLease visit "
              f"https://gpu-notebooks.e2enetworks.com/projects/{client.Default.project()}/model-endpoints")
        return prepare_object(response)

    def get(self, endpoint_id):

        if type(endpoint_id) != int:
            raise ValueError(endpoint_id)

        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/serving/inference/" \
              f"{endpoint_id}/"
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def logs(self, endpoint_id):

        if type(endpoint_id) != int:
            raise ValueError(endpoint_id)

        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/serving/inference/" \
              f"{endpoint_id}/logs/"
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def start(self, endpoint_id):
        payload = json.dumps({
            "action": "start"
        })
        if type(endpoint_id) != int:
            raise ValueError(endpoint_id)
        headers['Authorization'] = f'Bearer {client.Default.access_token()}'
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/serving/inference/" \
              f"{endpoint_id}/"
        req = requests.Request('PUT', url=url, data=payload, headers=headers)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def stop(self, endpoint_id):
        payload = json.dumps({
            "action": "stop"
        })
        if type(endpoint_id) != int:
            raise ValueError(endpoint_id)
        headers['Authorization'] = f'Bearer {client.Default.access_token()}'
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/serving/inference/" \
              f"{endpoint_id}/"
        req = requests.Request('PUT', url=url, data=payload, headers=headers)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def list(self):
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/serving/inference/"
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def delete(self, endpoint_id):
        if type(endpoint_id) != int:
            raise ValueError(endpoint_id)

        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/serving/inference/" \
              f"{endpoint_id}/"
        req = requests.Request('DELETE', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    @staticmethod
    def help():
        print("EndPoint Class Help")
        print("\t\t=================")
        print("\t\tThis class provides functionalities to interact with EndPoint.")
        print("\t\tAvailable methods:")
        print("\t\t1. __init__(team, project): Initializes an EndPoints instance with the specified team and "
              "project IDs.")
        print("\t\t2. list_plans()")
        print("\t\t3. create_triton(endpoint_name, plan, model_id, model_path='', replicas=1)")
        print("\t\t4. create_pytorch(endpoint_name, plan, model_id, model_path='', replicas=1)")
        print("\t\t5. create(endpoint_name, framework, plan, container_name, container_type, model_id, replicas=1, "
              "disc_size=10, model_path="", env_variables=[], mount_path="", registry_endpoint="", "
              "auth_type='pass', username="", password="", docker_config=""): "
              "Creates an endpoint with the provided details.")
        print("\t\t6. get(endpoint_id): Retrieves information about a specific endpoint using its ID.")
        print("\t\t7. logs(endpoint_id): Retrieves logs of a specific endpoint using its ID.")
        print("\t\t8. stop(endpoint_id): Stops a specific endpoint using its ID.")
        print("\t\t9. start(endpoint_id): Starts a specific endpoint using its ID.")
        print("\t\t10. list(): Lists all endpoints associated with the team and project.")
        print("\t\t11. delete(endpoint_id): Deletes an endpoint with the given ID.")
        print("\t\t12. help(): Displays this help message.")

        # Example usages
        print("\t\tExample usages:")
        print("\t\tendpoints = EndPoints(123, 456)")
        print("\t\tendpoints.create("
              "\n\t\t\t\tendpoint_name(required):String => 'Name of Endpoint'",
              "\n\t\t\t\tframework(required):String => '['triton', 'pytorch', 'llma', 'stable_diffusion', 'mpt,"
              "\n\t\t\t\t\t'codellama', 'custom']'",
              "\n\t\t\t\tplan(required):String=> Plans Can be listed using tir.Plans Apis",
              "\n\t\t\t\tcontainer_type(optional):String=> Default value is public and "
              "\n\t\t\t\t\tallowed values are [public, private]",
              "\n\t\t\t\tmodel_id:Integer=> Required in case of Framework type=[triton, pytorch] and "
              "\n\t\t\t\t\tif model is stored in EOS",
              "\n\t\t\t\tcontainer_name(optional):String=> Docker Container Image Name required in case of Custom "
              "\n\t\t\t\tContainer Only",
              "\n\t\t\t\treplicas(optional):Integer=> Default value id 1",
              "\n\t\t\t\tdisc_size(optional):Integer=> Default value id 10Gb",
              "\n\t\t\t\tmodel_path(optional):String=> Path of EOS bucket where the model is stored",
              "\n\t\t\t\tenv_variables(optional):List=> Env variables can be passed as "
              "\n\t\t\t\t\t[{ 'key': '', 'value': '/mnt/models'}]"
              "\n\t\t\t\tmount_path(optional):String=> Default value is '/mnt/models'"
              "\n\t\t\t\tregistry_endpoint(optional):String=> Required in Case of container_type=private"
              "\n\t\t\t\tauth_type(optional):String=> Required in case of container_type=private, "
              "\n\t\t\t\t\tAllowed Values are ['pass', 'docker'] "
              "\n\t\t\t\t\tDefault Value is pass'"
              "\n\t\t\t\tusername(optional):String=> Required in case of container_type=private and auth_type=pass"
              "\n\t\t\t\tusername(optional):String=> Required in case of container_type=private and auth_type=pass"
              "\n\t\t\t\tdocker_config(optional):String=> Required in case of container_type=private and "
              "auth_type=docker")
        print("\t\tendpoints.get(789)")
        print("\t\tendpoints.logs(789)")
        print("\t\tendpoints.stop(789)")
        print("\t\tendpoints.start(789)")
        print("\t\tendpoints.list()")
        print("\t\tendpoints.delete(789)")
