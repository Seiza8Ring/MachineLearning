#Code- Lillian    Flowchart- Connor


def failsafe(ans):
    if ans == 'console' or ans == 'mobile':
        print(f"{ans} is not available right now.")
        
    else: print(f"{ans} is not a listed option.")
    


print("Caution: should a syntax error ocurr, you will need to restart.")

ans = input("What is your Gaming Platform? (pc/console/mobile) ").lower()

if ans == 'pc':
    #PC
    ans = input("Single-player or Multiplayer?(single/multi) ").lower()

    if ans == 'single':
        #Single-player
        ans = input("Preferred genre? (soul-like/horror/turn-based/openworld) ").lower()
        if ans == 'soul-like':
            #soul-like
            ans = input("Time Commitment? (casual/regular/hardcore) ").lower()
            if ans == 'casual':
                #Casual games   pc, single-player, soul-like, casual
                print("""
--- Games That Fit ---
Star Wars Jedi: Fallen Order
Another Crab's Treasure
Dark Souls III
""")
            elif ans == 'regular':
                #Regular Games  pc, single-player, soul-like, regular
                print("""
--- Games That Fit ---
Lies of P
Sekiro: Shadows Die Twice
Steelrising
""")
            elif ans == 'hardcore':
                #Hardcore Games pc, single-player, soul-like, hardcore
                print("""
--- Games That Fit ---
Elden Ring
Sekiro: Shadows Die Twice
Nioh 2 – The Complete Edition
""")
            else: failsafe(ans)

        elif ans == 'horror':
            #horror
            ans = input("Time Commitment? (casual/regular/hardcore) ").lower()
            if ans == 'casual':
                #Casual games   pc, single-player, horror, casual
                print("""
--- Games That Fit ---
Little Nightmares
Fears to Fathom
The Mortuary Assistant
MiSide
""")
            elif ans == 'regular':
                #Regular Games  pc, single-player, horror, regular
                print("""
--- Games That Fit ---
Resident Evil 7: Biohazard
Alien: Isolation
SOMA
""")
            elif ans == 'hardcore':
                #Hardcore Games pc, single-player, horror, hardcore
                print("""
--- Games That Fit ---
Alien: Isolation
Alan Wake 2
The Forest
""")
            else: failsafe(ans)

        elif ans == 'turn-based':
            #Turn-Based
            ans = input("Time Commitment? (casual/regular/hardcore) ").lower()
            if ans == 'casual':
                #Casual games   pc, single-player, turnbased, casual
                print("""
--- Games That Fit ---
Slay the Spire
Into the Breach
Child of Light
""")
            elif ans == 'regular':
                #Regular Games  pc, single-player, turnbased, regular
                print("""
--- Games That Fit ---
XCOM 2
Yakuza: Like a Dragon
Divinity: Original Sin 2
""")
            elif ans == 'hardcore':
                #Hardcore Games pc, single-player, turnbased, hardcore
                print("""
--- Games That Fit ---
Pathfinder: Wrath of the Righteous
XCOM 2 (with War of the Chosen DLC)
Battle Brothers
""")
            else: failsafe(ans)
        elif ans == 'openworld':
            #openworld
            ans = input("Time Commitment? (casual/regular/hardcore) ").lower()
            if ans == 'casual':
                #Casual games   pc, single-player, openworld, casual
                print("""
--- Games That Fit ---
Stray
Slime Rancher
Firewatch
""")
            elif ans == 'regular':
                #Regular Games  pc, single-player, openworld, regular
                print("""
--- Games That Fit ---
Horizon Zero Dawn Complete Edition
Cyberpunk 2077
Marvel's Spider-Man Remastered
""")
            elif ans == 'hardcore':
                #Hardcore Games pc, single-player, openworld, hardcore
                print("""
--- Games That Fit ---
The Elder Scrolls V: Skyrim (Special or Anniversary Edition)
Kenshi
Elden Ring
""")
            else: failsafe(ans)
        else: failsafe(ans)

    elif ans == 'multi':
        #multiplayer
        ans = input("Preferred genre? (soul-like/horror/turn-based/openworld) ").lower()
        if ans == 'soul-like':
            #soul-like
            ans = input("Time Commitment? (casual/regular/hardcore) ").lower()
            if ans == 'casual':
                #Casual games   pc, multiplayer, soul-like, casual
                print("""
--- Games That Fit ---
Remnant II (or Remnant: From the Ashes)
Stranger of Paradise: Final Fantasy Origin
Code Vein
""")
            elif ans == 'regular':
                #Regular Games  pc, multiplayer, soul-like, regular
                print("""
--- Games That Fit ---
Remnant II
Code Vein
Lords of the Fallen (2023)
""")
            elif ans == 'hardcore':
                #Hardcore Games pc, multiplayer, soul-like, hardcore
                print("""
--- Games That Fit ---
Elden Ring
Remnant 2
Nioh 2 – The Complete Edition
""")
            else: failsafe(ans)

        elif ans == 'horror':
            #horror
            ans = input("Time Commitment? (casual/regular/hardcore) ").lower()
            if ans == 'casual':
                #Casual games   pc, multiplayer, horror, casual
                print("""
--- Games That Fit ---
Lethal Company
Phasmophobia
Dead by Daylight
""")
            elif ans == 'regular':
                #Regular Games  pc, multiplayer, horror, regular
                print("""
--- Games That Fit ---
Dead by Daylight
Phasmophobia
The Outlast Trials
""")
            elif ans == 'hardcore':
                #Hardcore Games pc, multiplayer, horror, hardcore
                print("""
--- Games That Fit ---
GTFO
Project Zomboid
Hunt: Showdown 1896
""")
            else: failsafe(ans)

        elif ans == 'turn-based':
            #Turn-Based
            ans = input("Time Commitment? (casual/regular/hardcore) ").lower()
            if ans == 'casual':
                #Casual games   pc, multiplayer, turnbased, casual
                print("""
--- Games That Fit ---
Worms W.M.D
The Battle of Polytopia
Marvel Snap
""")
            elif ans == 'regular':
                #Regular Games  pc, multiplayer, turnbased, regular
                print("""
--- Games That Fit ---
Wildermyth
For The King
Armello
""")
            elif ans == 'hardcore':
                #Hardcore Games pc, multiplayer, turnbased, hardcore
                print("""
--- Games That Fit ---
Sid Meier’s Civilization VI
Baldur's Gate 3
Dominions 6: Rise of the Pantokrator
""")
            else: failsafe(ans)

        elif ans == 'openworld':
            #openworld
            ans = input("Time Commitment? (casual/regular/hardcore) ").lower()
            if ans == 'casual':
                #Casual games   pc, multiplayer, openworld, casual
                print("""
--- Games That Fit ---
Sea of Thieves
Minecraft
No Man's Sky
""")
            elif ans == 'regular':
                #Regular Games  pc, multiplayer, openworld, regular
                print("""
--- Games That Fit ---
Valheim
Sea of Thieves
No Man's Sky
""")
            elif ans == 'hardcore':
                #Hardcore Games pc, multiplayer, openworld, hardcore
                print("""
--- Games That Fit ---
EVE Online
Rust
DayZ
""")
            #else: failsafe(ans)
       
    else: failsafe(ans)

elif ans == 'console':
    #Console
    failsafe(ans)

elif ans == 'mobile':
    #Mobile
    failsafe(ans)

else: 
    failsafe(ans)