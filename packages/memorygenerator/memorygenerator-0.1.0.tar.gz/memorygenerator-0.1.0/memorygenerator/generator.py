# memorygenerator/generator.py
import random

memories = {
    'childhood': [
        "Remember when you got your first bicycle?",
        "That time you tried to climb a tree and fell down.",
        "Your first day at school and you cried all day."
    ],
    'adventure': [
        "The time you went on a treasure hunt in the mountains.",
        "When you got lost in the forest and found a secret cave.",
        "The epic road trip across the country with friends."
    ],
    'dream': [
        "Flying over the city at night, feeling free as a bird.",
        "Meeting a talking cat who guided you through a magical land.",
        "Falling endlessly through a tunnel of colors."
    ]
}

def generate_memory(theme):
    if theme not in memories:
        raise ValueError(f"Invalid theme: {theme}. Choose from {list(memories.keys())}")
    return random.choice(memories[theme])
