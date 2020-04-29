from phrasehunter.game import Game

if __name__ == "__main__":
    print("Welcome to the Phrasehunter Game!")
    g = Game("help",
            "let it be",
            "hey jude", 
            "come together")
    
    g.main_loop()