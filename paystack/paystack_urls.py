PAYSTACK_BASE_URL = "https://api.paystack.co"

TRANSACTION_URL = PAYSTACK_BASE_URL + "/transaction"
PAYSTACK_INITIALIZE_TRANSACTION_URL = TRANSACTION_URL + "/initialize"
PAYSTACK_VERIFY_TRANSACTION_URL = TRANSACTION_URL + "/verify/{0}"  # insert tran. ref.

PAYSTACK_CHARGE_AUTHORIZATION_URL = TRANSACTION_URL + "/charge_authorization"
