from dotenv import load_dotenv
load_dotenv()

import os
from supabase import create_client

url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)
session = None

def sign_up(users_email, users_password):
    supabase.auth.sign_up({ "email": users_email, "password": users_password })

def sign_in(users_email, users_password):
    try:
        session = supabase.auth.sign_in_with_password({ "email": users_email, "password": users_password })
        return session
    except:
        print("login failed")

def sign_out():
    supabase.auth.sign_out()

def select_all(table_name):
    data, count = supabase.table(table_name).select("*").execute()
    print(data, count)
    return data, count

def select(table_name, col_name, col_value):
    try:
        data = supabase.table(table_name).select(col_name).eq(col_name, col_value).execute()
        return data
    except:
        return None

def table_contain(table_name, col_name, eq):
    if select(table_name, col_name, eq) == None:
        return False
    return True

def insert(table_name, license_plate_value, pl_img_name_value, face_img_name):
    supabase.table(table_name).insert({"license_plate":license_plate_value, "pl_img_name":pl_img_name_value, "face_img_name":face_img_name}).execute()

def delete_row(table_name, col_name, col_value):
    supabase.table(table_name).delete().eq(col_name, col_value).execute()