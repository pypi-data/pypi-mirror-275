from relari.core.types import HTTPMethod
from typing import Any, Dict, List, Optional
from relari.metrics import Metric
import json


class EvaluationsClient:
    def __init__(self, client):
        self._client = client

    def list(self, project_id: str):
        endpoint = f"projects/{project_id}/experiments/"
        response = self._client._request(endpoint, HTTPMethod.GET)
        if response.status_code != 200:
            raise Exception("Failed to list evaluations: " + response.text)
        return response.json()

    def get(self, experiment_id: str):
        endpoint = f"projects/experiments/{experiment_id}/"
        response = self._client._request(endpoint, HTTPMethod.GET)
        if response.status_code != 200:
            raise Exception("Failed to get evaluation: " + response.text)
        return response.json()

    def submit(
        self,
        project_id: str,
        name: Optional[str],
        pipeline: List[Metric],
        data: List[Dict[str, Any]],
        metadata: Optional[Dict[str, Any]] = dict(),
    ):
        endpoint = f"projects/{project_id}/experiments/"
        payload = {
            "name": name,
            "pipeline": [metric.value for metric in pipeline],
            "data": data,
            "metadata": metadata,
        }
        res = self._client._request(
            endpoint, HTTPMethod.POST, data=json.dumps(payload)
        )
        if res.status_code != 200:
            raise Exception("Failed to submit evaluation: " + res.text)
        return res.json()["id"]