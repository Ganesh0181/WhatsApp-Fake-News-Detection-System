from twilio.rest import Client
from dotenv import load_dotenv
import os
import time

# =========================
# LOAD ENV
# =========================
load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_WHATSAPP_NUMBER")


# =========================
# VALIDATION
# =========================
def validate_env():
    missing = []

    if not account_sid:
        missing.append("TWILIO_ACCOUNT_SID")
    if not auth_token:
        missing.append("TWILIO_AUTH_TOKEN")
    if not twilio_number:
        missing.append("TWILIO_WHATSAPP_NUMBER")

    if missing:
        raise ValueError(
            f"❌ Missing environment variables: {', '.join(missing)}"
        )


validate_env()

client = Client(account_sid, auth_token)


# =========================
# FORMAT NUMBER
# =========================
def format_whatsapp_number(number: str) -> str:
    number = str(number).strip()
    return number if number.startswith("whatsapp:") else f"whatsapp:{number}"


# =========================
# SEND MESSAGE (PRODUCTION)
# =========================
def send_whatsapp_message(
    to: str,
    message: str,
    retries: int = 3,
    base_delay: float = 1.5
):

    to = format_whatsapp_number(to)
    last_error = None

    permanent_errors = [
        "not a valid phone number",
        "authentication",
        "permission",
        "invalid from"
    ]

    for attempt in range(1, retries + 1):

        try:
            response = client.messages.create(
                body=message,
                from_=twilio_number,
                to=to
            )

            print(f"✅ Sent successfully → {to}")
            print(f"🆔 SID: {response.sid}")

            return {
                "status": "success",
                "sid": response.sid,
                "to": to,
                "attempts": attempt
            }

        except Exception as e:
            last_error = str(e).lower()
            print(f"❌ Attempt {attempt}/{retries} failed: {last_error}")

            # 🚫 stop retries for permanent errors
            if any(err in last_error for err in permanent_errors):
                print("🚫 Permanent error detected. Stopping retries.")
                break

            # 🔁 exponential backoff retry
            if attempt < retries:
                wait_time = base_delay * (2 ** (attempt - 1))
                print(f"🔁 Retrying in {wait_time:.2f}s...")
                time.sleep(wait_time)

    print(f"🚨 Final failure: {last_error}")

    return {
        "status": "failed",
        "error": last_error,
        "to": to
    }