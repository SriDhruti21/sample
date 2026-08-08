"""
CartGuard AI
Real-Time Scenario Detector

Purpose:
Identify the likely reason behind a customer's
abandonment risk using real-time session signals.

This module does NOT predict abandonment.
The XGBoost model handles risk prediction.

This module identifies the scenario so the
Action Engine can choose an appropriate action.
"""

from typing import Dict, Any


# ============================================================
# Scenario Names
# ============================================================

PAYMENT_FAILURE = "PAYMENT_FAILURE"
DELIVERY_CONCERN = "DELIVERY_CONCERN"
PRICE_CHECKING = "PRICE_CHECKING"
NO_COD = "NO_COD"
CHECKOUT_FRICTION = "CHECKOUT_FRICTION"
CART_HESITATION = "CART_HESITATION"
NO_CLEAR_ISSUE = "NO_CLEAR_ISSUE"


# ============================================================
# Scenario Detection
# ============================================================

def detect_scenario(session: Dict[str, Any]) -> Dict[str, Any]:
    """
    Detect the most likely abandonment scenario.

    Parameters
    ----------
    session : dict
        Real-time session signals.

    Returns
    -------
    dict
        Scenario, reason and priority.
    """

    # --------------------------------------------------------
    # Read signals safely
    # --------------------------------------------------------

    payment_attempt = bool(
        session.get("payment_attempt", False)
    )

    payment_failed = bool(
        session.get("payment_failed", False)
    )

    delivery_viewed = bool(
        session.get("delivery_viewed", False)
    )

    delivery_date_changed = bool(
        session.get("delivery_date_changed", False)
    )

    shipping_cost_viewed = bool(
        session.get("shipping_cost_viewed", False)
    )

    price_comparison = bool(
        session.get("price_comparison", False)
    )

    cod_available = session.get(
        "cod_available",
        True
    )

    cod_requested = bool(
        session.get("cod_requested", False)
    )

    checkout_started = bool(
        session.get("checkout_started", False)
    )

    form_repeated = bool(
        session.get("form_repeated", False)
    )

    cart_changed = bool(
        session.get("cart_changed", False)
    )

    has_cart = bool(
        session.get("has_cart", False)
    )

    # --------------------------------------------------------
    # 1. Payment Failure
    # --------------------------------------------------------

    if payment_attempt and payment_failed:

        return {
            "scenario": PAYMENT_FAILURE,
            "reason": (
                "Payment was attempted but failed."
            ),
            "priority": 1
        }

    # --------------------------------------------------------
    # 2. No COD
    # --------------------------------------------------------

    if (
        has_cart
        and cod_requested
        and not cod_available
    ):

        return {
            "scenario": NO_COD,
            "reason": (
                "Cash on Delivery is unavailable "
                "for the customer's cart."
            ),
            "priority": 2
        }

    # --------------------------------------------------------
    # 3. Delivery Concern
    # --------------------------------------------------------

    if (
        has_cart
        and (
            delivery_viewed
            or delivery_date_changed
            or shipping_cost_viewed
        )
    ):

        return {
            "scenario": DELIVERY_CONCERN,
            "reason": (
                "The customer appears to be checking "
                "delivery or shipping information."
            ),
            "priority": 3
        }

    # --------------------------------------------------------
    # 4. Price Checking
    # --------------------------------------------------------

    if (
        has_cart
        and price_comparison
    ):

        return {
            "scenario": PRICE_CHECKING,
            "reason": (
                "The customer appears to be comparing "
                "product prices."
            ),
            "priority": 4
        }

    # --------------------------------------------------------
    # 5. Checkout Friction
    # --------------------------------------------------------

    if (
        checkout_started
        and form_repeated
    ):

        return {
            "scenario": CHECKOUT_FRICTION,
            "reason": (
                "The customer appears to be experiencing "
                "checkout form friction."
            ),
            "priority": 5
        }

    # --------------------------------------------------------
    # 6. Cart Hesitation
    # --------------------------------------------------------

    if (
        has_cart
        and cart_changed
    ):

        return {
            "scenario": CART_HESITATION,
            "reason": (
                "The customer has an active cart and "
                "recently changed cart contents."
            ),
            "priority": 6
        }

    # --------------------------------------------------------
    # 7. No Clear Issue
    # --------------------------------------------------------

    return {
        "scenario": NO_CLEAR_ISSUE,
        "reason": (
            "No specific abandonment reason was detected."
        ),
        "priority": 99
    }


# ============================================================
# Standalone Test
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print(" CARTGUARD AI - SCENARIO DETECTOR ")
    print("=" * 70)

    # --------------------------------------------------------
    # Test Session
    # --------------------------------------------------------

    test_session = {

        "has_cart": True,

        "payment_attempt": True,

        "payment_failed": True,

        "delivery_viewed": False,

        "delivery_date_changed": False,

        "shipping_cost_viewed": False,

        "price_comparison": False,

        "cod_available": True,

        "cod_requested": False,

        "checkout_started": True,

        "form_repeated": False,

        "cart_changed": False
    }

    # --------------------------------------------------------
    # Detect Scenario
    # --------------------------------------------------------

    result = detect_scenario(test_session)

    print("\n## SESSION SIGNALS")

    for key, value in test_session.items():

        print(
            f"{key:25} : {value}"
        )

    print("\n## DETECTED SCENARIO")

    print(
        f"\nScenario : "
        f"{result['scenario']}"
    )

    print(
        f"Reason   : "
        f"{result['reason']}"
    )

    print(
        f"Priority : "
        f"{result['priority']}"
    )

    print("\nScenario Detector Test Completed.")