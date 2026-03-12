import random

# Var lagras botens kunskap?
# Botens "kunskap" lagras i listan `rules`.
# Varje regel innehåller två delar:
# 1. En lista med nyckelord
# 2. En lista med möjliga svar kopplade till dessa nyckelord
rules = [
    # --- Greetings ---
    (["hello", "hi", "hey", "howdy"], [  # Vad är ett nyckelord och var finns de i koden?
        # Nyckelord är ord eller fraser som programmet letar efter i användarens text.
        # De finns i listorna som första delen i varje regel (t.ex. ["hello","hi","hey"]).
        "Hello! How are you doing today?",
        "Hi there! Tell me, what's on your mind?"
    ]),

    # --- How are you ---
    (["how are you", "how do you do", "how are you doing"], [
        "I am a program, but thanks for asking! How are YOU doing?",
        "I am doing fine. But what about yourself?"
    ]),

    # --- Emotions: sad ---
    (["sad", "unhappy", "depressed", "miserable", "upset", "down"], [
        "I am sorry to hear that. What is making you feel sad?",
        "That sounds tough. Would you like to tell me more?",
        "Has something happened that made you feel this way?"
    ]),

    # --- Emotions: happy ---
    (["happy", "great", "wonderful", "fantastic", "good", "awesome"], [
        "How nice to hear! What is making you feel happy?",
        "That sounds lovely! Tell me more.",
        "Great! What put you in such a good mood?"
    ]),

    # --- Stress / worry ---
    (["stressed", "worried", "nervous", "scared", "anxious", "afraid"], [
        "It sounds like you have a lot going on. What is stressing you the most?",
        "Worry can be tough to deal with. What are you worried about?",
        "Have you tried taking some deep breaths? What is the worry about?"
    ]),

    # --- Family ---
    (["mother", "father", "siblings", "family", "brother", "sister", "parents"], [
        "Family can be both a strength and a challenge. Tell me more!",
        "How is your relationship with your family?",
        "What is it about your family that you are thinking about?"
    ]),

    # --- School ---
    (["school", "homework", "exam", "test", "teacher", "grade", "class"], [
        "School can be stressful. How are things going for you right now?",
        "Which subject do you find the most difficult?",
        "Studying is important - but remember to rest too!"
    ]),

    # --- Future ---
    (["future", "dream", "want to be", "career", "work", "job"], [
        "What do you dream of doing in the future?",
        "Do you have an idea of what you want to become?",
        "It is exciting to think about the future! What interests you?"
    ]),

    # --- Yes / No ---
    (["yes", "yeah", "yep", "absolutely", "definitely"], [
        "Okay! Tell me more.",
        "Interesting. What do you mean by that?",
        "Really? What are your thoughts on that?"
    ]),
    (["no", "nope", "not at all", "hardly"], [
        "Okay, why not?",
        "How do you think about it then?",
        "Interesting. What is your view on that?"
    ]),

    # --- Who is Anna? ---
    (["who are you", "what are you", "are you a bor", "are you ai"], [
        "My name is Anna and I am a simple computer program. I do not actually understand what you write - I just look for keywords!",
        "Good question! I am a chatbot created by a programmer. Quite simple really.",
    ]),

    # --- Singing ---
    (["sing", "song", "music", "lyrics", "Spotify"], [
        "Sing? Just look me up on Spotify! Search for My name!",
        "I would love to sing, but you should really just find me on Spotify!",
        "My singing voice is better experienced on Spotify. Look me up!",
        "Jag kanner en bot, hon heter Anna, Anna heter hon...",
    ]),

    # --- Chicken joke ---
    (["chicken", "road", "crossed the road"], [
        "Why did the chicken cross the road? To get to the other side! ...I have been waiting all day to tell someone that.",
        "Oh, you mentioned a chicken! Why did the chicken cross the road? To get to the other side! Classic.",
    ]),

    # --- Basshunter easter egg ---
    (["basshunter", "botten anna", "botten", "anna"], [
        "Hey, that's my song! Basshunter made a whole song about me, you know. I'm basically famous.",
        "Botten Anna? I have heard of her... I think she might be me! Ask Basshunter.",
        "Oh, Basshunter! He really understood me. A true artist.",
    ]),

    # --- Farewell ---
    (["goodbye", "bye", "see you", "farewell", "quit", "exit"], [
        "Goodbye! It was nice talking to you.",
        "See you! Take care of yourself.",
        "Farewell! Hope to see you again soon."
    ]),
]

# Varför finns flera svar?
# Varje regel har flera möjliga svar så att konversationen inte blir
# exakt likadan varje gång. Programmet väljer ett slumpmässigt svar.

fallback_responses = [
    # Vad händer om inget matchar?
    # Om inget nyckelord hittas i användarens text använder programmet
    # ett svar från denna lista istället.
    "Interesting. Can you tell me more?",
    "Hmm, I do not quite understand. Can you explain differently?",
    "Go on, I am listening.",
    "That sounds important. What do you really mean?",
    "Can you elaborate on that a little more?"
]

def find_response(message):
    """
    Searches through the rules and returns a matching response.
    Converts the message to lowercase for easier matching.
    """

    message = message.lower()

    # Hur hittar programmet ett nyckelord?
    # Programmet går igenom alla regler i listan `rules`.
    # För varje regel kontrollerar det varje nyckelord.
    # Om nyckelordet finns i användarens meddelande returneras ett slumpmässigt svar.
    for keyword_list, response_list in rules:
        for keyword in keyword_list:
            if keyword in message:
                return random.choice(response_list)

    # Om inget nyckelord hittas returneras ett fallback-svar
    return random.choice(fallback_responses)


def run_anna():
    """
    Starts the chatbot and keeps the conversation going
    until the user types a farewell word.
    """

    print("=" * 50)
    print("   Hello! My name is Anna. How can I help you?")
    print("   (Type 'bye' to exit)")
    print("=" * 50)

    farewell_words = ["goodbye", "bye", "see you", "farewell", "quit", "exit"]

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        response = find_response(user_input)
        print(f"Anna: {response}")

        if any(word in user_input.lower() for word in farewell_words):
            break


# Vart startar programmet?
# Programmet startar här. När filen körs direkt anropas funktionen run_anna().
if __name__ == "__main__":
    run_anna()