import json
from relari.core.types import HTTPMethod

class ProjectsClient:
    def __init__(self, client):
        self._client = client

    def list(self):
        response = self._client._request("projects", HTTPMethod.GET)
        return response.json()

    def create(self, name: str):
        payload = {"name": name}
        response = self._client._request(
            "projects", HTTPMethod.POST, data=json.dumps(payload)
        )
        return response.json()

    def find(self, name: str):
        projects = self.list()
        name = name.strip()
        for project in projects:
            if project["name"].strip() == name:
                return project
        return None