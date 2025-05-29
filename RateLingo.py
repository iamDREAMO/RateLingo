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


# Word count per-word text
def count_words(text):
    words = text.strip().split()
    return len(words)


# Main Application logic (CLI Flow)

# App's homepage
def main():
    print("\nWelcome to RateLingo - The Twi Language Service Pricing Tool\n")
    print("Available Services: translation, transcription, voiceover, subtitling")
    
    # user input: Select Service Type
    service = input("\nEnter the service type: ").strip().lower()
    rate = get_service_rate(service)
    
    if rate is None:
        print("‼️ Invalid service. Please choose a valid option.")
        return
    
    # user input: Enter Text
    print("\nPaste or type the text you want to process. Press Enter twice(2x) to finish:\n")
    lines = []
    while True:
        line = input()
        if not line:
            break
        lines.append(line)
        
    full_text = "\n".join(lines)
    
    # Calculate Word Count and Cost
    word_count = count_words(full_text)
    total_cost = word_count * rate
    
    # Print Final Output
    print(f"service: {service.capitalize()}")
    print(f"Word Count: {word_count}")
    print(f"Rate per word: ${rate:.2f}")
    print(f"Total Cost: ${total_cost:.2f}")

if __name__ == "__main__":
    main()