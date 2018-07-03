import csv

if __name__ == '__main__':

    soccerlist = []

    with open('soccer_players.csv', newline='') as csvfile:  # this will open the file and starts the project
        reader = csv.DictReader(csvfile)  # variable that will be used to write the csv info to the new list(soccerlist)
        for row in reader:
            soccerlist.append((row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']))

    new_soccer_list = []  # this will be an ordered replacement of soccerlist
    for item in soccerlist:
        if item[2] == 'YES':
            new_soccer_list.insert(0, item)  # this uses a cool algorithm... adds 'yes' values on the front and 'no' on the end (sorts them)

        else:
            new_soccer_list.append(item)

    Sharks = list(new_soccer_list[::3])  # i think this is a pretty clever way of making the teams =)
    Dragons = list(new_soccer_list[1::3])
    Raptors = list(new_soccer_list[2::3])

    with open('teams.txt', 'w') as team_file:  # file.write(thing+'\n') this will write
        team_file.write("Sharks" + '\n')  # this block will write the info of teams and names to a file named 'teams.txt'
        for item in Sharks:
            team_file.write(', '.join(item) + '\n')
        team_file.write('\n')
        team_file.write("Dragons" + '\n')
        for item in Dragons:
            team_file.write(', '.join(item) + '\n')
        team_file.write('\n')
        team_file.write("Raptors" + '\n')
        for item in Raptors:
            team_file.write(', '.join(item) + '\n')
        # the end is pretty long but gets the job done
