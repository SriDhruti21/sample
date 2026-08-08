# Cart Rescue

### Intelligent Cart Abandonment Prediction & Recovery System

Cart Rescue is an intelligent e-commerce platform that predicts cart abandonment in real time by analyzing customer behavior during their shopping journey. The system provides abandonment risk predictions, explains the factors influencing the prediction, and recommends the most appropriate recovery action to improve customer conversion.

Developed as part of **AI Build 2026 – Track 2: Cart Rescue**.

---

# Overview

Cart abandonment is a common challenge faced by e-commerce platforms. Customers may leave before completing their purchase due to payment failures, long checkout processes, delivery concerns, or price comparisons.

Cart Rescue continuously monitors customer sessions, analyzes behavioral patterns using machine learning, predicts abandonment risk, and recommends the most suitable action instead of applying the same strategy to every customer.

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

- Real-Time Session Monitoring
- Customer Behavior Analysis
- Feature Extraction
- Abandonment Risk Prediction
- Risk Score Generation
- Risk Explanation
- Intelligent Decision Recommendation

## Admin Dashboard

- Dashboard Overview
- Live Customer Sessions
- High Risk Sessions
- Session Details
- Action History
- Analytics

---

# System Workflow

```text
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

Cart_Rescue/
│
├── backend/
│   ├── routes/
│   │   ├── admin_routes.py         
│   │   ├── auth_routes.py           
│   │   ├── event_routes.py          
│   │   ├── product_routes.py        
│   │   └── session_routes.py        
│   │
│   ├── app.py                      
│   ├── config.py                    
│   ├── database.py                  
│   ├── decision_service.py         
│   ├── session_manager.py           
│   ├── twilio_service.py            
│   ├── create_admin.py              
│   ├── fix_admin.py                 
│   ├── test_api.py                 
│   ├── requirements.txt
│   └── .env                       
│
├── frontend/
│   ├── public/
│   │
│   ├── src/
│   │   ├── assets/
│   │   │
│   │   ├── components/
│   │   │   ├── AddToCartButton.jsx  
│   │   │   ├── Categories.jsx
│   │   │   ├── FeaturedProducts.jsx
│   │   │   ├── Footer.jsx
│   │   │   ├── Hero.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── Newsletter.jsx
│   │   │   └── Testimonials.jsx
│   │   │
│   │   ├── context/
│   │   │   └── SessionContext.jsx  
│   │   │
│   │   ├── pages/
│   │   │   ├── admin/
│   │   │   │   ├── AdminLayout.jsx
│   │   │   │   ├── AdminDashboard.jsx
│   │   │   │   ├── LiveSessions.jsx
│   │   │   │   ├── HighRiskSessions.jsx
│   │   │   │   ├── SessionDetail.jsx     
│   │   │   │   ├── ActionHistory.jsx
│   │   │   │   ├── Analytics.jsx
│   │   │   │   └── Admin.css
│   │   │   │
│   │   │   ├── Cart.jsx             
│   │   │   ├── Home.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   │   ├── Shop.jsx
│   │   │   ├── Auth.css
│   │   │   └── Cart.css
│   │   │
│   │   ├── App.jsx                
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   │
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
├── ml/
│   ├── datasets/                  
│   ├── realtime/
│   │   ├── realtime_features.py    
│   │   ├── risk_scorer.py           
│   │   ├── scenario_detector.py    
│   │   └── action_engine.py         
│   │
│   ├── saved_models/
│   │   └── xgboost.pkl              
│   │
│   ├── feature_engineering.py
│   ├── preprocessing.py
│   ├── xgboost_model.py
│   └── ...
│
├── .gitignore
└── README.md

---

# Machine Learning

The prediction engine uses an **XGBoost Classifier** trained on customer session data.

### Features Used

- Pages Visited
- Time on Site
- Cart Value
- Product Count
- Checkout Attempts
- Payment Attempts
- Payment Failures
- Purchase History

### Prediction Output

- Risk Score
- Predicted Reason
- Recommended Action

---

# Decision Agent

Possible recommendations include:

- Do Nothing
- Send Reminder
- Retry Payment
- Offer Discount Coupon
- Offer Free Shipping
- Customer Support Assistance

---

# Installation

## Clone Repository

```bash
git clone https://github.com/your-username/Hackathon1.git
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

# Team

Developed by

- P. Nithish
- Tallapaneni Sri Dhruti
- Akhilakoppolu

---

Thank you for taking the time to review our project.
