# RateLingo: CLI-based Twi language service pricing calculator

# Define services
def get_service_rate(service):
    rates = {
        "translation": 0.25,
        "transcription": 0.10,
        "voiceover": 0.15,
        "subtitling": 0.12
    }
    return rates.get(service.lower())

# Define wordcount
def count_words(text):