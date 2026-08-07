# Cart Rescue

### Intelligent Cart Abandonment Prediction & Recovery System

Cart Rescue is an intelligent e-commerce solution that helps businesses identify customers who are likely to abandon their shopping carts. The system analyzes customer behavior in real time, predicts abandonment risk using machine learning, and recommends the most suitable action to improve conversion rates.

This project was developed as part of **AI Build 2026 – Track 2: Cart Rescue**.

---

# Overview

Cart abandonment is one of the biggest challenges faced by e-commerce platforms. Customers often leave without completing their purchase due to reasons such as payment failures, long checkout processes, or simply losing interest.

Cart Rescue continuously monitors customer activity, predicts the likelihood of cart abandonment, explains the reason behind the prediction, and suggests an appropriate recovery action instead of applying the same solution to every customer.

---

# Features

## Customer Portal

- Customer Login
- Home Page
- Product Listing
- Product Details
- Shopping Cart
- Checkout
- Payment Processing

## AI Prediction Engine

- Real-time Session Monitoring
- Customer Behavior Analysis
- Feature Extraction
- Abandonment Risk Prediction
- Risk Explanation
- Intelligent Action Recommendation

## Admin Dashboard

- Dashboard Overview
- Live Customer Sessions
- High Risk Sessions
- Session Details
- Action History
- Analytics

---

# System Workflow

```
Customer Login
      │
      ▼
Browse Products
      │
      ▼
View Product
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
Machine Learning Prediction
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
Dashboard Update
```

---

# Dashboard

The dashboard allows administrators to monitor customer sessions in real time.

### Dashboard Modules

- Dashboard
- Live Sessions
- Session Details
- High Risk Sessions
- Action History
- Analytics

### Session Details

Selecting a customer session displays:

- Customer ID
- Products Viewed
- Cart Value
- Pages Visited
- Time on Site
- Payment Attempts
- Payment Status
- Risk Score
- Risk Explanation
- Recommended Action

---

# Technology Stack

## Frontend

- React.js
- Tailwind CSS
- Axios
- React Router

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

- Twilio
- WhatsApp API
- SMS API

---

# Project Structure

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
│   ├── customer/
│   │   ├── Login.jsx
│   │   ├── Home.jsx
│   │   ├── ProductListing.jsx
│   │   ├── ProductDetails.jsx
│   │   ├── Cart.jsx
│   │   └── Checkout.jsx
│   │
│   └── dashboard/
│       ├── Dashboard.jsx
│       ├── LiveSessions.jsx
│       ├── SessionDetails.jsx
│       ├── HighRiskSessions.jsx
│       ├── ActionHistory.jsx
│       └── Analytics.jsx
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

# Database Collections

```
Users

Products

Sessions

CartEvents

Predictions

Recommendations
```

---

# Machine Learning

The prediction engine uses an **XGBoost Classifier** to estimate the probability of cart abandonment.

### Features Used

- Pages Visited
- Time on Site
- Cart Value
- Number of Products
- Checkout Attempts
- Payment Attempts
- Payment Failures
- Purchase History

### Prediction Output

- Risk Score
- Risk Level
- Possible Reason
- Recommended Action

---

# Decision Agent

Based on the predicted risk score, the Decision Agent recommends the most suitable action.

Possible recommendations include:

- Do Nothing
- Send Reminder
- Retry Payment
- Offer Discount
- Free Shipping
- Customer Support Assistance

---

# REST APIs

## Customer APIs

```
POST /login

GET /products

GET /products/{id}

POST /cart

POST /checkout

POST /payment
```

## Dashboard APIs

```
GET /dashboard

GET /sessions

GET /high-risk

GET /analytics
```

## AI APIs

```
POST /predict

POST /recommend
```

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/<your-username>/Hackathon1.git
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

# Local Setup

| Service | URL |
|---------|-----|
| Frontend | http://localhost:5173 |
| Dashboard | http://localhost:5173/dashboard |
| Backend | http://localhost:5000 |

---

# Future Improvements

- Personalized recovery strategies
- Email notifications
- Explainable AI visualizations
- Cloud deployment
- Real-time event streaming
- Performance monitoring
- Advanced analytics

---

# Team

Developed by:

- P. Nithish
- Tallapaneni Sri Dhruti
- Akhila koppolu

---

# License

This project was developed for the **AI Build 2026 Hackathon** as an academic and demonstration project.

---

Thank you for taking the time to review our project.