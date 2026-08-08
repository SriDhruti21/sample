"""
CartGuard AI
Real-Time Action Engine

Purpose:
Select ONE bounded intervention based on:
1. Abandonment risk
2. Detected shopping scenario

DO_NOTHING is always a valid action.
"""

from pathlib import Path
import json


# ============================================================
# Configuration
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

ACTIONS = [
    "DO_NOTHING",
    "SHOW_REMINDER",
    "SHOW_CHECKOUT_HELP",
    "SHOW_PAYMENT_RETRY",
    "SHOW_DELIVERY_INFO",
    "SHOW_SHIPPING_INFO",
    "SHOW_COD_OPTION",
    "SHOW_PRODUCT_RECOMMENDATION",
    "OFFER_SMALL_INCENTIVE",
]


# ============================================================
# Action Decision
# ============================================================

def recommend_action(risk_level, abandonment_probability, scenario):
    """
    Select exactly one action.

    Parameters:
        risk_level: LOW / MEDIUM / HIGH
        abandonment_probability: float between 0 and 1
        scenario: detected scenario string

    Returns:
        action, reason
    """

    risk_level = str(risk_level).upper()
    scenario = str(scenario).upper()

    # --------------------------------------------------------
    # LOW RISK
    # --------------------------------------------------------

    if risk_level == "LOW":

        return (
            "DO_NOTHING",
            "Abandonment risk is low. No intervention is necessary."
        )

    # --------------------------------------------------------
    # MEDIUM RISK
    # --------------------------------------------------------

    if risk_level == "MEDIUM":

        if scenario == "PAYMENT_FAILURE":
            return (
                "SHOW_PAYMENT_RETRY",
                "Payment failure detected with moderate abandonment risk."
            )

        if scenario == "SHIPPING_COST_SHOCK":
            return (
                "SHOW_SHIPPING_INFO",
                "Shipping cost concern detected with moderate abandonment risk."
            )

        if scenario == "DELIVERY_DELAY":
            return (
                "SHOW_DELIVERY_INFO",
                "Delivery concern detected with moderate abandonment risk."
            )

        if scenario == "COD_UNAVAILABLE":
            return (
                "SHOW_COD_OPTION",
                "COD availability may be affecting checkout completion."
            )

        if scenario == "CHECKOUT_FRICTION":
            return (
                "SHOW_CHECKOUT_HELP",
                "Repeated checkout/form activity suggests friction."
            )

        if scenario == "PRICE_COMPARISON":
            return (
                "SHOW_PRODUCT_RECOMMENDATION",
                "Price comparison behavior detected."
            )

        return (
            "SHOW_REMINDER",
            "Moderate abandonment risk detected without a specific high-priority issue."
        )

    # --------------------------------------------------------
    # HIGH RISK
    # --------------------------------------------------------

    if risk_level == "HIGH":

        if scenario == "PAYMENT_FAILURE":
            return (
                "SHOW_PAYMENT_RETRY",
                "High abandonment risk with a failed payment attempt."
            )

        if scenario == "SHIPPING_COST_SHOCK":
            return (
                "SHOW_SHIPPING_INFO",
                "High abandonment risk with shipping-cost interaction."
            )

        if scenario == "DELIVERY_DELAY":
            return (
                "SHOW_DELIVERY_INFO",
                "High abandonment risk with delivery-date concern."
            )

        if scenario == "COD_UNAVAILABLE":
            return (
                "SHOW_COD_OPTION",
                "High abandonment risk with COD availability concern."
            )

        if scenario == "CHECKOUT_FRICTION":
            return (
                "SHOW_CHECKOUT_HELP",
                "High abandonment risk with checkout friction."
            )

        if scenario == "PRICE_COMPARISON":
            return (
                "SHOW_PRODUCT_RECOMMENDATION",
                "High abandonment risk with price-comparison behavior."
            )

        if scenario == "CART_VALUE_CHANGE":
            return (
                "SHOW_REMINDER",
                "High abandonment risk after cart-value changes."
            )

        # No specific scenario
        return (
            "OFFER_SMALL_INCENTIVE",
            "High abandonment risk detected without a more specific intervention reason."
        )

    # --------------------------------------------------------
    # Safety fallback
    # --------------------------------------------------------

    return (
        "DO_NOTHING",
        "Unknown risk level. No intervention selected."
    )


# ============================================================
# Display Helper
# ============================================================

def display_decision(
    purchase_probability,
    abandonment_probability,
    risk_level,
    scenario,
    scenario_reason,
    action,
    action_reason
):

    print("\n")
    print("=" * 70)
    print(" CARTGUARD AI - ACTION DECISION ")
    print("=" * 70)

    print("\n## RISK ASSESSMENT")
    print("-" * 40)

    print(
        f"Purchase Probability     : "
        f"{purchase_probability:.4f}"
    )

    print(
        f"Abandonment Probability  : "
        f"{abandonment_probability:.4f}"
    )

    print(f"Risk Level               : {risk_level}")

    print("\n## SCENARIO")
    print("-" * 40)

    print(f"Scenario                 : {scenario}")
    print(f"Reason                   : {scenario_reason}")

    print("\n## RECOMMENDED ACTION")
    print("-" * 40)

    print(f"Action                   : {action}")
    print(f"Reason                   : {action_reason}")

    print("\n## AVAILABLE ACTIONS")
    print("-" * 40)

    for available_action in ACTIONS:
        print(f"- {available_action}")

    print("\n" + "=" * 70)


# ============================================================
# Standalone Test
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print(" CARTGUARD AI - REAL-TIME ACTION ENGINE TEST ")
    print("=" * 70)

    # Test scenario
    purchase_probability = 0.20
    abandonment_probability = 0.80

    risk_level = "HIGH"

    scenario = "PAYMENT_FAILURE"

    scenario_reason = (
        "Payment was attempted but failed."
    )

    action, action_reason = recommend_action(
        risk_level=risk_level,
        abandonment_probability=abandonment_probability,
        scenario=scenario
    )

    display_decision(
        purchase_probability=purchase_probability,
        abandonment_probability=abandonment_probability,
        risk_level=risk_level,
        scenario=scenario,
        scenario_reason=scenario_reason,
        action=action,
        action_reason=action_reason
    )