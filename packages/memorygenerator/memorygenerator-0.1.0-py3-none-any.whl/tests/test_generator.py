# tests/test_generator.py
import pytest
from memorygenerator.generator import generate_memory

def test_generate_memory_childhood():
    memory = generate_memory('childhood')
    assert memory in [
        "Remember when you got your first bicycle?",
        "That time you tried to climb a tree and fell down.",
        "Your first day at school and you cried all day."
    ]

def test_generate_memory_invalid_theme():
    with pytest.raises(ValueError):
        generate_memory('invalid_theme')
