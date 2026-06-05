def rule_based_chatbot():
    # 1. KNOWLEDGE BASE: Dictionary with 5+ intents (O(1) Constant Time Lookup)
    intents = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! Great to connect with you.",
        "how are you": "I'm functioning perfectly at maximum algorithmic efficiency! How about you?",
        "project details": "This is Project 1: A deterministic, white-box rule-based AI chatbot.",
        "architecture": "I am built using an IPO (Input-Process-Output) model with a dictionary skeleton.",
        "help": "You can greet me, ask about 'project details', 'architecture', or type 'exit' to leave.",
        "bye": "Goodbye! Have a great day ahead."
    }
    
    print("====================================================")
    print("  PROJECT 1: DETERMINISTIC RULE-BASED CHATBOT ACTIVE ")
    print("====================================================")
    print("Type 'exit' to terminate the program.\n")
    
    # 2. THE HEARTBEAT: Infinite Loop 
    while True:
        # Raw Data Inflow
        raw_input = input("You: ")
        
        # 3. PHASE 1: Sanitization (Handles cases and whitespace)
        clean_input = raw_input.lower().strip()
        
        # 4. EXIT STRATEGY: Clean Break Command
        if clean_input == 'exit':
            print("Chatbot: Terminating session. System shutting down cleanly. Goodbye!")
            break
            
        # 5. IMPLEMENTATION: The .get() Method (Atomic lookup + fallback)
        reply = intents.get(clean_input, "I do not understand. Type 'help' for available commands.")
        
        # Output Phase
        print(f"Chatbot: {reply}\n")

if __name__ == "__main__":
    rule_based_chatbot()