"""
CartGuard AI
Real-Time Feature Generator
"""

import math
from datetime import datetime


# ============================================================
# FEATURE ORDER
# Must exactly match XGBoost training
# ============================================================

FEATURE_ORDER = [
    "session_duration",
    "total_events",
    "unique_products",
    "unique_categories",
    "unique_brands",
    "total_price",
    "average_price",
    "minimum_price",
    "maximum_price",
    "price_range",
    "price_std",
    "view_count",
    "cart_count",
    "has_cart",
    "cart_to_event_ratio",
    "views_to_event_ratio",
    "cart_to_view_ratio",
    "events_per_second",
    "products_per_category",
    "products_per_brand",
    "category_per_event_ratio",
    "brand_per_event_ratio"
]


# ============================================================
# Generate Features
# ============================================================

def generate_features(session_events):

    if not session_events:
        raise ValueError("Session contains no events.")

    prices = []

    products = set()
    categories = set()
    brands = set()

    timestamps = []

    view_count = 0
    cart_count = 0

    # --------------------------------------------------------
    # Process Events
    # --------------------------------------------------------

    for event in session_events:

        event_type = event.get("event_type")

        if event_type == "view":
            view_count += 1

        elif event_type == "cart":
            cart_count += 1

        # Product
        product_id = event.get("product_id")

        if product_id is not None:
            products.add(product_id)

        # Category
        category_id = event.get("category_id")

        if category_id is not None:
            categories.add(category_id)

        # Brand
        brand = event.get("brand")

        if brand:
            brands.add(brand)

        # Price
        price = event.get("price")

        if price is not None:

            try:

                price = float(price)

                if math.isfinite(price) and price >= 0:
                    prices.append(price)

            except (ValueError, TypeError):
                pass

        # Timestamp
        event_time = event.get("event_time")

        if event_time:

            try:

                if isinstance(event_time, datetime):

                    timestamps.append(event_time)

                else:

                    timestamp = str(event_time)

                    timestamp = timestamp.replace("Z", "+00:00")

                    timestamps.append(
                        datetime.fromisoformat(timestamp)
                    )

            except Exception:
                pass

    # --------------------------------------------------------
    # Basic Features
    # --------------------------------------------------------

    total_events = len(session_events)

    unique_products = len(products)

    unique_categories = len(categories)

    unique_brands = len(brands)

    # --------------------------------------------------------
    # Price Features
    # --------------------------------------------------------

    if prices:

        total_price = sum(prices)

        average_price = (
            total_price / len(prices)
        )

        minimum_price = min(prices)

        maximum_price = max(prices)

        price_range = (
            maximum_price - minimum_price
        )

        if len(prices) > 1:

            mean = average_price

            variance = sum(
                (p - mean) ** 2
                for p in prices
            ) / len(prices)

            price_std = math.sqrt(variance)

        else:

            price_std = 0.0

    else:

        total_price = 0.0
        average_price = 0.0
        minimum_price = 0.0
        maximum_price = 0.0
        price_range = 0.0
        price_std = 0.0

    # --------------------------------------------------------
    # Session Duration
    # --------------------------------------------------------

    if len(timestamps) >= 2:

        timestamps.sort()

        session_duration = (
            timestamps[-1] - timestamps[0]
        ).total_seconds()

        session_duration = max(
            session_duration,
            0.0
        )

    else:

        session_duration = 0.0

    # --------------------------------------------------------
    # Ratios
    # --------------------------------------------------------

    cart_to_event_ratio = (
        cart_count / total_events
        if total_events > 0
        else 0.0
    )

    views_to_event_ratio = (
        view_count / total_events
        if total_events > 0
        else 0.0
    )

    cart_to_view_ratio = (
        cart_count / view_count
        if view_count > 0
        else 0.0
    )

    events_per_second = (
        total_events / session_duration
        if session_duration > 0
        else 0.0
    )

    products_per_category = (
        unique_products / unique_categories
        if unique_categories > 0
        else 0.0
    )

    products_per_brand = (
        unique_products / unique_brands
        if unique_brands > 0
        else 0.0
    )

    category_per_event_ratio = (
        unique_categories / total_events
        if total_events > 0
        else 0.0
    )

    brand_per_event_ratio = (
        unique_brands / total_events
        if total_events > 0
        else 0.0
    )

    has_cart = (
        1 if cart_count > 0 else 0
    )

    # ========================================================
    # EXACT 22 FEATURES
    # ========================================================

    features = {

        "session_duration": session_duration,

        "total_events": total_events,

        "unique_products": unique_products,

        "unique_categories": unique_categories,

        "unique_brands": unique_brands,

        "total_price": total_price,

        "average_price": average_price,

        "minimum_price": minimum_price,

        "maximum_price": maximum_price,

        "price_range": price_range,

        "price_std": price_std,

        "view_count": view_count,

        "cart_count": cart_count,

        "has_cart": has_cart,

        "cart_to_event_ratio": cart_to_event_ratio,

        "views_to_event_ratio": views_to_event_ratio,

        "cart_to_view_ratio": cart_to_view_ratio,

        "events_per_second": events_per_second,

        "products_per_category": products_per_category,

        "products_per_brand": products_per_brand,

        "category_per_event_ratio": category_per_event_ratio,

        "brand_per_event_ratio": brand_per_event_ratio
    }

    return features


# ============================================================
# Convert Dictionary → Model Vector
# ============================================================

def features_to_vector(features):

    return [
        features[name]
        for name in FEATURE_ORDER
    ]


# ============================================================
# Test
# ============================================================

if __name__ == "__main__":

    print("=" * 70)
    print(" CARTGUARD AI - REAL-TIME FEATURE GENERATOR ")
    print("=" * 70)

    sample_events = [

        {
            "event_type": "view",
            "product_id": 101,
            "category_id": 10,
            "category_code": "electronics",
            "brand": "brand_a",
            "price": 45000
        },

        {
            "event_type": "view",
            "product_id": 102,
            "category_id": 10,
            "category_code": "electronics",
            "brand": "brand_b",
            "price": 50000
        },

        {
            "event_type": "cart",
            "product_id": 102,
            "category_id": 10,
            "category_code": "electronics",
            "brand": "brand_b",
            "price": 50000
        }

    ]

    features = generate_features(sample_events)

    print("\n## Generated Features")

    for name, value in features.items():

        print(
            f"{name:<30}: {value}"
        )

    model_input = features_to_vector(features)

    print("\n## Model Input")

    print(model_input)

    print(
        f"\nModel Input Length : "
        f"{len(model_input)}"
    )

    print("\nFeature Generator Test Completed.")