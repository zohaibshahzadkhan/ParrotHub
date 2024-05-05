import os

os.environ.setdefault("DATABASE_URL","Starting with 'postgres://', only required for deployment")
os.environ.setdefault("SECRET_KEY","YOUR KEY HERE")
os.environ.setdefault("CLOUDINARY_URL","Starting with 'cloudinary://'")