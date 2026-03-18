# Project Plan — Posting Objects (Digital Citizenship)

This plan outlines the steps to build a social media platform prototype in Python, with a focus on demonstrating how data is collected, used, and controlled.

---

## ✅ Objectives (What this project proves)

1. **Understand data collection**: Show what user data is stored (account info, interactions, timestamps) and why.
2. **Demonstrate data usage**: Explain how platforms use those data points (feed personalization, analytics, engagement metrics).
3. **Show privacy controls**: Give users ways to consent, export, or delete their data.
4. **Explain ethical concerns**: Address algorithmic bias, echo chambers, and data minimization.

---

## 🛠️ Implementation Phases

### Phase 1 — Base App (MVP)

1. Create a minimal Flask app (`app.py`)
2. Add user registration + login
3. Add profile pages
4. Add ability to create text posts
5. Add public feed (all posts)

**Deliverables:**
- Working app with login + posting
- Basic database schema (users, posts)

---

### Phase 2 — Data Tracking & Analytics

1. Implement an **event log** for actions like:
   - login/logout
   - view post
   - like/comment
   - follow/unfollow
2. Build a simple “analytics” view showing: 
   - most active users
   - most viewed posts
   - recent actions (event log)
3. Add “recommendation” logic (e.g., show posts from followed users first)

**Deliverables:**
- Event log store (SQLite table or JSON log)
- Dashboard view showing tracked data

---

### Phase 3 — Privacy & User Control

1. Add a **Consent/Privacy** landing page for first-time users
2. Add **profile privacy settings** (public vs private)
3. Implement `Download my data` (export user’s posts + events)
4. Implement `Delete my account` (remove user and related data)

**Deliverables:**
- Consent workflow
- Data export + deletion buttons

---

### Phase 4 — Project Write-up (Digital Citizenship Connection)

Write a short report (could be in the repo or a separate doc) describing:

- What data the app collects, why it collects it, and how it could be used.
- What data the app does not collect (data minimization).
- User data rights in the app (delete/export, privacy controls).
- Ethical considerations (algorithmic visibility, consent, transparency).

---

## 📌 How to Run (Quick Start)

1. Create and activate a virtual environment (recommended).
2. Install dependencies (`pip install -r requirements.txt`).
3. Run `python app.py`.
4. Open `http://localhost:5000` in your browser.

---

## ✅ Suggested Next Step
If you'd like, I can generate the initial scaffold for `app.py`, `models.py`, `templates/`, and the database schema so you can start with a working prototype immediately.