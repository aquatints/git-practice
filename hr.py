# Determine Target Heart Rate Zone
# Assigned to: Wen

# Comments describe what needs to be done, obviously ;P

# prompt user for age

age = input ("Input age: ")
while age <= 0:
	print "that is not a valid age. Please try again"
	age = input ("Input age: ")

	#something for upper bounds of age? if older than oldest recorded person say "Wow! You sould call the Guiness book of world records"

# calculate max heart rate by doing 206.9 - (0.67 * age)

maxHR = (206.9 - (0.67 * age))

# print max hr 

print ("Maximum heart rate: " + str(maxHR))

'''

# prompt user for resting heart rate, or allow user to enter a ? for 65 as a guess

restHR = raw_input ("Input resting heart rate (if you do not know, enter '?'): ")
if restHR == "?":
	restHR = 65

restHR = int(restHR)

# calculate Heart Rate Reserve (HRR); HRR=MaxHR-RestHR

HRR = (maxHR - restHR)

print ("HRR " + str(HRR))

'''

# calculate lower bound of SPORADIC training zone (74% of maxHR)

LB = (.74 * maxHR)

# calculate upper bound of SPROADIC training zone (84% of maxHR)

UB = (.84 * maxHR)

# print lower and upper bound in the format [Lower, Upper]

print ("[" + str(LB) + ", " + str (UB) + "]")