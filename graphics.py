from termcolor import colored

def main_menu_graph():
    print("""
 _           _   _   _           _     _           
| |         | | | | | |         | |   (_)          
| |__   __ _| |_| |_| | ___  ___| |__  _ _ __  ___ 
| '_ \ / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
| |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ \\
|_.__/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                        | |        
                                        |_|
     __  ___        _           __  ___                   
    /  |/  /____ _ (_)____     /  |/  /___   ____   __  __
   / /|_/ // __ `// // __ \   / /|_/ // _ \ / __ \ / / / /
  / /  / // /_/ // // / / /  / /  / //  __// / / // /_/ / 
 /_/  /_/ \__,_//_//_/ /_/  /_/  /_/ \___//_/ /_/ \__,_/  
                                                         
    """)
    print(f"Hello, please choose the game mode!")
    print(f"Pressing {colored('quit', 'red')} at any stage will exit the game.")
    print(f"""
    1. Human vs Human 
    2. Human vs AI
    3. AI vs AI
    """)

def who_starts_graph():
    print("""
    Okay! Player vs the AI it is! Who goes first?
                
    1 - I want to go first!
    2 - AI should probably go first...
                """)

def winner_screen_graph():
    print("""
           _                       
          (_)                      
 __      ___ _ __  _ __   ___ _ __ 
 \ \ /\ / / | '_ \| '_ \ / _ \ '__|
  \ V  V /| | | | | | | |  __/ |   
   \_/\_/ |_|_| |_|_| |_|\___|_|   
                                   
                                   
""")

def tie_screen_graph():
    print("""
 .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. |
| |  _________   | || |     _____    | || |  _________   | |
| | |  _   _  |  | || |    |_   _|   | || | |_   ___  |  | |
| | |_/ | | \_|  | || |      | |     | || |   | |_  \_|  | |
| |     | |      | || |      | |     | || |   |  _|  _   | |
| |    _| |_     | || |     _| |_    | || |  _| |___/ |  | |
| |   |_____|    | || |    |_____|   | || | |_________|  | |
| |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------' 
""")