from prometheus_client import Counter

REQIEST_CNT = Counter("request", "Sent request count")
SUCCESS_RESPONSE_CNT = Counter("success_response", "Recieved response with valid data")
ERROR_RESPONSE_CNT = Counter("error response", "Recieved response with invalid data")