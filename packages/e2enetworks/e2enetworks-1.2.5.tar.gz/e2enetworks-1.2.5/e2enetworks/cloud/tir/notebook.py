import json
from typing import Optional

import requests

from e2enetworks.cloud.tir.helpers import plan_name_to_sku_item_price_id
from e2enetworks.cloud.tir.skus import Plans, client
from e2enetworks.cloud.tir.utils import prepare_object
from e2enetworks.constants import (BASE_GPU_URL, INSTANCE_TYPE, NOTEBOOK,
                                   PAID_USAGE, headers)


class Notebooks:
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

    def create(self, name, plan_name, image_id, disk_size_in_gb=30, notebook_type="new", notebook_url=""):
        skus, skus_table = Plans().get_plans_list(NOTEBOOK, image_id)
        payload = json.dumps({
            "name": name,
            "image_id": image_id,
            "sku_item_price_id": plan_name_to_sku_item_price_id(skus, plan_name),
            "auto_shutdown_timeout": None,
            "instance_type": PAID_USAGE,
            "dataset_id_list": [],
            "disk_size_in_gb": disk_size_in_gb,
            "notebook_type": notebook_type,
            "notebook_url": notebook_url
        })
        headers['Authorization'] = f'Bearer {client.Default.access_token()}'
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/notebooks/?" \
              f"apikey={client.Default.api_key()}"
        response = requests.post(url=url, headers=headers, data=payload)
        return prepare_object(response)

    def get(self, notebook_id):

        if type(notebook_id) != int:
            raise ValueError(notebook_id)

        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/notebooks/" \
              f"{notebook_id}/"
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def list(self):

        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/notebooks/"
        req = requests.Request('GET', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def delete(self, notebook_id):
        if type(notebook_id) != int:
            raise ValueError(notebook_id)

        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/notebooks/" \
              f"{notebook_id}/"
        req = requests.Request('DELETE', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def stop(self, notebook_id):
        if type(notebook_id) != int:
            raise ValueError(notebook_id)

        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/notebooks/" \
              f"{notebook_id}/actions/?action=stop&"
        req = requests.Request('PUT', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def start(self, notebook_id):
        if type(notebook_id) != int:
            raise ValueError(notebook_id)

        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/notebooks/" \
              f"{notebook_id}/actions/?action=start&"
        req = requests.Request('PUT', url)
        response = client.Default.make_request(req)
        return prepare_object(response)

    def upgrade(self, notebook_id, size):
        if type(notebook_id) != int:
            raise ValueError(notebook_id)

        if type(size) != int:
            raise ValueError(notebook_id)

        payload = json.dumps({
            "size": size})
        headers['Authorization'] = f'Bearer {client.Default.access_token()}'
        url = f"{BASE_GPU_URL}teams/{client.Default.team()}/projects/{client.Default.project()}/notebooks/" \
              f"{notebook_id}/pvc/upgrade/?apikey={client.Default.api_key()}"
        response = requests.put(url=url, headers=headers, data=payload)
        return prepare_object(response)

    @staticmethod
    def help():
        print("\t\tNotebook Class Help")
        print("\t\t=================")
        help_text = f"""
                Notebooks class provides methods to interact with notebooks in a project.

                Available methods:
                1. create(
                    name(required):String, 
                    plan(required):String=> Plans Can be listed using tir. Plans Apis",
                    image_id(required), 
                    instance_type={INSTANCE_TYPE}, 
                    disk_size_in_gb=30,
                    notebook_type="new",
                    notebook_url="")
                2. get(notebook_id): Get information about a notebook.
                3. list(): List all notebooks in the project.
                4. delete(notebook_id): Delete a notebook.
                5. stop(notebook_id): Stop a running notebook.
                6. start(notebook_id): Start a stopped notebook.
                7. upgrade(notebook_id, size): Upgrade the size of a notebook's PVC.

                Usage:
                notebooks = Notebooks(team, project)
                notebooks.create("test-notebook", "CPU-C3-4-8GB-0", 9, 
                    instance_type="paid_usage", 
                    disk_size_in_gb=30,
                    notebook_type="new",
                    notebook_url="")
                notebooks.get(notebook_id)
                notebooks.list()
                notebooks.delete(notebook_id)
                notebooks.stop(notebook_id)
                notebooks.start(notebook_id)
                notebooks.upgrade(notebook_id, size)
                """
        print(help_text)
