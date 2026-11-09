#!/usr/bin/env python3
"""
Ra-udo's Little Adventure
A short text adventure based on the Game Ideas document.
"""

import random
import time
import sys

# ---------------------------------------------------------------------------
# Character & world data (taken directly from the design notes)
# ---------------------------------------------------------------------------

SPECIES_LIFESPAN = 5000
PLAYER_AGE = 3852
# 1500 years ≈ 13 human years → roughly 1 year ≈ 0.00867 human years
HUMAN_EQUIV = round(PLAYER_AGE * (13 / 1500))

APPEARANCE = (
    "You have three eyes, one ear, five noses, one mouth, "
    "three arms, four legs, ten fingers on each hand, and seven toes on each foot."
)

CLOTHING = (
    "Your clothes look almost like human clothes, but they have been cleverly "
    "altered so they fit your three arms and four legs comfortably."
)

HOME = "Your home is nice, cozy, and calm. Soft light filters in and everything smells familiar."

# Naming rules reminder (used in flavour text)
# Boys' names end with “du”. Girls' names end with anything except “du”.

# ---------------------------------------------------------------------------
# Dialogue pools
# ---------------------------------------------------------------------------

MUDU_LINES = [
    "Mudu scratches one of his five noses. \"The weather feels the same as it did three hundred years ago.\"",
    "Mudu looks at you with all three eyes. \"Don't forget to come home before the twin moons rise.\"",
    "Mudu mutters, \"I once walked to the Crystal Dunes when I was your age. Took me forty years.\"",
    "Mudu waves one of his three arms lazily. \"Adventure is fine. Just remember where the door is.\"",
    "Mudu says, \"Your mother left some stewed root-fruit on the table. Eat before you go.\"",
]

MADIMOONA_LINES = [
    "MadiMoona suddenly appears from another room. \"Ra-udo! Did you pack an extra pair of walking socks for your seven toes?\"",
    "MadiMoona pops her head around the doorway. \"Be kind to the old stones. They remember everything.\"",
    "MadiMoona hums a short tune. \"The wind told me you would leave today. It usually tells the truth.\"",
    "MadiMoona gives you a quick three-armed hug. \"Come back with stories, not just dust.\"",
    "MadiMoona says softly, \"Your father pretends not to worry. He worries.\"",
]

MANI_NUDU_LINES = [
    "Mani Nudu grins with all three eyes. \"I knew you'd finally come out! The eastern path is whispering today.\"",
    "Mani Nudu stretches his four legs. \"Race you to the Whispering Arch? Winner gets the last sweet-root.\"",
    "Mani Nudu lowers his voice. \"Ramnundu has been sitting under the old listening tree again. He might have a riddle for us.\"",
    "Mani Nudu points with one of his three arms. \"I found a new trail that smells like rain and old metal. Want to see?\"",
]

