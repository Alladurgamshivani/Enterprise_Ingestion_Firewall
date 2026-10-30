"""Small demonstration intent detector.

Replace detect_intent() with your existing intent-detection workflow when
integrating this sample into your current workspace.
"""
from app.schemas.chat import IntentAnalysis


def detect_intent(message: str) -> IntentAnalysis:
    text = message.lower()

    if any(word in text for word in ("payment", "paid", "transaction", "refund", "deducted")):
        intent = "payment_issue"
        summary = "The user is asking about a payment, transaction, or refund."
        requires_action = True
        priority = "high" if any(word in text for word in ("deducted", "charged twice", "fraud")) else "normal"
    elif any(word in text for word in ("order", "delivery", "shipment", "tracking")):
        intent = "order_tracking"
        summary = "The user is asking about an order or delivery."
        requires_action = True
        priority = "normal"
    elif any(word in text for word in ("error", "failed", "not working", "crash", "exception")):
        intent = "technical_issue"
        summary = "The user is reporting a technical problem."
        requires_action = True
        priority = "normal"
    else:
        intent = "general_query"
        summary = "The user has asked a general question."
        requires_action = False
        priority = "normal"

    return IntentAnalysis(
        intent=intent,
        summary=summary,
        requires_action=requires_action,
        priority=priority,
    )
