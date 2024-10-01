import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL','postgresql://postgres.bnqdbkonvykhsvnaxviv:sefa52073406@aws-0-eu-central-1.pooler.supabase.com:6543/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False