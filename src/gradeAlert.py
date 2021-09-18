#!/usr/bin/env python3
""" Program to load and parse csv files."""


#from collections import Counter
import sys, random, csv, os

DATE = "10 Sept 2021"
VERSION = "i"
AUTHOR = "Oliver Bonham-Carter"
AUTHORMAIL = "obonhamcarter@allegheny.edu"
THISPROG = sys.argv[0].replace("./","")
WHATISTHIS_p1 = "\n\tA Grader program: grade csv files are opened,\n\tparsed and files for each row are created.\n\tThen, place these files into GitHub Classroom\n\trepositories to report grades."
WHATISTHIS_p2 = "\t Use option '-h' for more glorification about this amazing project!\n"

MYOUTPUT_DIR = "0_out/" # all results are saved in this local directory


# Bold colour list
colour_list =['\033[1;30m',
'\033[1;31m',
'\033[1;32m',
'\033[1;33m',
'\033[1;34m',
'\033[1;35m',
'\033[1;36m',
'\033[1;37m',
'\033[1;90m',
'\033[1;91m',
'\033[1;92m',
'\033[1;93m',
'\033[1;94m',
'\033[1;95m',
'\033[1;96m']

BIYellow = '\033[1;93m'     # Yellow
BIGreen='\033[1;92m'      # Green
BIBlue='\033[1;94m'       # Blue
BICyan='\033[1;96m'       # Cyan
BIRed='\033[1;91m'        # Red
BIWhite='\033[1;97m'      # White
White='\033[0;37m'        # White



banner1_str = """

       ██████╗ ██████╗  █████╗ ██████╗ ███████╗
      ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔════╝
      ██║  ███╗██████╔╝███████║██║  ██║█████╗
      ██║   ██║██╔══██╗██╔══██║██║  ██║██╔══╝
      ╚██████╔╝██║  ██║██║  ██║██████╔╝███████╗
       ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚══════╝

       █████╗ ██╗     ███████╗██████╗ ████████╗
      ██╔══██╗██║     ██╔════╝██╔══██╗╚══██╔══╝
      ███████║██║     █████╗  ██████╔╝   ██║
      ██╔══██║██║     ██╔══╝  ██╔══██╗   ██║
      ██║  ██║███████╗███████╗██║  ██║   ██║
      ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝   ╚═╝
"""
# banner ref: https://manytools.org/hacker-tools/ascii-banner/



def get_platformType():
	"""Function to dermine the OS type."""
	platforms = {
	'darwin' : 'OSX',
	'win32'  : 'Windows',
	'linux1' : 'Linux',
	'linux2' : 'Linux'}
	if sys.platform not in platforms:
		return sys.platform
	return platforms[sys.platform]
#end of get_platformType()

def printWithColour(colCode_str, myMessage_str):
	"""A function to print with colour for Unix and MacOS."""
	platform_str = get_platformType()
	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		myMessage_str = colCode_str + myMessage_str + BIWhite
		# print(colCode_str + myMessage_str + BIWhite)
	else: # Windows does not seem to like these colourcodes
		# print(myMessage_str)
		pass
	return myMessage_str
# end of printWithColour()


def bannerScreen(myCount_int):
	"""prints a charming and colourful little message for the user"""
	# report the perceived OS type
	platform_str = get_platformType()

	if platform_str.lower() == "linux" or platform_str.lower() == "osx":
		for i in range(myCount_int):
			randomColour_str = random.choice(colour_list) # choose a random colour to display the title screen.
			print(randomColour_str + banner1_str + BIWhite)
	else:
		print(banner1_str)
#end of bannerScreen()




def helper():
	"""Cheap online help; how to use the program"""
	bannerScreen(1) # print up one banner screen
	print(WHATISTHIS_p1)
	h_str1 = "\t"+DATE+" | version: "+VERSION
	h_str2 = "\t"+AUTHOR +"\n\tmail: "+AUTHORMAIL
	print("\t"+len(h_str2) * "-")
	print(printWithColour(BIYellow,h_str1))
	print("\t"+len(h_str2) * "-")
	print(h_str2)
	print("\t"+len(h_str2) * "-")
	print(printWithColour(BIGreen,f"\t [+] \U0001f600 USAGE: {THISPROG}  myGrades.csv"))

#end of helper()



def getArguments(argv_list):
	""" A function to determine what parameters have been entered"""

	# print(argv_list)

	param_1 = "CSV" # call for cvsReader()
	param_2 = "-H" # call for helper()

	if len(argv_list) == 0:
			# Output welcome message
			# print(printWithColour(BICyan,WHATISTHIS_p1))
			print(printWithColour(BICyan,WHATISTHIS_p2))

	helperFlag_Bool = False
	csvFile_str = None # file to open
	for i in argv_list:
		# print(BIRed + f"Checking <<{i}>>" + White)
		if param_1 in i.upper():
			print(i)
			csvFile_str = i
			# print(f"\t CSV file found: {myfile_str}")
		if param_2 == i.upper():
			# print(f"\t Call to help found: {i}")
			helperFlag_Bool = True
			helper()
			exit()

		if param_1 not in i.upper() and param_2 not in i.upper():
			print(printWithColour(BICyan,WHATISTHIS_p2))


		if csvFile_str != None:
			begin(csvFile_str)
			# end of getArguments()




def cvsReader(csvFile_str):
	"""Function to open csv file and parse contents"""
	tmp_str = "" # used hold a string of the cvs row
	topRow_Bol = False

	with open(csvFile_str) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')

		for row_list in csv_reader: # row as a list
			if topRow_Bol == False: # get col names
				topRow_list = row_list
				topRow_Bol = True
			else:
				tmp_str = "" #string of row data
				for pos in range(len(row_list)):
					# print(f"{pos}::{row_list[pos]}")
					tmp_str = tmp_str + f"{topRow_list[pos]} : {row_list[pos]}\n\n"

				tmp_str = tmp_str + "\n____\n\n"
				print(printWithColour(BICyan,f"\t [+] Processing : {row_list[0]}")) # the student name from current row
				saveFile(row_list[0], tmp_str) # student name, data

		exit()
		#end of cvsReader()


def saveFile(fname, in_str):
	"""Save the string as a text file. Data is in_str variable."""

	if len(in_str) > 0:
			tmp_str = ""

			try:
				tmp_dir = checkDataDir(MYOUTPUT_DIR)
				fname = fname.replace(",","").replace(" ","").replace(".","") # remove commas and spaces in filename
				filename = MYOUTPUT_DIR + fname+"_gradebook.md"
				f = open(filename, "w")
				f.write(in_str)
				f.close()
				print(printWithColour(BIGreen, f"\t [+] Saving <{filename}>\n" + White))

			except IOError:
				printErrorByPlatform(BRed + f"\t Problem saving file... incorrect permissions?!" + White)
	# end of saveFile()


def checkDataDir(dir_str):
#function to determine whether a data output directory exists.
#if the directory doesnt exist, then it is created

	try:
		os.makedirs(dir_str)
		#if MYOUTPUT_DIR doesn't exist, create directory
		#printByPlatform("\t Creating :{}".format(dir_str))
		return 1

	except OSError:
		#printErrorByPlatform("\t Error creating directory or directory already present ... ")
		return 0
#end of checkDataDir()




def begin(csvFile_str):
	"""Driver function"""
	print(printWithColour(BIYellow,f"\t [+] File to open: {csvFile_str}\n"))
	cvsReader(csvFile_str)
#end of begin()



if __name__ == '__main__':
	getArguments(sys.argv[1:])
