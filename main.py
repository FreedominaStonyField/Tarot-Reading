import random

# Define the tarot card deck
tarot_deck = [
    "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
    "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
    "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance", "The Devil",
    "The Tower", "The Star", "The Moon", "The Sun", "Judgment", "The World",
    "Ace of Cups", "Two of Cups", "Three of Cups", "Four of Cups", "Five of Cups",
    "Six of Cups", "Seven of Cups", "Eight of Cups", "Nine of Cups", "Ten of Cups",
    "Page of Cups", "Knight of Cups", "Queen of Cups", "King of Cups",
    "Ace of Pentacles", "Two of Pentacles", "Three of Pentacles", "Four of Pentacles", "Five of Pentacles",
    "Six of Pentacles", "Seven of Pentacles", "Eight of Pentacles", "Nine of Pentacles", "Ten of Pentacles",
    "Page of Pentacles", "Knight of Pentacles", "Queen of Pentacles", "King of Pentacles",
    "Ace of Swords", "Two of Swords", "Three of Swords", "Four of Swords", "Five of Swords",
    "Six of Swords", "Seven of Swords", "Eight of Swords", "Nine of Swords", "Ten of Swords",
    "Page of Swords", "Knight of Swords", "Queen of Swords", "King of Swords",
    "Ace of Wands", "Two of Wands", "Three of Wands", "Four of Wands", "Five of Wands",
    "Six of Wands", "Seven of Wands", "Eight of Wands", "Nine of Wands", "Ten of Wands",
    "Page of Wands", "Knight of Wands", "Queen of Wands", "King of Wands",
]
# These Readings will be selected at random because i that is good enough for a fortine reading game.
tarot_readings = [
    "This means that there is uncertainty in your future.",
    "You will face unexpected challenges ahead.",
    "A period of change and transformation is approaching.",
    "This card suggests a need for introspection and soul-searching.",
    "You are about to embark on a journey of self-discovery.",
    "This signifies a time of balance and harmony in your life.",
    "Expect good fortune and success in your endeavors.",
    "A difficult decision lies ahead; trust your instincts.",
    "This card advises you to be patient and take your time.",
    "A period of joy and celebration is on the horizon.",
    "You may encounter obstacles, but with determination, you'll overcome them.",
    "This card signifies a major life transition or turning point.",
    "Prepare for a period of personal growth and enlightenment.",
    "Beware of deception and illusions; seek the truth.",
    "A dramatic change is imminent; embrace it with an open heart.",
    "This card suggests the need to release the past and move forward.",
    "You are in control of your destiny; take the reins.",
    "Prepare for unexpected opportunities and surprises.",
    "A period of emotional healing and renewal is approaching.",
    "This card encourages you to follow your passions and desires.",
    "Trust in your inner strength and resilience.",
    "A time of clarity and insight is on the horizon.",
    "You may face challenges, but they will lead to personal growth.",
    "This card signifies the end of a challenging phase in your life.",
    "Embrace new possibilities and adventures with an open mind.",
]


# Shuffle the tarot deck
random.shuffle(tarot_deck)

def draw_card():
    """Draw a single tarot card from the deck."""
    if len(tarot_deck) > 0:
        return tarot_deck.pop(0)
    else:
        return "The tarot deck is empty."

def main():
    print("""
Welcome to the Tarot Card Game! This game was made by me, Francisco Stanfield!
I made this game as part of this project for online pyton course.
Have some fun, don't take this too serously.
""")
    while True:
        user_input = input("Press 'd' to draw a card, 'q' to quit: ")
        if user_input == 'd':
            card = draw_card()
            print(f"You drew: {card}")
            print(tarot_readings[random.randrange(0, len(tarot_readings))])
        elif user_input == 'q':
            print("Thank you for playing!")
            break
        else:
            print("Invalid input. Please press 'd' to draw a card or 'q' to quit.")

if __name__ == "__main__":
    main()
