from django.shortcuts import render
import stripe
import os
from dotenv import load_dotenv


load_dotenv()
stripe.api_key = os.getenv("API_KEY")


