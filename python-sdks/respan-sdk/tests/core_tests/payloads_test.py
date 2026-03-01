from respan_sdk.utils.payloads import with_api_key_for_signing


def test_with_api_key_for_signing_adds_api_key_without_mutating_source():
    source = {"unique_id": "log_123", "trace_unique_id": "trace_123"}

    result = with_api_key_for_signing(source, "sk_test_abc")

    assert result is not source
    assert result["api_key"] == "sk_test_abc"
    assert "api_key" not in source
    assert source["unique_id"] == "log_123"


def test_with_api_key_for_signing_no_api_key_keeps_source_unmodified():
    source = {"unique_id": "log_123"}

    result = with_api_key_for_signing(source, "")

    assert result is not source
    assert result == {"unique_id": "log_123"}
    assert "api_key" not in source
