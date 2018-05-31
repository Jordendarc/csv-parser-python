# csv-parser-python

This program recieves a csv file have rows that look like this [""string""]"" if there is only one element.  If there are more, then it would look like this [""string1""string2""string3""]"".  When read, there are commas between the column information.  This program will look to see if there are multiple strings in a row, partition the row, removes the characters "[],.  The program then will put each value into an array with another array keeping track of how many times that string appears in the file.  The program then writes the strings that appeared more than once to a csv file, where one column is the strings and the second column is filled with the amount of times the string appears in the first file.  


