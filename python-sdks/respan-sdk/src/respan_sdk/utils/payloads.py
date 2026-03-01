from typing import Any, Dict, Mapping, Optional


def with_api_key_for_signing(
    payload: Optional[Mapping[str, Any]],
    api_key: Optional[str],
) -> Dict[str, Any]:
    """
    Return a copy of payload with api_key attached for webhook signing.

    This avoids mutating the source payload that may later be reused for
    storage or other downstream processing.
    """
    copied_payload: Dict[str, Any] = dict(payload or {})
    if api_key:
        copied_payload["api_key"] = api_key
    return copied_payload
