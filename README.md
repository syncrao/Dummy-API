# 🚀 Dummy API

A simple API for school-related user login and validation.

🌐 **Base URL**
[`https://raoapi.vercel.app/api/school/`](https://raoapi.vercel.app/api/school/)

---

## 🔐 User Authentication

### 📋 User List

**GET**
[`https://raoapi.vercel.app/api/school/newuser/`](https://raoapi.vercel.app/api/school/newuser/)

### 🔑 User Login Validation

**POST**
[`http://raoapi.vercel.app/api/school/login/`](http://raoapi.vercel.app/api/school/login/)

**Request Body:**

```json
{
  "username": "syncrao",
  "password": "yourpassword"
}
```

**Response (Success - 200 OK):**

```json
{
  "message": "Login successful",
  "username": "rao",
  "id": "37ddb35c-7c21-4fb9-9f7b-27201179f0cc"
}
```

**Response (Failure - 401 Unauthorized):**

```json
{
  "error": "Invalid username or password"
}
```



## ⚙️ Setup Instructions

```bash
# 1️⃣ Clone the repository
git clone https://github.com/your-username/Dummy-API.git
cd Dummy-API

# 2️⃣ Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply database migrations
python manage.py migrate

# 5️⃣ (Optional) Create a superuser
python manage.py createsuperuser

# 6️⃣ Start the development server
python manage.py runserver
```

---

