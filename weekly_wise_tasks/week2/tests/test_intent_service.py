import sys
from pathlib import Path

BACKEND = Path(__file__).resolve().parents[1] / "backend"
sys.path.insert(0, str(BACKEND))

from app.services.intent_service import detect_intent


def test_payment_intent():
    result = detect_intent("My payment failed and money was deducted")
    assert result.intent == "payment_issue"
    assert result.requires_action is True
    assert result.priority == "high"


def test_order_tracking_intent():
    result = detect_intent("Where is my order delivery?")
    assert result.intent == "order_tracking"


def test_general_intent():
    result = detect_intent("Tell me what this application does")
    assert result.intent == "general_query"
