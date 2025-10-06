# crypto_chatbot.py

class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.greeting = "Hey there! Let's find you a green and growing crypto! 🌱🚀"
        
        # Predefined crypto database
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            },
            "Solana": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10
            },
            "Polkadot": {
                "price_trend": "stable",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 7/10
            }
        }
        
        self.disclaimer = "⚠️  Disclaimer: Crypto is risky—always do your own research! This is not financial advice."

    def get_rising_cryptos(self):
        """Find cryptocurrencies with rising price trends"""
        rising = []
        for crypto, data in self.crypto_db.items():
            if data["price_trend"] == "rising":
                rising.append(crypto)
        return rising

    def get_sustainable_cryptos(self, min_score=0.7):
        """Find cryptocurrencies with high sustainability scores"""
        sustainable = []
        for crypto, data in self.crypto_db.items():
            if data["sustainability_score"] >= min_score:
                sustainable.append((crypto, data["sustainability_score"]))
        # Sort by sustainability score in descending order
        return sorted(sustainable, key=lambda x: x[1], reverse=True)

    def get_profitable_cryptos(self):
        """Find cryptocurrencies with high profitability potential"""
        profitable = []
        for crypto, data in self.crypto_db.items():
            if data["price_trend"] == "rising" and data["market_cap"] in ["high", "medium"]:
                profitable.append(crypto)
        return profitable

    def get_balanced_recommendation(self):
        """Find cryptocurrencies that balance profitability and sustainability"""
        balanced = []
        for crypto, data in self.crypto_db.items():
            score = 0
            # Profitability factors
            if data["price_trend"] == "rising":
                score += 3
            if data["market_cap"] == "high":
                score += 2
            elif data["market_cap"] == "medium":
                score += 1
                
            # Sustainability factors
            score += data["sustainability_score"] * 3
                
            balanced.append((crypto, score))
        
        return sorted(balanced, key=lambda x: x[1], reverse=True)

    def analyze_crypto(self, crypto_name):
        """Provide detailed analysis of a specific cryptocurrency"""
        if crypto_name in self.crypto_db:
            data = self.crypto_db[crypto_name]
            analysis = f"""
Analysis for {crypto_name}:
• Price Trend: {data['price_trend'].upper()}
• Market Cap: {data['market_cap'].upper()}
• Energy Use: {data['energy_use'].upper()}
• Sustainability Score: {data['sustainability_score']*10}/10

"""
            if data["sustainability_score"] >= 0.7:
                analysis += "🌱 Excellent sustainability choice!\n"
            if data["price_trend"] == "rising":
                analysis += "+ : Currently trending upward!\n"
                
            return analysis
        else:
            return f"Sorry, I don't have data for {crypto_name}. Try: {', '.join(self.crypto_db.keys())}"

    def process_query(self, user_input):
        """Process user input and generate response"""
        user_input = user_input.lower()
        
        if any(word in user_input for word in ["hello", "hi", "hey", "greetings"]):
            return f"{self.greeting}\n\nI can help you with:\n• Trending cryptocurrencies \n• Sustainable coins \n• Investment recommendations \n• Crypto analysis \n\nWhat would you like to know?"
        
        elif any(word in user_input for word in ["trend", "rising", "going up", "profit"]):
            rising = self.get_rising_cryptos()
            if rising:
                response = " Currently trending cryptocurrencies:\n"
                for crypto in rising:
                    response += f"• {crypto}\n"
                response += f"\n{self.disclaimer}"
                return response
            else:
                return "No cryptocurrencies are currently showing strong upward trends."
        
        elif any(word in user_input for word in ["sustainable", "eco", "green", "environment"]):
            sustainable = self.get_sustainable_cryptos()
            if sustainable:
                response = "🌱 Most sustainable cryptocurrencies:\n"
                for crypto, score in sustainable:
                    response += f"• {crypto} (Score: {score*10}/10)\n"
                response += f"\n{self.disclaimer}"
                return response
            else:
                return "No highly sustainable cryptocurrencies found."
        
        elif any(word in user_input for word in ["recommend", "suggest", "advice", "investment"]):
            balanced = self.get_balanced_recommendation()
            if balanced:
                top_pick = balanced[0][0]
                data = self.crypto_db[top_pick]
                response = f"💡 Based on profitability and sustainability, I recommend:\n\n"
                response += f"🏆 {top_pick}!\n"
                response += f"• Price Trend: {data['price_trend']}\n"
                response += f"• Market Cap: {data['market_cap']}\n"
                response += f"• Sustainability: {data['sustainability_score']*10}/10\n"
                response += f"• Energy Use: {data['energy_use']}\n\n"
                response += f"🌟 Why? It balances growth potential with environmental responsibility!\n\n"
                response += self.disclaimer
                return response
        
        elif any(word in user_input for word in ["analyze", "analysis", "info about"]):
            for crypto in self.crypto_db.keys():
                if crypto.lower() in user_input:
                    return self.analyze_crypto(crypto)
            return "Which cryptocurrency would you like me to analyze? Try: Bitcoin, Ethereum, Cardano, etc."
        
        elif any(word in user_input for word in ["list", "show all", "available"]):
            response = "📋 Available cryptocurrencies in my database:\n"
            for crypto in self.crypto_db.keys():
                response += f"• {crypto}\n"
            response += f"\nAsk me about any of them!"
            return response
        
        elif any(word in user_input for word in ["thank", "thanks"]):
            return "You're welcome! Happy investing! 🚀"
        
        elif any(word in user_input for word in ["exit", "quit", "bye"]):
            return "Goodbye! Remember: " + self.disclaimer
        
        else:
            return """I'm not sure I understand. Try asking me:
• "Which cryptos are trending?"
• "What's the most sustainable coin?"
• "Recommend an investment"
• "Analyze Bitcoin"
• "List available cryptos"

Or type 'exit' to end our chat."""

    def chat(self):
        """Main chat loop"""
        print(f"🤖: {self.greeting}")
        print("Type 'exit' to end the conversation\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                print(f"🤖: Goodbye! Remember: {self.disclaimer}")
                break
                
            response = self.process_query(user_input)
            print(f"🤖: {response}\n")

# Run the chatbot
if __name__ == "__main__":
    bot = CryptoBuddy()
    bot.chat()