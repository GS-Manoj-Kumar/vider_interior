from django.shortcuts import render

# Create your views here.
import json
import urllib.request
from django.shortcuts import redirect
from django.contrib import messages
from .models import Lead
import os

WEBHOOK_URL = os.environ.get('MAKE_WEBHOOK_URL')


def submit_lead(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        country_code = request.POST.get('country_code', '+91')
        phone_raw = request.POST.get('phone', '').strip()
        phone = f"{country_code}{phone_raw}"
        bhk = request.POST.get('bhk', '')
        timeline = request.POST.get('timeline', '')
        budget = request.POST.get('budget', '')

        # Save to database
        Lead.objects.create(
            name=name,
            phone=phone,
            bhk=bhk,
            timeline=timeline,
            budget=budget,
        )

        # Forward to Make.com webhook
        payload = json.dumps({
            "name": name,
            "phone": phone,
            "bhk": bhk,
            "timeline": timeline,
            "budget": budget,
        }).encode('utf-8')

        try:
            req = urllib.request.Request(
                WEBHOOK_URL,
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            urllib.request.urlopen(req, timeout=5)
        except Exception as e:
            print(f"Webhook error: {e}")

        # Success message
        messages.success(request, "Thank you! We'll call you within 24 hours.")
        return redirect('/#consultation-form')

    return redirect('/')