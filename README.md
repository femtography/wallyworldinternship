# Movie Theater Seating Challenge - Walmart

## Assumptions:

Groups would be larger than 0.
Groups can not be more than 4 people.
Groups must have three seats between them and the next party within their row.
Groups can not have another group directly in front or behind them.
After all 25 possible reservation zones are taken, the program will stop processing requests and will proceed to finish remaining aspects of script.
Input file will be in .txt format.

## Instructions:

This script will work via the command line and was written in Python.
You will need to provide the complete path of the input file (test file) as well as where you would like the output file to be located.

  ### Example:
  
      python script.py PC/your/complete/path/test.txt  PC/lets/send/it/to/this/folder/
  
Since the assignment asks for complete path to be returned and not printed, you will have to check the location specified to verify accuracy of script.
Open up the output .txt file and verify that the results are provided as described in the instructions.

## Process:

I started by creating the I/O features of the script, ensuring that I could extract, process, and return the data as was being requested.
Created reservation feature by breaking it up into two functions, one that assigned tickets to a reservation request and another to handle the overall process of managing all inputs.
Used main() to pull all features together in the manner requested in the assignment. 

## Trade Offs:

Given the short time frame for completing, I simplified the reservation process into 25 zones of 4 seats. 
This limited the overall max capacity to 50% in the event that all reservations were for 4 people. Huge tradeoff for profits.
Reservations start from front to back of theater, for simplicity. 

## Improvements:

Create more dynamic function to assign seats to parties. 
  This would allow for minimum of three spaces of distance between groups to be achieved, allowing for 25% more seats to become available.
  Increases efficiency when smaller parties take up a zone that can fit 4 people.
  This allows for tickets to be assigned to best possible row based on consecutive seats available in said row.
