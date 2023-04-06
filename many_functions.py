str1 = "harry harry"
print(str1.replace("harry","john"))   #replacing any word harry into john.
print(str1.split(" "))  # making list of seq.
print(str1.capitalize()) # capitalize word of seq.first seq.
print(str1.center(50)) # make line in center.
print(str1.count("harry")) #counting of each word of seq.
print(str1.islower()) #check every letter in str is lower case.

str2 = "welcome to the console,,,."
print(str2.find("o"))   #given first word in str in which no of place. but only count first seq of char.


str3 = "Python Is Special."
print(str3.strip(",")) # cut any symbol or word using strip.
print(str3.isalnum())  # use of mix letter 0 to 9 & a - z ,A to Z only one seq TRUE OR FALSE.\
print(str3.isalpha())  # if combination is A - Z,a to z return true else (false).
print(str3.isprintable()) #when every char in str is printable return true else false.
print(str3.isspace()) # when in str using space returns true else false. 
print(str3.istitle()) #seq of every first word in str is capital true or false.
print(str3.startswith("Python")) # when any str or vlo first seq of letter is starts with (python)
print(str3.swapcase()) #it converts lower case into upper and upper case in lower.
print(str3.title())  # convert first letter in "capital" every seq of word in str.
