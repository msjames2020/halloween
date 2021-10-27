class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'  # pink
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BRED = '\033[31m'

def L():
  print("The road is so dark, you can't see the rock\nahead of you and you trip, falling to your knees.")
  print(bcolors.FAIL + bcolors.BOLD + "You yell with excrusiating pain!!! O-U-C-H" + bcolors.ENDC)
def H():
  print("Our story starts on a" + bcolors.OKCYAN + " cool" + bcolors.ENDC + " moonlit night.\nYou find yourself walking along a street alone\nYou can hear children laughing in the distance. ")
  print("You are looking for your friends to " + bcolors.BRED + "Trick-or-Treat" + bcolors.ENDC +"\nwith, but no appears to be around.")
  print("You check your cell phone and see there is no reception...")
  print("As you walk along you begin to feel scared,\nand suddenly a cat jumps from a tree and lands \right in front of you!")
  panic = input("You turn and look to the left and see the road is D A R K!\nTo the right you can't see beyond the rise in the road.\nWhich way do you run??? L = left or R = right. ")
  if panic == "L":
    print(""+ bcolors.WARNING + "Hisssssssss," + bcolors.ENDC + " the cat arches his back and he\'s \nready to pounce as you hurriedly run away.")
    L()

print(bcolors.HEADER + "Welcome to my interactive story." + bcolors.ENDC )
print("\nYou have two choices to read from.\nHalloween, or Christmas? ")
story = input("Which would you like:type in an H for Halloween or C for Christmas. ")

if story == "H":
  print(bcolors.BRED + "I love scary stories!" + bcolors.ENDC)
  H()