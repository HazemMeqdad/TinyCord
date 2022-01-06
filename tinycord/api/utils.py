def reason(reason: str) -> str:
    """
        encode a reason.
    """
    if reason is None:
        return {}
    return {'X-Audit-Log-Reason': reason.encode('utf-8')}