# Transaction-manager
A program which stores the users financial transactions which makes it easier to view your true balance across all financial sources.
INSTRUCTIONS
To start off, select "Clear transactions" then type "YES" and put in your starting balance, this 
would be the amount of money you currently have and will be labeled as the root transaction.

Adding transactions is self explanatory, each new transaction will have a day attached which assumes
that the transaction was made on the same day that it was input into the system and uses your computers
clock to extract the date.

Make sure to always exit the program by pressing 7 and selecting "Exit" rather than simply clicking
the close button in the corner as in order to save any modifications you would have to exit through the
program.
---------------------------------------------------------------------------------------------------------------------
Explanation
All of the transactions are structured as a linked list, with the root transaction being the root of the 
linked list and all the other transactions after that being seperate nodes. 
This allows me to simply store the root transaction in the .dat file as that will also automatically store
all the other transactions since the root has a ".next" attribute which points to the next node that also 
has a ".next" attribute which points to the next node and so on and so forth
---------------------------------------------------------------------------------------------------------------------
Aims
I want to allow the user to close the application with the close button and still save any modifications they
have made to the transactions file. I believe this may be possible by overriding the quit method in python but
I have yet to look into it.
I also want to allow the user to edit the date of a transaction which isn't hard to do but don't see it as super 
beneficial so it will most likely be added after everything else.
