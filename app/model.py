def predict(text: str):
    if "free" in text.lower():
        return "spam"
    return "not spam"