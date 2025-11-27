# capstone-project

#  Restaurant Reservation & Blog System – Capstone Project

## 1. Project Overview
**Purpose:** Full‑stack Django application for managing restaurant reservations and blog posts.  
**Features:** Responsive front‑end, CRUD functionality, role‑based authentication, notifications, deployment to cloud.  
**Tech Stack:** Django, Python, HTML/CSS/Bootstrap, PostgreSQL, Cloudinary, Heroku.

---

## 2. UX Design Process
- **Wireframes & Mockups:**
  - Homepage
  - Reservation form
  - Blog list/detail
  - Admin dashboard
- **Design Rationale:** Explanation of layouts, colours, and accessibility choices.  
- **Accessibility:** WCAG compliance, semantic HTML, alt text, ARIA labels.  
- **Responsiveness:** Screenshots of mobile/tablet/desktop views.

---

## 3. Database & Models
- **Schema Diagram (ER):** Show relationships between User, Reservation, Table, Post.
![ERD](assets/ERD.png)

- **Custom Models:**
  - **Reservation** – guest info, date/time, party size, status.
  - **Table** – number, capacity, location.
  - **Post** – blog content, author, timestamps.
- **Constraints:**
  - Party size > 0  
  - Reservation ≤ table capacity  
  - No double bookings
- **Migrations:** Document schema changes and version control.

---

## 4. CRUD Functionality
- **Create:** Reservation form, blog post form.  
- **Read:** Reservation list, blog list/detail.  
- **Update:** Edit reservation/post.  
- **Delete:** Cancel reservation/post.  
- **Access Control:** Customers manage their own reservations, admins manage all.

---

## 5. Authentication & Roles
- **Registration/Login:** Custom forms with validation.  
- **Roles:** Customer (default), Staff/Admin.  
- **Login State Reflection:** Navbar shows login/logout, conditional rendering.  
- **Access Control:** Restricted views based on role.

---

## 6. Testing
- **Python Tests:** Unit tests for models, views, forms; integration tests for booking flow.  
- **JavaScript Tests (if applicable):** Client‑side validation checks.  
- **Accessibility Tests:** Lighthouse/WAVE results.  
- **Responsiveness Tests:** Screenshots across devices.  
- **Testing Documentation:**
  - Table of test cases, expected vs actual results.
  - Key findings and fixes.

---

## 7. Version Control & Security
- **GitHub Repo:** Link to repository.  
- **Commit History:** Screenshots showing descriptive commit messages.  
- **Secure Code Management:**
  - `.env` for secrets  
  - `.gitignore` excludes sensitive files  
  - No hardcoded passwords or API keys

---

## 8. Deployment
- **Platform:** Heroku (with Postgres + Cloudinary).  
- **Deployment Steps:**
  1. Install Heroku CLI  
  2. Create app, add buildpacks  
  3. Configure environment variables  
  4. Push code, run migrations, collectstatic  
- **Verification:** Screenshots of deployed app.  
- **Security:** `DEBUG = False`, `ALLOWED_HOSTS` set, secrets in env vars.

---

## 9. AI Integration & Reflection
- **Code Creation:** AI scaffolding for models, forms, views.  
- **Debugging:** AI identified/fixed migration errors.  
- **Optimization:** AI suggested UX improvements (messages framework, Bootstrap styling).  
- **Reflection:**
  - How AI accelerated development  
  - How AI supported debugging  
  - How AI improved UX/performance  
  - Impact on workflow efficiency

---

## 10. Conclusion
- **Summary:** How the project meets all capstone criteria.  
- **Future Improvements:** Features to add (e.g., table availability checker, email notifications).  
- **Acknowledgements:** Tools, resources, and AI support.
