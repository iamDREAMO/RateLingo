"""
RateLingo CLI Module
Command-line interface for RateLingo
"""

from core import ServiceRates, WordCounter, PricingCalculator


class CLI:
    """Command-line interface for RateLingo"""
    
    def __init__(self):
        self.running = True
    
    def print_header(self):
        """Display application header"""
        print("\n" + "=" * 60)
        print("  RateLingo - Twi Language Service Pricing Calculator")
        print("=" * 60)
        print()
    
    def print_services(self):
        """Display available services"""
        print("Available Services:")
        print("-" * 60)
        for service in ServiceRates.get_all_services():
            rate = ServiceRates.get_rate(service)
            description = ServiceRates.get_description(service)
            print(f"  • {service.capitalize():<15} ${rate:.2f}/word")
            print(f"    {description}")
        print("-" * 60)
    
    def get_service_input(self):
        """
        Get service selection from user
        
        Returns:
            str: Selected service or None if invalid
        """
        service = input("\nEnter service type: ").strip().lower()
        
        if not ServiceRates.is_valid_service(service):
            print("❌ Invalid service. Please choose from the list above.")
            return None
        
        return service
    
    def get_text_input(self):
        """
        Get text input from user (supports multi-line)
        
        Returns:
            str: User's text input
        """
        print("\nPaste or type your text below.")
        print("Press Enter twice (on an empty line) to finish:\n")
        
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        
        return "\n".join(lines)
    
    def display_results(self, result):
        """
        Display calculation results
        
        Args:
            result (dict): Calculation results from PricingCalculator
        """
        print("\n" + "=" * 60)
        print("  CALCULATION RESULTS")
        print("=" * 60)
        print(f"Service:        {result['service']}")
        print(f"Description:    {result['description']}")
        print(f"Word Count:     {result['word_count']:,} words")
        print(f"Rate per Word:  {PricingCalculator.format_cost(result['rate'])}")
        print("-" * 60)
        print(f"TOTAL COST:     {PricingCalculator.format_cost(result['total_cost'])}")
        print("=" * 60)
    
    def ask_continue(self):
        """
        Ask user if they want to continue
        
        Returns:
            bool: True if user wants to continue, False otherwise
        """
        choice = input("\nWould you like to calculate another quote? (y/n): ").strip().lower()
        return choice in ['y', 'yes']
    
    def run(self):
        """Main CLI application loop"""
        self.print_header()
        
        while self.running:
            self.print_services()
            
            # Get service selection
            service = self.get_service_input()
            if service is None:
                if not self.ask_continue():
                    break
                continue
            
            # Get text input
            text = self.get_text_input()
            
            if not text.strip():
                print("⚠️  No text provided. Please enter some text to calculate.")
                if not self.ask_continue():
                    break
                continue
            
            # Calculate and display results
            result = PricingCalculator.calculate_service_cost(text, service)
            self.display_results(result)
            
            # Ask to continue
            if not self.ask_continue():
                break
        
        print("\nThank you for using RateLingo! 👋")
        print("Visit: https://github.com/iamDREAMO/RateLingo\n")


def main():
    """Entry point for CLI application"""
    app = CLI()
    app.run()


if __name__ == "__main__":
    main()