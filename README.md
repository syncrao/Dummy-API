# Dummy-API
https://ecea-2401-4900-7d87-36c2-f9b5-fe5d-ebbd-e378.ngrok-free.app/api/school/
## Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/your-username/Dummy-API.git
cd Dummy-API

# 2. Create and activate virtual environment
python3 -m venv env
source env/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply migrations
python manage.py migrate

# 5. (Optional) Create superuser
python manage.py createsuperuser

# 6. Run the server
python manage.py runserver
