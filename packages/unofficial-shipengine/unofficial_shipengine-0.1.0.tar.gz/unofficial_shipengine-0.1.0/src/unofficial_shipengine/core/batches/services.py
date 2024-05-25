import json
from typing import Union, Optional, Any

from attrs import asdict

from unofficial_shipengine.utils.serialize import serializer
from .models import Batch, BatchRequest, ProcessLabels
from ..common.services import BaseService
from ..shipments.models import Shipment


class BatchService(BaseService):
    """
    BatchService provides methods for interacting with batch-related endpoints in the ShipEngine API.

    Methods:
        create_batch(batch_request: BatchRequest) -> Batch:
            Creates a new batch based on the given batch request.

        get_by_id(batch_id: str) -> Batch:
            Retrieves a batch by its ID.

        process_labels(batch: Union[Batch, str], process_labels: ProcessLabels) -> None:
            Processes labels for the given batch.

        get_batch_errors(batch: Union[Batch, str], page: int = 1, pagesize: int = 1) -> dict[str, Any]:
            Retrieves errors for the given batch.

        delete_batch(batch: Union[Batch, str]) -> None:
            Deletes the given batch.

        add_to_batch(batch: Union[Batch, str], shipments: list[Union[Shipment, str]], rates: Optional[list[str]] = None) -> None:
            Adds shipments to the given batch.

        remove_from_batch(batch: Union[Batch, str], shipments: list[Union[Shipment, str]], rates: Optional[list[str]] = None) -> None:
            Removes shipments from the given batch.
    """

    def create_batch(self, batch_request: BatchRequest) -> Batch:
        """
        Creates a new batch based on the given batch request.

        Args:
            batch_request (BatchRequest): The request data for creating a batch.

        Returns:
            Batch: The created batch object.

        Raises:
            ShipEngineAPIError: If the response from the API is invalid.
        """
        data: str = json.dumps(asdict(batch_request, value_serializer=serializer))

        response = self.session.post("https://api.shipengine.com/v1/batches", data=data)
        response_dict = json.loads(response.text)
        self._handle_response(response)

        return Batch.from_dict(response_dict)

    def get_by_id(self, batch_id: str) -> Batch:
        """
        Retrieves a batch by its ID.

        Args:
            batch_id (str): The ID of the batch to retrieve.

        Returns:
            Batch: The retrieved batch object.

        Raises:
            ShipEngineAPIError: If the response from the API is invalid.
        """
        url: str = f"https://api.shipengine.com/v1/batches/{batch_id}"

        response = self.session.get(url)
        response_dict = json.loads(response.text)
        self._handle_response(response)

        return Batch.from_dict(response_dict)

    def process_labels(
        self, batch: Union[Batch, str], process_labels: ProcessLabels
    ) -> None:
        """Function can take a Batch object or a batch_id."""
        if isinstance(batch, Batch):
            batch = batch.batch_id

        data: str = json.dumps(asdict(process_labels, value_serializer=serializer))
        url: str = f"https://api.shipengine.com/v1/batches/{batch}/process/labels"
        response = self.session.post(url, data=data)
        self._handle_response(response)

    def get_batch_errors(
        self, batch: Union[Batch, str], page: int = 1, pagesize: int = 1
    ) -> dict[str, Any]:
        """
        Retrieves errors for the given batch.

        Args:
            batch (Union[Batch, str]): The batch object or batch ID.
            page (int, optional): The page number to retrieve. Defaults to 1.
            pagesize (int, optional): The number of errors per page. Defaults to 1.

        Returns:
            dict[str, Any]: The errors for the batch.

        Raises:
            ShipEngineAPIError: If the response from the API is invalid.
        """
        if isinstance(batch, Batch):
            batch = batch.batch_id

        url: str = f"https://api.shipengine.com/v1/batches/{batch}/errors"
        response = self.session.get(
            url, params=json.dumps({"page": page, "pagesize": pagesize})
        )

        response_json: dict[str, Any] = response.json()

        return response_json

    def delete_batch(self, batch: Union[Batch, str]) -> None:
        """
        Deletes the given batch.

        Args:
            batch (Union[Batch, str]): The batch object or batch ID.

        Raises:
            ShipEngineAPIError: If the response from the API is invalid.
        """
        if isinstance(batch, Batch):
            batch = batch.batch_id

        url: str = f"https://api.shipengine.com/v1/batches/{batch}"
        response = self.session.delete(url)
        self._handle_response(response)

    def add_to_batch(
        self,
        batch: Union[Batch, str],
        shipments: list[Union[Shipment, str]],
        rates: Optional[list[str]] = None,
    ) -> None:
        """
        Adds shipments to the given batch.

        Args:
            batch (Union[Batch, str]): The batch object or batch ID.
            shipments (list[Union[Shipment, str]]): A list of shipment objects or shipment IDs.
            rates (Optional[list[str]], optional): A list of rate IDs. Defaults to None.

        Raises:
            ShipEngineAPIError: If the response from the API is invalid.
        """
        self._modify_batch(batch, "add", shipments, rates)

    def remove_from_batch(
        self,
        batch: Union[Batch, str],
        shipments: list[Union[Shipment, str]],
        rates: Optional[list[str]] = None,
    ) -> None:
        """
        Removes shipments from the given batch.

        Args:
            batch (Union[Batch, str]): The batch object or batch ID.
            shipments (list[Union[Shipment, str]]): A list of shipment objects or shipment IDs.
            rates (Optional[list[str]], optional): A list of rate IDs. Defaults to None.

        Raises:
            ShipEngineAPIError: If the response from the API is invalid.
        """
        self._modify_batch(batch, "remove", shipments, rates)

    def _modify_batch(
        self,
        batch: Union[Batch, str],
        endpoint: str,
        shipments: list[Union[str, Shipment]],
        rates: Optional[list[str]] = None,
    ) -> None:
        if isinstance(batch, Batch):
            batch = batch.batch_id

        shipments = [s if isinstance(s, str) else s.shipment_id for s in shipments]

        url: str = f"https://api.shipengine.com/v1/batches/{batch}/{endpoint}"
        data: str = json.dumps({"shipment_ids": shipments, "rate_ids": rates})
        response = self.session.post(url, data=data)
        self._handle_response(response)
