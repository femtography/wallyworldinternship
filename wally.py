
import sys
from datetime import datetime

# Function that creates a new file at a specified location and returns the location upon producing a psuedorandom name.
def createFile(base):
    now = datetime.now();
    timestamp = round(datetime.timestamp(now));

    newFileLocation = base + 'FileOut' + str(timestamp);

    newFile = open(newFileLocation,"w");
    newFile.close();

    return newFileLocation;

# Method that writes all lines given in list format.
def writeToFile(fileToWriteTo, lines):
    daFile = open(fileToWriteTo,"w");
    daFile.writelines(lines);
    daFile.close();

# Function that assigns ticket numbers for 10 x 20 theater that uses letters to signify rows and that cannot sit groups directly next to or in front/behind another group.
# This function returns the reservation number along with the tickets that were assigned to said reservation in the form of a string.
def ticketAssignment(row, col, quantity):
    rows = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"];
    cols = [1, 9, 17];
    colsEven = [5, 13];
    tickets = "";

    # Logic that ensures that no groups are next to eachother in a row or that there is not another group in the row directly in front/behind them.
    for req in range(quantity):
        if req == 0:
            if row == 0 or row % 2 == 0:
                ticketNum = str(req + colsEven[col]);
                tickets = tickets + rows[row] + ticketNum;
            else:
                ticketNum = str(req + cols[col]);
                tickets = tickets + rows[row] + ticketNum;
        else:
            if row == 0 or row % 2 == 0:
                ticketNum = str(req + colsEven[col]);
                tickets = tickets + "," + rows[row] + ticketNum;
            else:
                ticketNum = str(req + cols[col]);
                tickets = tickets + "," + rows[row] + ticketNum;

    return tickets  + "\n"

# Function that takes in all reservations and utilizes the ticketAssignment() function to complete. This function returns a list of all the reservations and their assigned tickets.
# Edge cases and breaking assumptions will skip that reservation and continue to next reservation until at maximum capacity based on Health/Safety Standards.
def processReservations(lines):
    reservations = [];
    row = 0;
    col = 0;

    for line in lines:
        parts = line.split(" ")
        resNum = parts[0];
        quantity = int(parts[1]);

        if row > 9:
            print("Reservation: " + resNum);
            print("This theater is at capacity based on Health/Safety Standards.");
            print("Please seek alternate theater rooms for reservations. We apologize for the inconvenience!");
            print(" ");
            return reservations;

        if quantity > 4:
            print("Reservation: " + resNum);
            print("Due to Health/Safety Standards, we can only accomodate groups of no more than 4 people.");
            print("Please request a reservation of 4 people or less.");
            print(" ");
            print("If you have a group of more than four, please make multiple reservations of 4 or less people.");
            print("Thank you for understanding. We apologize for the inconvenience!");
            print(" ");
            continue

        if quantity < 1:
            print("Reservation: " + resNum);
            print("Unfortunately, at this moment we are not able to accomodate ghosts.");
            print("Please check back in at a later date to see if our policy has changed or feel free to make a reservation with a quantity of 1 or more.");
            print(" ");
            continue

        temp = ticketAssignment(row, col, quantity);

        reservations.append(resNum + " " + temp)

        col += 1;

        if row == 0 or row % 2 == 0:
            if col > 1:
                col = 0;
                row += 1;
        else:
            if col > 2:
                col = 0;
                row += 1;

    return reservations

# Main function that takes in arguements from command line and returns the full location of the output file. Does not print location, it returns it, per assignment.
def main(argv):

    fileIn = open(str(argv[1]), 'r');
    fileOut = createFile(str(argv[2]));
    lines = fileIn.readlines();
    tickets = processReservations(lines);

    writeToFile(fileOut, tickets);
    return fileOut;


if __name__ == "__main__":
   main(sys.argv)
