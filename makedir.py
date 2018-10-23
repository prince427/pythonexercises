import os

dirName = "tempDIr"
dirName2 = "tempDir2"
dirName3 = "te


try:
	os.mkdir(dirName)
	print("Directory" , dirName , "Created")
except FileExistsError:
	print("Directory", dirName , "already exists")

try:
	os.mkdir(dirName2)
	print("Directory" , dirName2 , "Created")
except FileExistsError:
	print("Directory", dirName2 , "already exists")



