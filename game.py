import random

# Rebranded Route Obstacles and Characters
ROUTE = [
    {
        "type": "vip",
        "name": "Vice Principal Vance",
        "where": "standing by the main gates checking watches",
        "says": "Punctuality is the bedrock of academic excellence, Mr. Cruz.",
    },
    {
        "type": "hazard",
        "name": "Stairwell Traffic Jam",
        "where": "blocking the central stairs",
        "time_cost": 5,
        "energy_cost": 2,
    },
    {
        "type": "vip",
        "name": "Dr. Aris Thorne (Research Fellow)",
        "where": "peering out from the wet lab",
        "says": "Ah, Cruz! Remember to review those lab reports today!",
    },
    {
        "type": "hazard",
        "name": "Freshly Mopped Hallway",
        "where": "slippery tiles stretching outside the department wing",
        "time_cost": 6,
        "energy_cost": 3,
    },
]

def ask(prompt, options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in options:
            return choice
        print(f"Pick one of: {', '.join(options)}")

# Game Variables
state = "walking"  # walking | vip | hazard | class | broke
energy = 5
time_left = 12   # Minutes remaining until class starts
respect = 0
stop = 0
who = None

print("=== RACE TO CLASS ===")
print("Class starts in 12 minutes! Mr. Cruz leaves the faculty lounge with 5 Energy.")

while state not in ("class", "broke"):
    print(f"\n[STATE: {state.upper()} | Time Left: {time_left} min | Energy: {energy} | Respect: {respect}]")
    
    if state == "walking":
        if stop == len(ROUTE):
            state = "class"
            continue
        who = ROUTE[stop]
        stop += 1
        print(f"You spot {who['name']} {who['where']}.")
        state = who["type"]
        
    elif state == "vip":
        print(f"{who['name']} is nearby.")
        choice = ask("(t)alk briefly (+1 respect, loses 2 min) or (n)od and sprint past (saves time)? ", ["t", "n"])
        
        if choice == "t":
            print(f"{who['name']}: \"{who['says']}\"")
            respect += 1
            time_left -= 2
            print("-> +1 Respect earned! (Cost 2 minutes)")
        else:
            print(f"You offer a polite nod to {who['name']} and keep moving.")
            time_left -= 1
        
        state = "walking"
        
    elif state == "hazard":
        print(f"Hazard Ahead: {who['name']}.")
        
        if respect > 0:
            print(f"Your high respect ({respect}) lets you use a staff-only clearance keycard!")
            time_left -= 1
            respect -= 1
            print("-> Passed smoothly around the hazard! (-1 min)")
        else:
            choice = ask(f"(w)ait it out (loses {who['time_cost']} min) or (s)print through (costs {who['energy_cost']} energy, 60% chance to save time)? ", ["w", "s"])
            
            if choice == "w":
                print(f"You tread carefully... losing {who['time_cost']} minutes.")
                time_left -= who["time_cost"]
            else:
                if random.random() < 0.6:
                    print("Sprint successful! You burst through the delay in 1 minute!")
                    time_left -= 1
                    energy -= 1
                else:
                    print(f"You stumbled! Lost {who['energy_cost']} energy and {who['time_cost']} minutes pushing through.")
                    energy -= who["energy_cost"]
                    time_left -= who["time_cost"]

        # Check failure condition
        if energy <= 0:
            state = "broke"
        else:
            state = "walking"

# --- ENDINGS ---
print("\n" + "=" * 35)
print(f"FINAL RESULT | Time Left: {time_left} min | Final Energy: {energy}")
print("=" * 35)

if state == "broke":
    print("\n BAD ENDING: COLLAPSED IN THE HALLWAY")
    print("You ran out of physical energy mid-commute. Students find Mr. Cruz fast asleep outside the classroom door as the bell rings.")

elif time_left < 0:
    print("\n BAD ENDING: TARDY & DISGRACED")
    print(f"You arrived {abs(time_left)} minute(s) late. Vice Principal Vance is waiting outside the door tapping his watch.")

elif time_left >= 5 and energy >= 4:
    print("\n GOLDEN ENDING: LEGENDARY PROFESSOR")
    print("You arrived early with time to set up slides and take a sip of coffee. Peak lecture performance delivered effortlessly!")

else:
    print("\n GOOD ENDING: MADE IT ON TIME")
    print(f"You slid into the room with {time_left} minute(s) to spare! Out of breath, but ready to teach.")
