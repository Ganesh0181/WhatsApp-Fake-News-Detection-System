from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from twilio.twiml.messaging_response import MessagingResponse

from model import predict_news
from database import save_result

# ⚠️ only works if file exists
try:
    from broadcast import broadcast_message
except:
    broadcast_message = None

app = FastAPI()

# =========================
# CORS
# =========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# HOME
# =========================
@app.get("/")
def home():
    return {"message": "WhatsApp AI Bot Running 🚀"}


# =========================
# CHAT ENGINE
# =========================
def chat_engine(text: str):
    msg = text.lower().strip()

    if msg in ["hi", "hello", "hey"]:
        return "👋 Hello! Send me any news or message to analyze."

    if "your name" in msg:
        return "🤖 I am your Fake News Detection Bot"

    if "what can you do" in msg:
        return "I detect Fake News, Spam, Scam + Chat with you"

    return None


# =========================
# SMART ROUTER
# =========================
def smart_router(text: str):

    msg = text.lower().strip()

    spam_keywords = ["click here", "win money", "free gift", "urgent prize"]
    scam_keywords = ["earn money", "send money", "lottery", "bank", "otp", "password"]

    if any(w in msg for w in spam_keywords):
        return "SPAM / CLICKBAIT", 95.0

    if any(w in msg for w in scam_keywords):
        return "SCAM / FRAUD", 97.0

    if len(msg) < 15:
        return "NEED MORE INFO", 0.0

    return None


# =========================
# UI BUILDER (FINAL FIXED)
# =========================
def build_reply(prediction: str, confidence: float):

    if prediction == "NEED MORE INFO":
        return (
            "🤖 INSUFFICIENT INPUT\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n"
            "Please send full news/article/message\n"
            "Example: ISRO launched satellite"
        )

    # title mapping
    if "SPAM" in prediction:
        title = "🚨 SPAM / CLICKBAIT DETECTED"
        risk = "HIGH RISK"
    elif "SCAM" in prediction:
        title = "⛔ SCAM / FRAUD DETECTED"
        risk = "CRITICAL RISK"
    elif "FAKE" in prediction:
        title = "❌ FAKE NEWS DETECTED"
        risk = "FAKE NEWS"
    else:
        title = "✅ REAL / SAFE CONTENT"
        risk = "SAFE"

    # confidence bar
    bar_count = int(confidence / 10)
    bar = "█" * bar_count + "░" * (10 - bar_count)

    return f"""
{title}

{risk}

📊 Confidence: {confidence:.2f}%
[{bar}]
""".strip()


# =========================
# WHATSAPP WEBHOOK
# =========================
@app.post("/whatsapp")
async def whatsapp_bot(
    Body: str = Form(...),
    From: str = Form(...)
):

    print("\n========== NEW MESSAGE ==========")
    print("User:", From)
    print("Message:", Body)

    msg = Body.lower().strip()

    try:

        # 1. CHAT MODE
        chat_response = chat_engine(msg)
        if chat_response:
            reply_text = chat_response

        # 2. BROADCAST MODE
        elif msg.startswith("broadcast:") and broadcast_message:
            message = Body.replace("broadcast:", "").strip()
            result = broadcast_message(message)

            reply_text = f"""
🚀 Broadcast Completed

📊 Total: {result['total']}
✅ Success: {result['success']}
❌ Failed: {result['failed']}
""".strip()

        else:

            # 3. RULE ENGINE
            result = smart_router(Body)

            if result:
                prediction, confidence = result
                reply_text = build_reply(prediction, confidence)

            else:
                # 4. ML MODEL
                prediction, confidence = predict_news(Body)

                save_result(From, Body, prediction, confidence)

                reply_text = build_reply(prediction, confidence)

    except Exception as e:
        print("Error:", str(e))
        reply_text = "⚠️ System error occurred. Please try again."

    response = MessagingResponse()
    response.message(reply_text)

    return PlainTextResponse(str(response), media_type="application/xml")