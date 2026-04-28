"""
RateLingo Core Module
Contains business logic for rate calculations and word counting
"""

class ServiceRates:
    """Manages service types and their rates"""
    
    SERVICES = {
        "translation": {
            "rate": 0.25,
            "description": "Twi-English translation services"
        },
        "transcription": {
            "rate": 0.10,
            "description": "Audio/video to text transcription"
        },
        "voiceover": {
            "rate": 0.15,
            "description": "Professional voice-over recording"
        },
        "subtitling": {
            "rate": 0.12,
            "description": "Video subtitling and captions"
        }
    }
    
    @classmethod
    def get_rate(cls, service):
        """
        Get the rate for a specific service
        
        Args:
            service (str): Service name
            
        Returns:
            float: Rate per word or None if service not found
        """
        service_data = cls.SERVICES.get(service.lower())
        return service_data["rate"] if service_data else None
    
    @classmethod
    def get_description(cls, service):
        """
        Get the description for a specific service
        
        Args:
            service (str): Service name
            
        Returns:
            str: Service description or None if service not found
        """
        service_data = cls.SERVICES.get(service.lower())
        return service_data["description"] if service_data else None
    
    @classmethod
    def get_all_services(cls):
        """
        Get list of all available services
        
        Returns:
            list: List of service names
        """
        return list(cls.SERVICES.keys())
    
    @classmethod
    def is_valid_service(cls, service):
        """
        Check if a service is valid
        
        Args:
            service (str): Service name to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        return service.lower() in cls.SERVICES


class WordCounter:
    """Handles text processing and word counting"""
    
    @staticmethod
    def count_words(text):
        """
        Count words in the provided text
        
        Args:
            text (str): Text to count words from
            
        Returns:
            int: Number of words
        """
        if not text or not text.strip():
            return 0
        
        # Split by whitespace and filter empty strings
        words = text.strip().split()
        return len(words)
    
    @staticmethod
    def count_characters(text, include_spaces=True):
        """
        Count characters in the provided text
        
        Args:
            text (str): Text to count characters from
            include_spaces (bool): Whether to include spaces in count
            
        Returns:
            int: Number of characters
        """
        if not text:
            return 0
        
        if include_spaces:
            return len(text)
        else:
            return len(text.replace(" ", "").replace("\n", "").replace("\t", ""))


class PricingCalculator:
    """Calculates pricing based on word count and service rates"""
    
    @staticmethod
    def calculate_cost(word_count, rate):
        """
        Calculate total cost based on word count and rate
        
        Args:
            word_count (int): Number of words
            rate (float): Rate per word
            
        Returns:
            float: Total cost
        """
        return word_count * rate
    
    @staticmethod
    def calculate_service_cost(text, service):
        """
        Calculate cost for a specific service and text
        
        Args:
            text (str): Text to process
            service (str): Service type
            
        Returns:
            dict: Dictionary containing word_count, rate, and total_cost
                  or None if service is invalid
        """
        if not ServiceRates.is_valid_service(service):
            return None
        
        word_count = WordCounter.count_words(text)
        rate = ServiceRates.get_rate(service)
        total_cost = PricingCalculator.calculate_cost(word_count, rate)
        
        return {
            "service": service.capitalize(),
            "word_count": word_count,
            "rate": rate,
            "total_cost": total_cost,
            "description": ServiceRates.get_description(service)
        }
    
    @staticmethod
    def format_cost(cost):
        """
        Format cost as currency string
        
        Args:
            cost (float): Cost to format
            
        Returns:
            str: Formatted cost string (e.g., "$12.50")
        """
        return f"${cost:.2f}"