import random
import pandas as pd
import requests

def make_decisions(options):
  option = input("Please enter the options you have currently: ")
  if option == "DONE" or "done":
    break
  options.append(option)
elif not options: 
    print("no options provided")
else: 
    decision = random.choice(options)
    print(f"\nYour decision: {decision}")

if __name__ == "__main__":
    options = []
    make_decision(options)
