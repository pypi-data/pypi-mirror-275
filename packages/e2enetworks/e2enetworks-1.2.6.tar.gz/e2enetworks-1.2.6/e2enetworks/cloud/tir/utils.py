import yaml
import json
from typing import Dict, Any
from requests import Response
from types import SimpleNamespace


def load_yaml(
        path: str,
) -> Dict[str, Any]:
    _load_from_local(path)


def _load_from_local(path: str) -> Dict[str, Any]:
    with open(path) as f:
        return yaml.safe_load(f)


def load_json(b: bytes, object_hook=None) -> Dict:
    return json.loads(b, object_hook=object_hook)


def prepare_object(response: Response):
    if not response.ok:
        try:
            output = response.json()
        except:
            output = response.reason
        print("ERROR:", output.get('errors'))
        return response.json().get('errors')
    
    flag = response.json().get('data')
    response = load_json(response.content, object_hook=lambda d: SimpleNamespace(**d))
    return response.data if hasattr(response, "data") and flag  else response.message


def prepare_response(response: Response) -> Dict:
    if response.ok:
        return load_json(response.content)

    # logger.error("")
    print("api call failed with error:", response.reason)
    return {
        "error": response.reason
    }
