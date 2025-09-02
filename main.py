# Version simulation pour apprendre sans API
import os
from dotenv import load_dotenv
import random

load_dotenv()

# Simuler la configuration
print("Simulated AI client successfully configured.")

# Définir le message
my_message = "Write a Poem to my mom Laila congratulating her for her 74th birthday!"
print(f"Sending message to AI: '{my_message}'")

# Simulation d'une réponse AI
def simulate_ai_response(message):
    """Simule une réponse d'IA pour l'apprentissage"""
    
    # Différentes réponses selon le contenu du message
    if "poem" in message.lower() and "birthday" in message.lower():
        poems = [
            """🎉 Happy 74th Birthday, Dear Laila! 🎉

Seventy-four years of wisdom and grace,
A mother's love that time cannot erase.
Your gentle heart and caring ways,
Have brightened all our nights and days.

May this special day bring you joy,
Like when you raised your precious child.
Your laughter fills our hearts with cheer,
Happy Birthday, Mother dear!

With all our love on this special day,
May happiness come your way! 💕""",
            
            """🌹 Pour Maman Laila - 74 Ans de Bonheur 🌹

Soixante-quatorze printemps de vie,
Maman Laila, notre étoile qui brille.
Tes yeux pétillent de mille sourires,
Ton cœur déborde de doux souvenirs.

Aujourd'hui nous célébrons ton jour,
Avec tendresse et tout notre amour.
Que cette année t'apporte la paix,
Et tous les bonheurs que tu mérites!

Joyeux anniversaire, Maman chérie! 🎂✨"""
        ]
        return random.choice(poems)
    
    return "Bonjour! Comment puis-je vous aider aujourd'hui?"

# Simuler l'appel API
print("\n🤖 Simulated AI Reply: \n")
ai_reply_content = simulate_ai_response(my_message)
print(f"{ai_reply_content}")

print("\n" + "="*50)
print("📚 APPRENTISSAGE:")
print("- Votre code fonctionne parfaitement!")
print("- Structure correcte pour les appels API")
print("- Prêt pour une vraie API quand vous en aurez une")
print("="*50)