RAMNUNDU_LINES = [
    "Ramnundu opens his one ear fully. \"The ground remembers every footstep. Walk lightly and it may answer.\"",
    "Ramnundu regards you with calm three-eyed patience. \"A question asked in haste often receives an answer that takes centuries.\"",
    "Ramnundu nods slowly. \"You carry the restlessness of the young. That is not a flaw. Just do not let it become a chain.\"",
    "Ramnundu says, \"There is a hollow stone near the southern ridge. Place your hand inside and listen. It only speaks once.\"",
]

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def slow_print(text, delay=0.03):
    """Print text with a gentle typewriter effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def pause(seconds=1.0):
    time.sleep(seconds)

def clear_screen():
    print("\n" * 2)

def choice(prompt, options):
    """Present numbered options and return the chosen index (0-based)."""
    print()
    for i, opt in enumerate(options, 1):
        print(f"  {i}. {opt}")
    while True:
        try:
            raw = input("\n> ").strip()
            num = int(raw)
            if 1 <= num <= len(options):
                return num - 1
        except ValueError:
            pass
        print("Please enter a number from the list.")

# ---------------------------------------------------------------------------
# Game sections
# ---------------------------------------------------------------------------

def intro():
    clear_screen()
    slow_print("=== Ra-udo's Little Adventure ===")
    pause(0.8)
    print()
    slow_print(f"You are Ra-udo.")
    slow_print(f"You are {PLAYER_AGE} years old. Your people usually live about {SPECIES_LIFESPAN} years.")
    slow_print(f"In human terms you would be roughly {HUMAN_EQUIV} years old — still young, full of curiosity.")
    pause(0.6)
    print()
    slow_print(APPEARANCE)
    slow_print(CLOTHING)
    pause(0.8)
    print()
    slow_print("You like going on a lot of adventures.")
    pause(1.0)

def at_home():
    clear_screen()
    slow_print("You stand in your home.")
    slow_print(HOME)
    pause(0.8)

    # Father
    print()
    slow_print("Your father, Mudu, is nearby.")
    pause(0.4)
    slow_print(random.choice(MUDU_LINES))
    pause(1.0)

    # Mother (she pops up randomly)
    if random.random() < 0.85:  # almost always appears at the start
        print()
        slow_print(random.choice(MADIMOONA_LINES))
        pause(1.0)

    print()
    slow_print("The day stretches ahead of you. What do you want to do?")
    options = [
        "Step outside and look for your friend Mani Nudu",
        "Stay home a little longer and talk to Mudu again",
        "Call out for MadiMoona once more",
        "Just head out into the world on your own"
    ]
    choice_idx = choice("Choose:", options)

    if choice_idx == 0:
        return "friend"
    elif choice_idx == 1:
        return "talk_mudu"
    elif choice_idx == 2:
        return "talk_mother"
    else:
        return "explore_alone"

def talk_mudu_again():
    clear_screen()
    slow_print(random.choice(MUDU_LINES))
    pause(1.0)
    slow_print("Mudu seems content to keep saying soft, ordinary things.")
    print()
    slow_print("You decide it is time to go outside.")
    pause(0.8)
    return "friend"

def talk_mother_again():
    clear_screen()
    slow_print(random.choice(MADIMOONA_LINES))
    pause(1.0)
    slow_print("MadiMoona smiles with all three eyes and then drifts away again.")
    print()
    slow_print("You feel ready to leave the cozy house.")
    pause(0.8)
    return "friend"

def meet_friend():
    clear_screen()
    slow_print("Outside, the air is mild. Four-legged footprints of many sizes mark the soft ground.")
    pause(0.6)
    slow_print("You soon find Mani Nudu waiting near the path that leads away from the village.")
    pause(0.5)
    slow_print(random.choice(MANI_NUDU_LINES))
    pause(1.0)

    print()
    slow_print("Mani Nudu looks at you expectantly.")
    options = [
        "Suggest going to see the wise villager Ramnundu",
        "Propose exploring a new trail together",
        "Ask Mani Nudu what he has been up to lately",
        "Invite him back to your house for a while"
    ]
    choice_idx = choice("What do you say?", options)

    if choice_idx == 0:
        return "wise"
    elif choice_idx == 1:
        return "trail"
    elif choice_idx == 2:
        return "chat_friend"
    else:
        return "back_home"

def chat_with_friend():
    clear_screen()
    slow_print("Mani Nudu stretches all four legs and talks for a while.")
    slow_print("He tells you about a shiny stone he found, a bird with two songs, and how the river tasted different last season.")
    pause(1.2)
    slow_print("Eventually he says, \"We should do something real today. Let's go see Ramnundu.\"")
    pause(0.8)
    return "wise"

def explore_trail():
    clear_screen()
    slow_print("The two of you follow a faint trail that smells of rain and old metal.")
    pause(0.7)
    slow_print("After a long walk (which still feels short by your people's standards) you reach a quiet ridge.")
    pause(0.6)
    slow_print("There is a hollow stone half-buried in the ground. It looks exactly like the one Ramnundu sometimes mentions.")
    pause(0.8)
    print()
    slow_print("Mani Nudu whispers, \"Should we put a hand inside?\"")
    options = [
        "Yes — place one of your three hands into the hollow",
        "Better ask Ramnundu about it first",
        "Leave it alone and head back"
    ]
    choice_idx = choice("What do you do?", options)

    if choice_idx == 0:
        return "hollow_stone"
    elif choice_idx == 1:
        return "wise"
    else:
        return "end_quiet"

def visit_wise():
    clear_screen()
    slow_print("You find Ramnundu sitting under the old listening tree, just as expected.")
    pause(0.5)
    slow_print(random.choice(RAMNUNDU_LINES))
    pause(1.2)

    print()
    slow_print("Ramnundu waits, one ear fully open.")
    options = [
        "Ask him if there is something you should be looking for",
        "Tell him about the hollow stone on the ridge",
        "Simply sit quietly with him for a while",
        "Thank him and continue exploring with Mani Nudu"
    ]
    choice_idx = choice("What do you do?", options)

    if choice_idx == 0:
        return "quest_hint"
    elif choice_idx == 1:
        return "hollow_advice"
    elif choice_idx == 2:
        return "sit_quiet"
    else:
        return "trail"

def hollow_stone_event():
    clear_screen()
    slow_print("You carefully slide one hand into the cool hollow.")
    pause(1.0)
    slow_print("For a moment nothing happens. Then a soft vibration travels up your arm.")
    pause(0.8)
    slow_print("A voice that is not quite a voice speaks inside your mind:")
    pause(0.6)
    slow_print("\"The path you walk is still being written. Walk it with all three eyes open.\"")
    pause(1.2)
    slow_print("The feeling fades. Mani Nudu stares at you, three eyes wide.")
    slow_print("\"What did it say?\" he asks.")
    pause(0.8)
    slow_print("You tell him. The two of you sit in silence for a long, comfortable while.")
    pause(1.0)
    return "end_wonder"

def hollow_advice():
    clear_screen()
    slow_print("Ramnundu listens carefully.")
    pause(0.5)
    slow_print("\"The hollow stone speaks only once to each person,\" he says. \"If you have not yet heard it, you may try. If you have, it will remain silent.\"")
    pause(1.0)
    slow_print("He adds, \"Either way, the message is usually the same: keep walking, and keep looking.\"")
    pause(0.8)
    return "trail"

def quest_hint():
    clear_screen()
    slow_print("Ramnundu considers your question for a long time — long even for your people.")
    pause(1.0)
    slow_print("\"There is no great danger today,\" he finally says. \"There is only the ordinary world, which is already full of things worth noticing.\"")
    pause(0.8)
    slow_print("\"If you need a direction, walk toward the place that feels least familiar. That is usually enough.\"")
    pause(1.0)
    return "trail"

def sit_quiet():
    clear_screen()
    slow_print("You sit beside Ramnundu under the listening tree.")
    pause(0.8)
    slow_print("No one speaks for a long time. The wind moves through the leaves. Somewhere far away a creature with seven toes walks past.")
    pause(1.2)
    slow_print("When you finally stand, Ramnundu simply nods. You feel calmer than before.")
    pause(0.8)
    return "end_calm"

def back_home_with_friend():
    clear_screen()
    slow_print("You and Mani Nudu return to your cozy home.")
    pause(0.5)
    slow_print("Mudu looks up and says something mild and forgettable.")
    if random.random() < 0.6:
        slow_print(random.choice(MADIMOONA_LINES))
    pause(0.8)
    slow_print("The four of you (counting Mani Nudu) spend a quiet stretch of time together.")
    pause(1.0)
    return "end_home"

def explore_alone():
    clear_screen()
    slow_print("You set out alone.")
    pause(0.6)
    slow_print("The world feels large and quiet. Your four legs carry you steadily.")
    pause(0.8)
    slow_print("After a while you find yourself near the old listening tree. Ramnundu is there.")
    pause(0.6)
    return "wise"

def ending(ending_type):
    clear_screen()
    if ending_type == "end_wonder":
        slow_print("The day ends with a quiet sense of wonder.")
        slow_print("You and Mani Nudu walk home under the twin moons, talking about what the stone might have meant.")
        slow_print("Somewhere behind you, the hollow stone keeps its silence for the next person.")
    elif ending_type == "end_calm":
        slow_print("You return home feeling settled.")
        slow_print("Mudu is still saying soft, ordinary things. MadiMoona appears just long enough to smile.")
        slow_print("Tomorrow there will be more paths.")
    elif ending_type == "end_home":
        slow_print("The cozy house holds you all for a while.")
        slow_print("Adventure can wait. Sometimes the best part of leaving is knowing you can come back.")
    elif ending_type == "end_quiet":
        slow_print("You and Mani Nudu leave the hollow stone undisturbed.")
        slow_print("Some things are better approached with a little more knowing.")
        slow_print("The path home feels friendly under your seven-toed feet.")
    else:
        slow_print("The day simply continues, the way days do.")

    pause(1.2)
    print()
    slow_print("— End of this little adventure —")
    print()
    slow_print("Thank you for walking a while as Ra-udo.")
    slow_print("(Names follow the rule: boys end in “du”. Girls do not.)")
    print()

# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------

def main():
    intro()
    state = "home"

    while True:
        if state == "home":
            state = at_home()
        elif state == "talk_mudu":
            state = talk_mudu_again()
        elif state == "talk_mother":
            state = talk_mother_again()
        elif state == "friend":
            state = meet_friend()
        elif state == "chat_friend":
            state = chat_with_friend()
        elif state == "trail":
            state = explore_trail()
        elif state == "wise":
            state = visit_wise()
        elif state == "hollow_stone":
            state = hollow_stone_event()
        elif state == "hollow_advice":
            state = hollow_advice()
        elif state == "quest_hint":
            state = quest_hint()
        elif state == "sit_quiet":
            state = sit_quiet()
        elif state == "back_home":
            state = back_home_with_friend()
        elif state == "explore_alone":
            state = explore_alone()
        elif state.startswith("end_"):
            ending(state)
            break
        else:
            # Fallback
            ending("end_quiet")
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nYou decide to rest for now. The adventure will wait.")
        sys.exit(0)
