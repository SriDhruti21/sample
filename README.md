<div align="center">

# 🛒 Cart Rescue
### AI-Powered Cart Abandonment Prediction & Recovery System

An intelligent e-commerce platform that predicts cart abandonment in real time, explains why a customer is likely to leave, and recommends the best recovery action using Machine Learning and AI.

Built for **AI Build 2026 – Track 2: Cart Rescue**

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![React](https://img.shields.io/badge/React-Frontend-61DAFB)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-Styling-38B2AC)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green)
![XGBoost](https://img.shields.io/badge/XGBoost-ML-orange)

</div>

---

# 📌 Overview

Cart Rescue is an AI-powered intelligent cart recovery system that continuously monitors customer browsing behavior, predicts the probability of cart abandonment, identifies the most likely reason for abandonment, and recommends the best recovery action.

Unlike traditional e-commerce systems that send discount coupons to every customer, Cart Rescue makes **smart, data-driven decisions** to maximize conversion while minimizing unnecessary discounts.

---

# 🎯 Problem Statement

Customers abandon shopping carts for various reasons such as:

- Payment failures
- High shipping charges
- Checkout friction
- Long decision-making time
- Price comparison
- Delivery concerns

Most existing systems treat every customer the same by offering discounts.

**Cart Rescue solves this by using Artificial Intelligence to predict abandonment risk and recommend personalized recovery actions.**

---

# ✨ Features

## Customer Portal

- Customer Login
- Browse Products
- Product Details
- Add to Cart
- Checkout
- Payment Processing

---

## AI Prediction Engine

- Real-Time Session Monitoring
- Feature Extraction
- XGBoost Prediction Model
- Abandonment Risk Score
- Explainable AI
- Intelligent Decision Agent
- Personalized Recovery Recommendation

---

## Admin Dashboard

- Live Customer Sessions
- High Risk Sessions
- Session Details
- Risk Explanation
- Recommended Actions
- Action History
- Analytics Dashboard

---

# 🏗 System Architecture

```
                CUSTOMER

Open Website
      │
      ▼
Browse Products
      │
      ▼
View Product
      │
      ▼
Add To Cart
      │
      ▼
Checkout
      │
      ▼
Payment Attempt
      │
      ▼
Payment Success / Failure
      │
      ▼
Backend Stores Events

──────────────────────────────────────

          AI ENGINE

Receive Session Events
      │
      ▼
Feature Extraction
      │
      ▼
XGBoost Prediction
      │
      ▼
Risk Score
      │
      ▼
Decision Agent
      │
      ▼
Recommended Action
      │
      ▼
Store Prediction

──────────────────────────────────────

        ADMIN DASHBOARD

Live Sessions
      │
      ▼
High Risk Sessions
      │
      ▼
Session Details
      │
      ▼
Risk Explanation
      │
      ▼
Recommended Action
      │
      ▼
Notification
```

---

# 🧠 AI Workflow

```
Customer Activity
        │
        ▼
Session Events
        │
        ▼
Feature Extraction
        │
        ▼
XGBoost Prediction Model
        │
        ▼
Abandonment Risk Score
        │
        ▼
Decision Agent
        │
        ▼
Recommended Recovery Action
        │
        ▼
Save Prediction
        │
        ▼
Dashboard Update
```

---

# 📊 Dashboard

The AI dashboard provides complete visibility into customer behavior.

### Dashboard Modules

- Dashboard
- Live Sessions
- Session Details
- High Risk Sessions
- Action History
- Analytics

---

## Session Details

Clicking on any session displays:

- Customer ID
- Products Viewed
- Cart Value
- Products Added
- Time on Site
- Pages Visited
- Payment Attempts
- Payment Failed
- AI Risk Score
- Risk Explanation
- Recommended Action

---

# ⚙ Technology Stack

## Frontend

- React.js
- Tailwind CSS
- Axios
- React Router DOM

## Backend

- Python
- Flask
- REST APIs

## Database

- MongoDB

## Machine Learning

- XGBoost
- Scikit-learn
- Pandas
- NumPy

## Notifications

- Twilio API
- WhatsApp API
- SMS API

---

# 📂 Project Structure

```
frontend/
│
├── public/
│
├── src/
│   ├── components/
│   │   ├── Navbar.jsx
│   │   ├── Sidebar.jsx
│   │   ├── ProductCard.jsx
│   │   ├── ProductGrid.jsx
│   │   ├── CartItem.jsx
│   │   ├── RiskBadge.jsx
│   │   ├── RiskScore.jsx
│   │   ├── RiskExplanation.jsx
│   │   ├── RecommendedAction.jsx
│   │   ├── SessionCard.jsx
│   │   ├── SessionTable.jsx
│   │   ├── MetricCard.jsx
│   │   └── Loading.jsx
│   │
│   ├── pages/
│   │
│   │── customer/
│   │     ├── Login.jsx
│   │     ├── Home.jsx
│   │     ├── ProductListing.jsx
│   │     ├── ProductDetails.jsx
│   │     ├── Cart.jsx
│   │     └── Checkout.jsx
│   │
│   │── dashboard/
│         ├── Dashboard.jsx
│         ├── LiveSessions.jsx
│         ├── SessionDetails.jsx
│         ├── HighRiskSessions.jsx
│         ├── ActionHistory.jsx
│         └── Analytics.jsx
│
├── App.jsx
├── main.jsx
├── index.css
│
├── package.json
├── tailwind.config.js
├── postcss.config.js
└── index.html
```

---

# 🗄 Database Collections

```
Users

Products

Sessions

CartEvents

Predictions

Recommendations
```

---

# 🤖 Machine Learning Model

The AI engine uses an **XGBoost Classifier** trained on customer session data.

### Features Used

- Pages Visited
- Time on Site
- Cart Value
- Product Count
- Checkout Attempts
- Payment Attempts
- Payment Failures
- Purchase History

### Output

- Risk Score (0–100%)
- Abandonment Reason
- Recommended Recovery Action

---

# 💡 Decision Agent

The Decision Agent determines the most appropriate recovery strategy based on the predicted risk.

Possible recommendations include:

- Do Nothing
- Send WhatsApp Reminder
- Retry Payment
- Offer Discount Coupon
- Offer Free Shipping
- Customer Support Assistance

---

# 🔥 REST APIs

## Customer APIs

```
POST /login

GET /products

GET /products/:id

POST /cart

POST /checkout

POST /payment
```

---

## Dashboard APIs

```
GET /dashboard

GET /sessions

GET /high-risk

GET /analytics
```

---

## AI APIs

```
POST /predict

POST /recommend
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/your-username/cart-rescue.git
```

## Frontend

```bash
cd frontend

npm install

npm run dev
```

## Backend

```bash
cd backend

pip install -r requirements.txt

python app.py
```

---

# 🌐 Local URLs

| Service | URL |
|----------|-----|
| Frontend | http://localhost:5173 |
| Dashboard | http://localhost:5173/dashboard |
| Backend | http://localhost:5000 |

---

# 📈 Project Workflow

```
Customer Login
      │
      ▼
Browse Products
      │
      ▼
Add to Cart
      │
      ▼
Checkout
      │
      ▼
Payment Attempt
      │
      ▼
Store Session Events
      │
      ▼
AI Prediction
      │
      ▼
Risk Score
      │
      ▼
Decision Agent
      │
      ▼
Recommendation
      │
      ▼
Dashboard
      │
      ▼
Admin Notification
```

---

# 🔮 Future Enhancements

- Deep Learning Models (LSTM / Transformers)
- Reinforcement Learning
- Kafka Event Streaming
- Explainable AI (SHAP)
- Cloud Deployment (AWS)
- Kubernetes Deployment
- Real-Time WebSocket Dashboard
- Personalized Offers
- Dynamic Pricing Integration

---

# 🏆 Key Highlights

- Real-Time Cart Monitoring
- AI-Based Risk Prediction
- Explainable Machine Learning
- Intelligent Decision Agent
- Live Admin Dashboard
- WhatsApp & SMS Integration
- Modular Architecture
- Scalable REST APIs
- MongoDB Session Storage
- Enterprise-Ready Design

---

# 👨‍💻 Team

**Project:** Cart Rescue – AI-Powered Cart Abandonment Prediction & Recovery

Developed as part of **AI Build 2026 – Track 2: Cart Rescue**

---

# 📜 License

This project is intended for educational and hackathon purposes.

---

<div align="center">

### ⭐ If you like this project, don't forget to Star the repository!

Made with ❤️ using React, Flask, MongoDB & AI

</div>