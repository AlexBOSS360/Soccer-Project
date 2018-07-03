import csv

if __name__ == '__main__':

    soccerlist = []

    with open('soccer_players.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            soccerlist.append((row['Name'], row['Height (inches)'], row['Soccer Experience'], row['Guardian Name(s)']))

    new_soccer_list = []
    for item in soccerlist:
        if item[2] == 'YES':
            new_soccer_list.insert(0, item)
        else:
            new_soccer_list.append(item)
    count = 1
    for item in new_soccer_list:

        print(count, item, sep='-->')
        print('*')
        count += 1

    Sharks = list(new_soccer_list[::3])
    Dragons = list(new_soccer_list[1::3])
    Raptors = list(new_soccer_list[2::3])

    print('SHARKS')
    for item in Sharks:
        print(item)

    print('DRAGONS')
    for item in Dragons:
        print(item)
    print('RAPTORS')
    for item in Raptors:
        print(item)

    with open('teams.txt', 'w') as team_file:  # file.write(thing+'\n') this will write
        team_file.write("Sharks" + '\n')
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
