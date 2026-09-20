import re
import random
from collections import defaultdict

from replies import REPLIES


# =========================================================
# CATEGORY DETECTION
# =========================================================
#
# This is intentionally simple and editable.
# Add words/phrases here as the project grows.
# =========================================================


CATEGORY_PATTERNS = {
    "greeting": [
        r"\bhi\b",
        r"\bhai\b",
        r"\bhello\b",
        r"\bhey\b",
        r"\bhelo\b",
        r"\bhii+\b",
        r"\bhy\b",
        r"\bda\b",
        r"\beda\b",
        r"\bentha\b",
        r"\bwhat'?s up\b",
        r"\bsugham\b",
    ],

    "ano": [
    r"\bano\b",
    ],

    "goodbye": [
        r"\bbye\b",
        r"\bgoodbye\b",
        r"\bsee you\b",
        r"\bsee ya\b",
        r"\bgn\b",
        r"\bgood night\b",
        r"\bpinne kanam\b",
        r"\bappo seri\b",
    ],

    "thanks": [
        r"\bthanks\b",
        r"\bthank you\b",
        r"\bthank u\b",
        r"\bthx\b",
        r"\bthanks da\b",
        r"\bnanni\b",
    ],

    "apology": [
        r"\bsorry\b",
        r"\bmy bad\b",
        r"\bsorry da\b",
        r"\benikku sorry\b",
        r"\bmy bad\b",
        r"\bsry\b",
    ],

    "bragging": [
        r"\bfull mark\b",
        r"\bfull marks\b",
        r"\btop mark\b",
        r"\btop marks\b",
        r"\btop ayi\b",
        r"\btop aayi\b",
        r"\bfirst ayi\b",
        r"\bfirst aayi\b",
        r"\bwon\b",
        r"\bwon the\b",
        r"\baced\b",
        r"\bgot first\b",
        r"\bhighest mark\b",
        r"\bhighest marks\b",
        r"\bgot \d+ marks?\b",
        r"\bscored \d+\b",
        r"\bI got\b.*\bmarks?\b",
        r"\bnjan\b.*\bmark\b",
        r"\bnjan\b.*\bwin\b",
        r"\bnjan\b.*\bwon\b",
        r"\bnjan\b.*\btop\b",
        r"\bexam\b.*\bfull\b",
    ],

    "success": [
        r"\bpassed\b",
        r"\bpass ayi\b",
        r"\bpass aayi\b",
        r"\bsucceeded\b",
        r"\bsuccess\b",
        r"\bdone\b",
        r"\bcompleted\b",
        r"\bfinished\b",
        r"\bgot the job\b",
        r"\bgot selected\b",
        r"\bselected ayi\b",
    ],

    "failure": [
        r"\bfailed\b",
        r"\bfail ayi\b",
        r"\bfail aayi\b",
        r"\blost\b",
        r"\bmistake\b",
        r"\bmessed up\b",
        r"\bscrewed up\b",
        r"\bdidn't work\b",
        r"\bnot work\b",
        r"\bcan't do\b",
        r"\bcannot do\b",
        r"\bparajayam\b",
    ],

    "insult": [
        r"\bstupid\b",
        r"\bidiot\b",
        r"\bdumb\b",
        r"\buseless\b",
        r"\bmoron\b",
        r"\btrash\b",
        r"\bshut up\b",
        r"\bpo da\b",
        r"\bmyre\b",
        r"\bpoda\b",
        r"\bpotta\b",
    ],

    "sad": [
        r"\bsad\b",
        r"\bdepressed\b",
        r"\bcrying\b",
        r"\bcry\b",
        r"\bupset\b",
        r"\blonely\b",
        r"\bhurt\b",
        r"\bfeeling bad\b",
        r"\bfeeling down\b",
        r"\bdesham\b",
        r"\bsankadam\b",
        r"\bvesham\b",
    ],

    "angry": [
        r"\bangry\b",
        r"\bmad\b",
        r"\bpissed\b",
        r"\bfurious\b",
        r"\bhate\b",
        r"\bverupp\b",
        r"\bdeshyam\b",
        r"\bdeshyam aanu\b",
    ],

    "bored": [
        r"\bbored\b",
        r"\bboring\b",
        r"\bnothing to do\b",
        r"\bonnum cheyyanilla\b",
        r"\bveruthe\b",
    ],

    "love": [
        r"\bi love you\b",
        r"\blove you\b",
        r"\bily\b",
        r"\bdo you love me\b",
        r"\bcrush\b",
    ],

    "obvious_question": [
        r"^what is 2\s*\+\s*2\??$",
        r"^what day is it\??$",
        r"^what time is it\??$",
        r"^what is my name\??$",
        r"^are you an ai\??$",
        r"^are you a bot\??$",
    ],

    "question": [
    r"\?",
    ],

}


# =========================================================
# RESPONSE MEMORY
# =========================================================
#
# We don't randomly pick a response.
# We cycle through the category's replies so the same
# reply is not immediately repeated.
# =========================================================

_next_reply_index = defaultdict(int)


def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"\s+", " ", text)
    return text


def detect_category(message: str) -> str:

    text = normalize(message)

    if not text:
        return "empty"

    # "ano" always gets priority
    if re.search(r"\bano\b", text):
        return "ano"

    # Any question gets the pucham1 reaction
    if "?" in text:
        return "question"

    scores = defaultdict(int)

    for category, patterns in CATEGORY_PATTERNS.items():

        for pattern in patterns:

            if re.search(pattern, text):

                scores[category] += max(
                    1,
                    len(pattern) // 8
                )

    if not scores:
        return "generic"

    return max(scores, key=scores.get)

def choose_reply(category: str) -> str:
    replies = REPLIES.get(category) or REPLIES["generic"]

    return random.choice(replies)

def emotion_for(category: str) -> str:
    emotion_map = {
        "greeting": "happy",
        "bragging": "jealous",
        "ano": "confused",
        "success": "happy",
        "failure": "sad",
        "thanks": "happy",
        "apology": "neutral",
        "insult": "angry",
        "sad": "supportive",
        "angry": "angry",
        "confused": "confused",
        "obvious_question": "sarcastic",
        "question": "sarcastic",
        "bored": "bored",
        "goodbye": "neutral",
        "love": "awkward",
        "empty": "confused",
        "generic": "neutral",
    }

    return emotion_map.get(category, "neutral")


def generate_response(message: str) -> dict:

    category = detect_category(message)

    # Every question gets pucham1
    if category == "question":
        return {
            "text": "",
            "emotion": "sarcastic",
            "meme": "memes/pucham1.jpg",
        }

    reply = choose_reply(category)

    # Meme response
    if reply.startswith("memes/"):
        return {
            "text": "",
            "emotion": emotion_for(category),
            "meme": reply,
        }

    # Text response
    return {
        "text": reply,
        "emotion": emotion_for(category),
        "meme": None,
    }