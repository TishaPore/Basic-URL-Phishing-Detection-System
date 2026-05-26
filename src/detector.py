def check_url(url):
    suspicious_words = ["login", "verify", "bank", "secure"]

    for word in suspicious_words:
        if word in url.lower():
            return "⚠️ Suspicious URL Detected"

    return "✅ URL Appears Safe"
