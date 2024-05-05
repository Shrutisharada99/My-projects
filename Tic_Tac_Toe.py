#dictionary data structure
#tic tac toe game
Board{ 'top-L': '', 'top-M': '', 'top-R':'',
 'mid-L': '', 'mid-M': '', 'mid-R':'',
'bot-L': '', 'bot-M': '', 'bot-R':''}
print.pprint(Board) #displays a Tic Tac Toe board
def pBoard(b):
    print(b[top-L]+ '|'+ b[top-M]+ '|'+ b[top-R])
    print('-------')
    print(b[mid-L]+ '|'+ b[mid-M]+ '|'+ b[mid-R])
    print('-------')
    print(b[bot-L]+ '|'+ b[bot-M]+ '|'+ b[bot-R])
#Now the values can be filled in the '' on the Board dictionary 
#Fill values 'X' and 'O'

