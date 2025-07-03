# ✨ EduWeb - Smart Learning Portal

A smart and responsive online learning platform built with **Django** and **Django REST Framework** (DRF). It provides secure, scalable APIs and an admin-friendly interface to manage courses, instructors, and students.

---

## 📄 Description

**Edunext** is a full-stack educational platform for managing online courses. It allows users to register, log in, and interact with educational content using secure APIs. The admin panel enables easy course and user management.

This project showcases my backend development skills using Django, DRF, and API integration — ideal for internships and developer roles.

---

## 🚀 Features

- 📚 View all available courses
- 👩‍🏫 Instructor list and details
- 🎓 Secure student registration with token-based login
- 🔐 Token Authentication using DRF
- 🧪 API tested via Postman
- 🛠️ Admin dashboard to manage all data
- 📈 Scalable project structure using Django best practices

---

## 🔐 API Endpoints (DRF)

| Method | Endpoint                        | Description                        |
|--------|----------------------------------|------------------------------------|
| GET    | `/api/courses/`                 | List all courses                   |
| GET    | `/api/instructors/`             | List all instructors               |
| GET    | `/api/students/`                | List all students                  |
| POST   | `/api/student/register/`        | Register a new student             |
| POST   | `/api/custom-login/`            | Login and get token auth           |

---

## 📸 Screenshots

> ✅ Visual preview of key pages and APIs used

| Page/API | Screenshot |
|----------|------------|
| Index Page | ![Index]("[edunext_project/pictures/home.png](https://github.com/Karannannaware/edunext_project/blob/6e874caba8e86f226a9977d6db1dfe2caf9eaca2/edunext_project/pictures/home.png)") |
| Admin Dashboard | ![Admin](screenshot) |
| Courses API | ![Courses](screenshots/api_courses.png) |
| Instructors API | ![Instructors](screenshots/api_instructors.png) |
| Students API | ![Students](screenshots/api_students.png) |
| Student Registration API | ![Register](screenshots/api_register.png) |
| Custom Login API | ![Login](screenshots/api_login.png) |

> 📝 Place your screenshots inside a `screenshots/` folder in the GitHub repo for proper linking.

---

## ⚙️ Setup Instructions

Follow these steps to run the project locally:

```bash
# 1. Clone the repository
git clone https://github.com/your-username/edunext_project.git
cd edunext_project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create a superuser for admin access
python manage.py createsuperuser

# 6. Start the server
python manage.py runserver
