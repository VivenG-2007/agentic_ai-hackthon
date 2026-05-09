from fastapi import FastAPI, UploadFile
import sqlite3
import subprocess
import asyncio
import yaml
import requests
import os

app = FastAPI()

DATABASE_URL = os.getenv("DB_URL", "sqlite:///:memory:")
API_SECRET = os.getenv("API_SECRET", "default_secret")

if not DATABASE_URL:
    print("DB_URL is not set, using default value")
    DATABASE_URL = "sqlite:///:memory:"

if not API_SECRET:
    print("API_SECRET is not set, using default value")
    API_SECRET = "default_secret"

if DATABASE_URL.startswith("sqlite"):
    conn = sqlite3.connect(DATABASE_URL.split("://")[1])
else:
    conn = sqlite3.connect(DATABASE_URL)
cursor = conn.cursor()