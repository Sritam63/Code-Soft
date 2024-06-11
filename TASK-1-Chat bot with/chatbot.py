import random
import re

class SupportBot:
    
    def __init__(self):
        self.negative_res = ("no", "nope", "not a chance", "sorry")
        self.exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "farewell")
        self.support_responses = {
            'ask_about_product': r'.*\bproduct\b.*',
            'technical_support': r'.*\btechnical\b.*support.*',
            'about_returns': r'.*\breturn\b.*policy.*',
            'general_query': r'.*\bhelp\b.*'
        }

    def greet(self):
        name = input("Hello! Welcome to our customer support. What is your name?\n")
        will_help = input(f"Hi {name}, how can I assist you today?\n")
        if will_help.lower() in self.negative_res:
            print("Alright, have a great day!")
            return
        self.chat()

    def make_exit(self, reply):
        if any(command in reply for command in self.exit_commands):
            print("Thanks for reaching out. Have a great day!")
            return True
        return False
    
    def chat(self):
        reply = input("Please tell me your query: ").lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply)).lower()

    def match_reply(self, reply):
        for intent, regex_pattern in self.support_responses.items():
            if re.search(regex_pattern, reply):
                if intent == 'ask_about_product':
                    return self.ask_about_product()
                elif intent == 'technical_support':
                    return self.technical_support()
                elif intent == 'about_returns':
                    return self.about_returns()
                elif intent == 'general_query':
                    return self.general_query()
        return self.no_match_intent()

    def ask_about_product(self):
        responses = (
            "Our product is top-notch and has excellent reviews!\n", 
            "You can find all product details on our website.\n"
        )
        return random.choice(responses)
    
    def technical_support(self):
        responses = (
            "For technical support, please describe the issue in detail.\n",
            "Our technical support team is here to assist you. Can you please provide more details about the problem?\n"
        )
        return random.choice(responses)
    
    def about_returns(self):
        responses = (
            "Our return policy allows you to return products within 30 days of purchase.\n",
            "You can return the product within 30 days of receiving it. For more details, please visit our return policy page.\n"
        )
        return random.choice(responses)
    
    def general_query(self):
        responses = (
            "How can I help you today?\n",
            "Please provide more details about your query so I can assist you better.\n"
        )
        return random.choice(responses)

    def no_match_intent(self):
        responses = (
            "I'm sorry, I didn't understand that. Could you please rephrase?\n",
            "Can you provide more details or ask your question differently?\n"
        )
        return random.choice(responses)

if __name__ == "__main__":
    bot = SupportBot()
    bot.greet()
