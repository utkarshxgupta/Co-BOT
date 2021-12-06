import aiml
import os

kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile="bot_brain.brn")
else:
    kernel.bootstrap(learnFiles="startup.xml")

 



I = input("user>> ")
while I != "exit()":
    print("bot>> "+kernel.respond(I))
    I = input("user>> ")

 	
kernel.saveBrain("bot_brain.brn")
