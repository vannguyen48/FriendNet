# Van Nguyen and Brandon Kelly

'''
DELIVERABLE 2 INSTRUCTIONS:
    For this part of the project, we learned how to implement Dijkstra's Algorithm
    via: http://math.mit.edu/~rothvoss/18.304.3PM/Presentations/1-Melissa.pdf
    We followed the pseudo code (though it is basically a step by step on how the algorithm
    should run) and implemented from there.

    The best friend chain can be tested by selecting option number #3 when the menu
    prompts the user to do so. At that point, you simply enter two names who are inside
    of the graph (text.txt). At this time, since Dr. Schroeder told us that we do not need
    error handling, if you enter two names that are not inside of the graph then the 
    program will crash. Make sure that you capitalize the first letter of each name entered
    (or have it match with however it is in the .txt) or else an error will occur. Once entered,
    the shortest path gets displayed with each "node" visited (in this case the names it
    traveled through get displayed). It also calculates the cost to go through that path.
    Even though it was not a requirement (though suggested), we did not have time to begin
    implementing our "killer features" for this deliverable date. However, implementing
    Dijkstra_Algorithm's algorithm will be a huge help in implementing our killer features in the 
    coming week.

DELIVERABLE 1 QUESTIONS:
Best friend chain - what's the name of all users on the friendliest chain of people to get from user A to user B,
or an indication that there's no path:
    The algorithm we are using for this is Dijkstra_Algorithm's algorithm. This is an algorithm to find the shortest path between
    two nodes in a graph. This algorithm is what will help us implement the "Best friend chain". The goal of the chain
    is to minimize the amount of animosity we will take (10 - Friend Rating since the friend values are in numerical scale
    ) and add up the resulting values to find the lowest. This will leave us with the friendliest chain.
    We can come up with an animosity graph in order to help us figure out the best friend chain. In other words, A and B 
    with relationship 6 will have animosity level of 4. We can perform the same calculation for all relationships in
    the net work and attempt to find the shortest path using Dijkstra's algorithm. 

Two Killer Features:
    Our first killer feature is one that will let the user see who is the most liked throughout all FriendNet (or
    in coding terms, throughout the entire graph). We use the friendship ratings that we grab from the .txt file
    and sum up the total values from the outgoing paths and compare the values to each other to determine who has the
    highest net rating. That person is then deemed the friendliest in friendNET. This killer features runs through
    the entire graph as it must check each node (person).
    Our second killer feature is the ability to see who is likely to unfriend who. To implement this, we would look at
    all the direct paths coming out of each node. We would be able to list out all the node's (individual's) best
    friends, acquaintances, and worst friends. This would work somewhat like the "close-friend" tag on Facebook to
    categorize individuals. If the ranking is 7 or above it is a best friend, 3 to 6 is an acquaintance, and 1 to 2 is
    a bad friend (likely to unfriend). This would only look at what one individual thinks of another, not the other way 
    around. It will simply output these titles when the user requests this feature to be ran. This is the killer feature
    does not run over the entire graph.
'''


# Main function that brings all the options together to construct a user interface
def main():
    choice = 0
    print("Welcome to FriendNet!")
    textfile = raw_input("What is the name of your file? ")  # Accepts user input for the .txt file name
    while (choice != '6'):
        print("What do you want to do? ")  # Accepts user input for choice option
        print("1) Check if user exists ")
        print("2) Check connection between users ")
        print("3) Best Friend Chain ")
        print("4) Who is the most friendly in FriendNet? ")
        print("5) Who is likely to unfriend who? ")
        print("6) Quit ")
        choice = raw_input()
        if choice == '1':
            exists(textfile)  # Checks if a user exists
        elif choice == '2':
            connection(textfile)  # Checks if there is a connection between users
        elif choice == '3':
            bestfriendchain(textfile, choice)
        elif choice == '4':
            bestfriendchain(textfile, choice)
        elif choice == '5':
            unfriend(textfile)
    if (choice == '6'):
        quit()  # Quits the program


# Checks if a user exists
def exists(textfile):
    found = 0
    print("What user? ")
    user = raw_input()  # Takes user input for which user to search if they exist
    with open(textfile) as openfile:
        for line in openfile:
            for part in line.split():  # Loops through the .txt file to check if a user exists, if they do return 1
                if user in part:
                    found = 1
    if (found == 1):  # If-else stating if the user exists or not
        print (user + " exists")
    else:
        print(user + " does not exist")


# This function is called when the user wants to check the connection between two users
def connection(textfile):
    found = 0
    users = []
    print("What users (separated by spaces)? ")
    users = raw_input()  # Accepts user input for individual's names
    usera, userb = users.split()
    parse(textfile, usera, userb)


# Allows the user to quit the program if they select option 6
def quit():
    return 0


