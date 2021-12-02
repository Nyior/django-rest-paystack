from rest_framework import status

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .base_api_service import BaseAPIService
from paystack.models import BasePaymentHistory


class TransactionService(BaseAPIService):

    def __init__(self, request) -> None:
        self.request = request
        self.user = request.user

    def _create_transaction_object(self, transaction_data):
        user = transaction_data["metadata"]["user"]

        BasePaymentHistory.objects.create(
            user=user,
            charge_type="GATEWAY PURCHASE",
            amount=transaction_data["amount"],
            currency=transaction_data["currency"],
            txRef=transaction_data["reference"],
            payment_date_time=transaction_data["paid_at"],
            status=transaction_data["status"],
        )

    def log_transaction(self, transaction_data): # transaction will be logged in the webhook
        self._create_transaction_object(transaction_data)

    def _validate_payload(self, payload: dict) -> None:
        """ check that payload has all the required params """
        required = ["email", "amount"]

        for i in required:
            if not payload[i]:
                raise ValidationError(f"{i} must be provided")

    def initialize_payment(self, payload: dict) -> Response:
        path = "/initialize"

        self._validate_payload(payload)
        return self.make_request("POST", path, payload)

    def verify_payment(self, transaction_ref: str) -> Response:
        path = "/verify/{0}".format(transaction_ref)
        
        response = self.make_request("GET", path)
       
        if response.data["status"] == "success" and response.status_code == 200:
            return response
        else:
            raise ValidationError("payment for this transaction could not be processed")

    def transactions(self, **kwargs):
        status = kwargs.get('status')
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')

        path = "/transaction/?perPage={}".format(kwargs.get('pagination'))
        path = path + "&status={}".format(status) if status else path
        path = path + "&from={}".format(start_date) if start_date else path
        path = path + "&to={}".format(end_date) if end_date else path

        return self.make_request("GET", path)

    def transaction(self, transaction_id):
        path = "transaction/{}/".format(transaction_id)
        return self.make_request("GET", path)