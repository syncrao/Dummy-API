from django.contrib.auth.hashers import make_password
from School_API.models import User

users = [
  { "name": "Shahrukh Rao", "email": "shahrukh1@example.com", "password": "password123" },
  { "name": "Ayesha Khan", "email": "ayesha.k@example.com", "password": "password123" },
  { "name": "Rohan Mehta", "email": "rohan.mehta@example.com", "password": "password123" },
  { "name": "Fatima Ali", "email": "fatima.ali@example.com", "password": "password123" },
  { "name": "Aman Verma", "email": "aman.verma@example.com", "password": "password123" },
  { "name": "Sara Sheikh", "email": "sara.sheikh@example.com", "password": "password123" },
  { "name": "Zaid Hussain", "email": "zaid.h@example.com", "password": "password123" },
  { "name": "Mehak Bano", "email": "mehak.bano@example.com", "password": "password123" },
  { "name": "Imran Siddiqui", "email": "imran.sid@example.com", "password": "password123" },
  { "name": "Nida Raza", "email": "nida.raza@example.com", "password": "password123" },
  { "name": "Faizan Shaikh", "email": "faizan.s@example.com", "password": "password123" },
  { "name": "Bushra Ansari", "email": "bushra.ans@example.com", "password": "password123" },
  { "name": "Karan Kapoor", "email": "karan.kapoor@example.com", "password": "password123" },
  { "name": "Anjali Singh", "email": "anjali.singh@example.com", "password": "password123" },
  { "name": "Yusuf Pathan", "email": "yusuf.p@example.com", "password": "password123" },
  { "name": "Neha Yadav", "email": "neha.yadav@example.com", "password": "password123" },
  { "name": "Adnan Qureshi", "email": "adnan.q@example.com", "password": "password123" },
  { "name": "Ritika Jain", "email": "ritika.jain@example.com", "password": "password123" },
  { "name": "Mohit Chauhan", "email": "mohit.c@example.com", "password": "password123" },
  { "name": "Sana Mirza", "email": "sana.mirza@example.com", "password": "password123" }
]


for u in users:
    User.objects.create(
        name=u["name"],
        email=u["email"],
        password=make_password(u["password"])
    )


print("done")