# This is the primary parsing function that will allow the program to split up person A, person B and their
# friendship value so that other functionality (such as checking friendship chains) are able to properly work.
# It will go line by line through the text document, and split the names and values based on whitespace and dashes.
# .strip() is used so that no '\n' appear in the output when parsing.
def parse(textfile, userA, userB):
    A = []  # List 1 for the first person
    B = []  # List 2 for the second person
    level = []
    found = 0
    index = 0
    with open(textfile, 'r') as f:
        for l in f:
            spl = l.strip().split(' ')
            if len(spl) == 3:
                a, b, d = spl
                A.append(a)
                B.append(b)
                level.append(d)
    f.close

    for x in range(0, len(A)):
        if (userA == A[x]):
            if (userB == B[x]):
                found = 1
                index = x

    if (found == 1):
        print(userA + " and " + userB + " exist with relationship " + level[index])
    else:
        print(userA + " and " + userB + " are not connections")


# Parses the .txt file given and separates each name and friendship value into three
# different lists. These are then placed inside of a dictionary so that we can properly
# traverse the graph.
def bestfriendchain(textfile, choice):
    A = []
    B = []
    level = []
    Dict = {}
    bflevel = []  # Best-friend level

    with open(textfile, 'r') as f:
        for l in f:
            spl = l.strip().split(' ')
            if len(spl) == 3:
                a, b, d = spl
                A.append(a)
                B.append(b)
                level.append(d)
    f.close
    for x in range(0, len(level)):
        bflevel.append(10 - int(level[x]))
    Dict = {}
    for i in range(len(A)):
        Dict[A[i]] = {}
    for i in range(len(A)):
        Dict[A[i]][B[i]] = bflevel[i]
    if (choice == '3'):
        print("What users (separated by spaces, note order matters)? ")  # because this is a directed graph
        users = raw_input()  # Accepts user input for individual's names
        usera, userb = users.split()
        Dijkstra_Algorithm(Dict, usera, userb)
    elif (choice == '4'):
        favoritefriend(Dict, A, B, level, bflevel)


def Dijkstra_Algorithm(connections, source, destination, path_value={}, previous={}, visited_node=[]):
    not_visited = {}
    route = []

    if source != destination:
        if not visited_node:
            path_value[source] = 0
        for neighbor in connections[source]:
            if neighbor not in visited_node:
                updated_distance = path_value[source] + connections[source][neighbor]
                if updated_distance < path_value.get(neighbor, float('inf')):
                    previous[neighbor] = source
                    path_value[neighbor] = updated_distance
        visited_node.append(source)  # Sets the node's status as "visited"
        # Lowest cost calculation
        for n in connections:
            if n not in visited_node:
                not_visited[n] = path_value.get(n, float('inf'))
        node = min(not_visited, key=not_visited.get)
        Dijkstra_Algorithm(connections, node, destination, path_value, previous, visited_node)

    else:
        p = destination
        while p != None:
            route.append(p)
            p = previous.get(p, None)
        print('Best-friend chain is: ' + str(route))
        print ('Total cost : ' + str(path_value[destination]))

# Traverses the entire graph and determines who is the most friendly in FriendNET
def favoritefriend(Dict, A, B, level, bflevel):
    topfriend = {}
    currenttopfriend = 0
    for i in range(len(A)):
        topfriend[A[i]] = 0
    for i in range(len(A)):
        topfriend[A[i]] += (10 - int(Dict[A[i]][B[i]])) # Keeps track of the top friend based on levels
    print(topfriend)
    for i in range(len(A)):  # Grabs the person's name and prints it and updates current as needed
        if (topfriend[A[i]] > currenttopfriend):
            currenttopfriend = topfriend[A[i]]
            friendname = A[i]
    print (friendname + " is the most friendly in FriendNet")

# Checks if a user is likely unfriend another based upon their associated friendship value
def unfriend(textfile):
    A = []  # Dictionary and variable initialization
    B = []
    level = []
    unfriend = 0

    # Parses the provided .txt file
    with open(textfile, 'r') as f:
        for l in f:
            spl = l.strip().split(' ')
            if len(spl) == 3:
                a, b, d = spl
                A.append(a)
                B.append(b)
                level.append(d)
    f.close
    print("Which user? ")
    user = raw_input()  # Accepts user input for individual's names
    for x in range(0, len(A)):
        if user == A[x] and int(level[x]) < 3:   # If the user's friend level is lower than 3 then "unfriend"
            print(user + " is likely to unfriend " + B[x])
        elif user == A[x] and int(level[x]) >= 7:   # If a user's friend level is >= 7 then "best friends"
            print(user + " and " + B[x] + " are best friends")
            unfriend = 1
        elif user == A[x] and int(level[x]) >= 3:   # If a user's friend level is between 3 and 6 then "acquaintances"
            print(user + " and " + B[x] + " are acquaintances")
            unfriend = 1
    if unfriend != 1:    # Checks if unfriend is == 1 which is only the case if a friend level is < 3.
        print(user + " is not likely to unfriend anybody")


main()
