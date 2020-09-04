# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:06:20 2020

@author: HP
"""


# importing regex and random libraries
import re
import random

class AlienBot:
  # potential negative responses
  negative_responses = ("no", "nope", "nah", "naw", "not a chance", "sorry")
  # keywords for exiting the conversation
  exit_commands = ("quit", "pause", "exit", "goodbye", "bye", "later")
  # random starter questions
  random_questions = (
        "Why are you here? ",
        "Are there many humans like you? ",
        "What do you consume for sustenance? ",
        "Is there intelligent life on this planet? ",
        "Does Earth have a leader? ",
        "What planets have you visited? ",
        "What technology do you have on this planet? "
    )

  def __init__(self):
    self.alienbabble = {'describe_planet_intent': r'.*your planet*',
                        'answer_why_intent': r'why are*',
                        'cubed_intent': r'Can*cube*3?'
                            }

  # Define .greet() below:
  def greet(self):
    self.name = input("What is your name?\n")
    will_help = input(f"I am {self.name} I'm not from this planet. Will you help me learn about your planet?\n")
    
    if will_help in self.negative_responses:
        print("Ok, Have a nice earth day!")
        return "exit";
       
    self.chat()
        
  # Define .make_exit() here:
  def make_exit(self, reply):
    for exit_command in self.exit_commands:
      if reply in exit_command:  
          print("Ok, have a nice Earth day!”")
          return True
      
    return False
          
  # Define .chat() next:
  def chat(self):
    reply = input("How are you?")  
    while not self.make_exit(reply):
        reply = input(self.match_reply(reply))
        #reply = input(random.choice(self.random_questions)).lower()
    

  # Define .match_reply() below:
  def match_reply(self, reply):
    for key,value in self.alienbabble.items():
       regex_patter = value 
       found_match = re.match(regex_patter,reply)
       intent = key
       if found_match and intent == "describe_planet_intent":
           return self.describe_planet_intent()
       elif found_match and intent == "answer_why_intent":
           return self.answer_why_intent()
       elif found_match and intent =="cubed_intent":
           return self.cubed_intent(reply)
       else:
           return self.no_match_intent()

  # Define .describe_planet_intent():
  def describe_planet_intent(self):
    random_response = ("My planet is a utopia of diverse organisms and species.","I am from Opidipus, the capital of the Wayward Galaxies. ")
    return random.choice(random_response)

  # Define .answer_why_intent():
  def answer_why_intent(self):
    random_response = ("I come in peace.","I am here to collect data on your planet and its inhabitants","I heard the coffee is good.")
    return random.choice(random_response)
       
  # Define .cubed_intent():
  def cubed_intent(self, number):
      number = int(number)
      cube_number = number * number * number
      return f"the cube of number is {cube_number}"

  # Define .no_match_intent():
  def no_match_intent(self):
      random_response = ("Please tell me more. ",
                            "Tell me more! ",
                            "Why do you say that? ",
                            "I see. Can you elaborate? ",
                            "Interesting. Can you tell me more? ",
                            "I see. How do you think? ",
                            "Why? ",
                            "How do you think I feel when you say that? ")
      return random.choice(random_response)

# Create an instance of AlienBot below:

alien = AlienBot()
alien.greet()