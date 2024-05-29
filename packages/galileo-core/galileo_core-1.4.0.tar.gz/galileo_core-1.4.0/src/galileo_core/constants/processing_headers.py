from enum import Enum


class ProcessingHeaders(str, Enum):
    received_at = "Galileo-Request-Received-At"
    execution_time = "Galileo-Request-Execution-Time"
    response_at = "Galileo-Request-Response-At"
