# ✏️ Replace EVERYTHING in this file with your own game from OnlineGDB.
#    (Click the pencil icon, select all, paste, then Commit changes.)

"""
Bodega Run - a state machine demo

Mr. Cruz has $5 and a craving. Get him to the bodega.
Watch the [STATE] line: every turn the program checks what state
he's in FIRST, and that decides what can happen next.
"""
import random

ROUTE = [
    {"type": "og", "name": "OG Papo", "where": "on his milk crate by the laundromat",
     "says": "Back in '89 this block had a payphone that WORKED. Respect the payphone."},
    {"type": "bandit", "name": "Sticky Fingers Stevie", "where": "lurking by the scaffolding",
     "toll": 2},
    {"type": "og", "name": "Ms. Gladys", "where": "watching the whole block from her window",
     "says": "Mijo, fix your collar. And tell those kids to do their homework."},
    {"type": "bandit", "name": "Two-Dollar Tony", "where": "posted up by the ATM that's always broken",
     "toll": 3},  # inflation hit Tony too
]


def ask(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"  Pick one of: {', '.join(options)}")


state = "walking"   # walking | og | bandit | bodega | broke
money = 5
respect = 0         # how many OGs you showed love to
stop = 0            # how far along the route you are
who = None          # who you're dealing with right now

print("Mr. Cruz leaves the house with $5. Destination: the bodega.")

while state not in ("bodega", "broke"):
    print(f"\n[STATE: {state.upper()} | ${money} | respect: {respect}]")

    if state == "walking":
        if stop == len(ROUTE):
            state = "bodega"
            continue
        who = ROUTE[stop]
        stop += 1
        print(f"You spot {who['name']} {who['where']}.")
        state = who["type"]  # someone shows up -> switch state

    elif state == "og":
        if ask(f"(t)alk to {who['name']} or (n)od and keep it moving? ", ["t", "n"]) == "t":
            print(f"{who['name']}: \"{who['says']}\"")
            respect += 1
            print("  +1 respect. Word gets around.")
        else:
            print(f"{who['name']} squints at you. Noted.")
        state = "walking"

    elif state == "bandit":
        if respect > 0:  # SAME bandit, different outcome -- because of state
            print(f"{who['name']} sees the OGs nod at you. \"Oh my bad, Mr. Cruz. Have a blessed day.\"")
        else:
            print(f"{who['name']}: \"Ayo teach, lemme hold ${who['toll']}.\"")
            if ask("(r)un or (p)ay the toll? ", ["r", "p"]) == "r":
                if random.random() < 0.5:
                    print("You hit him with the teacher speed-walk. Escaped!")
                else:
                    print(f"You trip over a MetroCard. He gets ${who['toll']} anyway.")
                    money -= who["toll"]
            else:
                print(f"You hand over ${who['toll']}. At least he said thank you.")
                money -= who["toll"]
        state = "broke" if money <= 0 else "walking"

print(f"\n[STATE: {state.upper()} | ${money}]")
if state == "broke":
    print("Mr. Cruz is broke before he reaches the door. The bodega cat stares in disappointment.")
elif money == 5:
    print("Full $5 intact. Chopped cheese AND an Arizona. Legendary run.")
elif money >= 3:
    print(f"Made it with ${money}. Chopped cheese secured. Minor losses.")
else:
    print(f"Made it with ${money}. One quarter water and your dignity. Barely.")
