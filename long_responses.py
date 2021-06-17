
# coding: utf-8
import random

R_EATING = "I don't like eat, not hungry"

def unknown():
    response = ["could you please re-phase that?", "sounds about right", "what does that mean?"][random.randrange(3)]
    
    return response