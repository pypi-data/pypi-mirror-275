from .api_client import APIClient


class APIResource:
    def __init__(self, base_endpoint: str, api_client: APIClient):
        self.base_endpoint = base_endpoint
        self.api_client = api_client

    def find(self, resource_id, base_endpoint=None, headers=None):
        if base_endpoint is None:
            endpoint = f"{self.base_endpoint}/{resource_id}"
        else:
            endpoint = f"{base_endpoint}/{resource_id}"

        response = self.api_client.get(endpoint=endpoint, headers=headers)

        return response

    def list(self, params, headers=None):
        endpoint = self.base_endpoint
        response = self.api_client.get(endpoint, params=params, headers=headers)

        return response

    def create(self, payload, headers=None, expected_successful_status_code=201):
        endpoint = self.base_endpoint
        response = self.api_client.post(
            endpoint, payload, headers, expected_successful_status_code
        )

        return response

    def update(
        self,
        resource_id,
        payload,
        base_endpoint=None,
        headers=None,
        expected_successful_status_code=200,
    ):
        if base_endpoint is None:
            endpoint = f"{self.base_endpoint}/{resource_id}"
        else:
            endpoint = f"{base_endpoint}/{resource_id}"

        response = self.api_client.patch(
            endpoint, payload, headers, expected_successful_status_code
        )

        return response

    def full_update(
        self,
        resource_id,
        payload,
        base_endpoint=None,
        headers=None,
        expected_successful_status_code=200,
    ):
        if base_endpoint is None:
            endpoint = f"{self.base_endpoint}/{resource_id}"
        else:
            if resource_id is None and base_endpoint is not None:
                endpoint = base_endpoint
            else:
                endpoint = f"{base_endpoint}/{resource_id}"

        response = self.api_client.put(
            endpoint, payload, headers, expected_successful_status_code
        )

        return response

    def delete(self, resource_id, base_endpoint=None, headers=None):

        if base_endpoint is None:
            endpoint = f"{self.base_endpoint}/{resource_id}"
        else:
            endpoint = f"{base_endpoint}/{resource_id}"

        self.api_client.delete(endpoint, headers)
