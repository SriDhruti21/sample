"""
CartGuard AI
Real-Time Risk Scorer

Loads the trained XGBoost model and calculates
purchase probability, abandonment probability,
and risk level for a session.
"""

from pathlib import Path
import json
import numpy as np
import xgboost as xgb


# ============================================================
# Paths
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "saved_models" / "xgboost.pkl"

FEATURE_LIST_PATH = (
    BASE_DIR
    / "saved_models"
    / "xgboost_feature_list.json"
)

THRESHOLD_PATH = (
    BASE_DIR
    / "saved_models"
    / "xgboost_threshold.json"
)


# ============================================================
# Load Model
# ============================================================

print("\n" + "=" * 70)
print(" CARTGUARD AI - REAL-TIME RISK SCORER ")
print("=" * 70)

print("\nLoading XGBoost model...")

model = xgb.XGBClassifier()

model.load_model(MODEL_PATH)

print("XGBoost Model Loaded Successfully.")


# ============================================================
# Load Feature List
# ============================================================

print("\nLoading feature list...")

with open(FEATURE_LIST_PATH, "r") as file:
    feature_data = json.load(file)


# Support both possible JSON formats
if isinstance(feature_data, dict):
    FEATURES = feature_data.get(
        "features",
        feature_data.get("feature_list", [])
    )
else:
    FEATURES = feature_data


print(f"Features Loaded : {len(FEATURES)}")


# ============================================================
# Load Threshold
# ============================================================

print("\nLoading classification threshold...")

with open(THRESHOLD_PATH, "r") as file:
    threshold_data = json.load(file)


if isinstance(threshold_data, dict):
    THRESHOLD = float(
        threshold_data.get(
            "threshold",
            threshold_data.get(
                "classification_threshold",
                0.5
            )
        )
    )
else:
    THRESHOLD = float(threshold_data)


print(f"Classification Threshold : {THRESHOLD}")


# ============================================================
# Display Model Information
# ============================================================

print("\n" + "=" * 70)
print("MODEL INFORMATION")
print("=" * 70)

print(f"Model       : XGBoost")
print(f"Features    : {len(FEATURES)}")
print(f"Threshold   : {THRESHOLD}")


# ============================================================
# Risk Scoring Function
# ============================================================

def score_session(feature_values):
    """
    Score one active customer session.

    Parameters
    ----------
    feature_values : list / numpy array / dictionary

    Returns
    -------
    dict
    """

    # --------------------------------------------------------
    # Convert dictionary to feature order
    # --------------------------------------------------------

    if isinstance(feature_values, dict):

        missing_features = [
            feature
            for feature in FEATURES
            if feature not in feature_values
        ]

        if missing_features:
            raise ValueError(
                f"Missing Features: {missing_features}"
            )

        values = [
            feature_values[feature]
            for feature in FEATURES
        ]

    else:

        values = list(feature_values)

    # --------------------------------------------------------
    # Validate feature count
    # --------------------------------------------------------

    if len(values) != len(FEATURES):

        raise ValueError(
            f"Expected {len(FEATURES)} features, "
            f"received {len(values)}"
        )

    # --------------------------------------------------------
    # Convert to numeric array
    # --------------------------------------------------------

    X = np.array(
        values,
        dtype=float
    ).reshape(1, -1)

    # --------------------------------------------------------
    # Prediction probability
    # --------------------------------------------------------

    purchase_probability = float(
        model.predict_proba(X)[0][1]
    )

    abandonment_probability = (
        1.0 - purchase_probability
    )

    # --------------------------------------------------------
    # Classification
    # --------------------------------------------------------

    prediction = int(
        purchase_probability >= THRESHOLD
    )

    # --------------------------------------------------------
    # Risk Level
    # --------------------------------------------------------

    if abandonment_probability >= 0.70:

        risk_level = "HIGH"

    elif abandonment_probability >= 0.40:

        risk_level = "MEDIUM"

    else:

        risk_level = "LOW"

    # --------------------------------------------------------
    # Result
    # --------------------------------------------------------

    result = {

        "purchase_probability":
            round(purchase_probability, 4),

        "abandonment_probability":
            round(abandonment_probability, 4),

        "risk_level":
            risk_level,

        "prediction":
            prediction,

        "threshold":
            THRESHOLD
    }

    return result


# ============================================================
# Standalone Test
# ============================================================

if __name__ == "__main__":

    test_features = [
        0.0,
        3,
        2,
        1,
        2,
        145000.0,
        48333.3333,
        45000.0,
        50000.0,
        5000.0,
        2357.0226,
        2,
        1,
        1,
        0.3333,
        0.6666,
        0.5,
        0.0,
        2.0,
        1.0,
        0.3333,
        0.6666
    ]

    result = score_session(test_features)

    print("\n" + "=" * 70)
    print("RISK RESULT")
    print("=" * 70)

    print(
        f"\nPurchase Probability    : "
        f"{result['purchase_probability']:.4f}"
    )

    print(
        f"Abandonment Probability : "
        f"{result['abandonment_probability']:.4f}"
    )

    print(
        f"Risk Level              : "
        f"{result['risk_level']}"
    )

    print(
        f"Model Prediction        : "
        f"{result['prediction']}"
    )

    print(
        f"Classification Threshold: "
        f"{result['threshold']:.4f}"
    )