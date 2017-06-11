# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."

# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure
def find_Games(speratedString, name): #procedure to seperate games from the text
    gamesSeparator = ' likes to play '
    games = []
    gName = ''
    
    for sentence in speratedString:
        if gamesSeparator in sentence:
            indexOfGamesSeparator = sentence.find(gamesSeparator)
            gName = sentence[:indexOfGamesSeparator]
            games = sentence[indexOfGamesSeparator + len(gamesSeparator):]
            if gName == name:
                return games

def create_data_structure(string_input): 
    network = {}
    if len(string_input) == 0:
        return network
    else:
        speratedString = string_input.split('.') #seprating sentences
        length = len(speratedString)
        
        #Connections Part#
        connectionsSeparator = ' is connected to '
        connections = []
        cName = ''
        games = []
        for sentence in speratedString:
            if connectionsSeparator in sentence:
                indexOfConnectionsSeparator = sentence.find(connectionsSeparator)
                cName = sentence[:indexOfConnectionsSeparator]
                connections = sentence[indexOfConnectionsSeparator + len(connectionsSeparator):]
                games = find_Games(speratedString, cName)
                network[cName] = [connections.split(', '), games.split(', ')]
               
        return network
# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.
def get_connections(network, user):
    if user in network:
        if len(network[user][0]) == 0: #user has no connections
            return []
        else:
            return network[user][0] #returns user's connections
    return None #user not in the network
# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network, user):
    if user in network:
        if len(network[user][1]) == 0: #user has no games
            return []
        else:
            return network[user][1] #returns user's games
    return None #user not in the network
# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.
def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        if user_B not in network[user_A][0]:
            network[user_A][0].append(user_B)
            return network #add new connection
        else:
            return network #connection already exists
    else:
        return False #one or both users not in network
# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)
def add_new_user(network, user, games):
    if user in network:
        return network
    else:
        network[user] = [[],games] #add user with no connections
        return network
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.
def get_secondary_connections(network, user):
    if user not in network:
        return None
    else:
        if len(network[user][0]) == 0: #user has no primary connections
            return []
        else:
            userConnections = get_connections(network, user)
            secondaryConnection = []
            for e in userConnections:
                for c in get_connections(network, e):
                    if c not in secondaryConnection: #check for duplicates
                        secondaryConnection.append(c)
            return secondaryConnection
# ----------------------------------------------------------------------------- 	
# count_common_connections(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.
def count_common_connections(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return False
    else:
        connectionsA = network[user_A][0]
        connectionsB = network[user_B][0]
        count = 0
        for e1 in connectionsA:
            for e2 in connectionsB:
                if e1 == e2:
                    count = count + 1
    return count
# ----------------------------------------------------------------------------- 
# find_path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print find_path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.
def find_path(network, user_A, user_B, path=[]): #recursive solution seperated
    path = path + [user_A] #as a start will have the value of user A only
    if user_A == user_B: #to stop once the added connection is the same as the second user
        return path 
    for e in network[user_A][0]:
        if e not in path:
            paths = find_path(network, e, user_B, path) #will take each connection of user A and the second user
            if paths:
                return paths

def find_path_to_friend(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return None
    else:
        return find_path(network, user_A, user_B)

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.

# Replace this with your own procedure! You can also uncomment the lines below
# to see how your code behaves. Have fun!

##MYOP no.1: add a new game to an existnig user in the network
def add_new_game(network, user, game):
    if user in network and game not in network[user][1]: #to ensure user is in the network and the game is not duplicate
        network[user][1].append(game)
        return network
    else:
        return 'No changes has been made, reinput new values'
# ----------------------------------------------------------------------------- 
##MYOP no.2: delete a user from the network and from any other user connected to him/her
def delete_user(network, user):
    if user in network:
        for u in network:
            connections = get_connections(network, u)
            if user in connections:
                del connections[connections.index(user)] #delete the user from the connections of other users
        del network[user] #delete the user iteself along with his connections and games
        print "User: " + user + " has been deleted"
    else:
        print "User does't exists"
# ----------------------------------------------------------------------------- 
##MYOP no.3: show statistics on the network
# a. highest connected users
# b. least connected users
def highest_connection(network): #find most connected user
    count = 0
    listOfUsers = []
    
    for e in network:
        if(len(get_connections(network, e))) > count: ##find highest user with connections
            count = len(get_connections(network, e))
    for e in network: ## to cover a case where several users have the same highest conenctions
        if count == (len(get_connections(network, e))):
            listOfUsers.append(e)
    if len(listOfUsers) > 1:
        return "The highest users with connections of " + str(count) + " are: " + str(listOfUsers)
    else:
        return "The highest user with connections of " + str(count) + " is: " + str(listOfUsers)

def least_connection(network): #find least connected user
    user = network.values()[0][0][0] #get the first user in the network
    count = get_connections(network, user)
    listOfUsers = []
    
    for e in network:
        if(len(get_connections(network, e))) < count: ##find least user with connections
            count = len(get_connections(network, e))
    for e in network: ## to cover a case where several users have the same lowest conenctions
        if count == (len(get_connections(network, e))):
            listOfUsers.append(e)
    if len(listOfUsers) > 1:
        return "The least users with connections of " + str(count) + " are: " + str(listOfUsers)
    else:
        return "The least user with connections of " + str(count) + " is: " + str(listOfUsers)

def network_stats(network): #to print the outcome of the highest and least user with connections
    print highest_connection(network)
    print least_connection(network)  
# ----------------------------------------------------------------------------- 
##MYOP no.4: check if two users are first level connected
def check_1st_level_connection(network, user_A, user_B):
    if user_A not in network or user_B not in network:
        return None
    if user_B in network[user_A][0]:
        print 'Users are first level connected'
    else:
        print 'Users are not first level connected'