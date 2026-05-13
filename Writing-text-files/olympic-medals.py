import re

with open('olympic-medals.csv', 'r') as fileobj:
    content=fileobj.read()

with open('olympic-medals-copy.csv', 'w') as fileobj:
    fileobj.write(content)

countries_overview = content.split("\n")
to_write = []
for country_score in countries_overview:
    if len(country_score) > 0:
        if country_score[0] == 'N':
            to_write.append(country_score+"\n")
            print(country_score)

with open('olympic-medals-n.csv', 'w') as fileobj:
    fileobj.writelines(to_write)

countries_overview = content.split("\n")
to_write_5_medals = []
count_lines=0
for country_score in countries_overview:
    if count_lines == 0: # This is the line with the header
        to_write_5_medals.append(country_score + "\n")
        count_lines += 1
    else:
        if len(country_score) > 0:
            if len(country_score.split(',')) == 4: # Normal situation of TEAM, gold, silver, bronze
                team,gold_medals,silver_medals,bronze_medals = country_score.split(',')
                print(team, gold_medals, silver_medals, bronze_medals)

            elif len(country_score.split(',')) > 4: # Special situation of TEAM, gold, silver, bronze.
                                                    # where TEAM contains a "," within quotes. E.g.
                                                    # "Hong Kong, China"
                # split the line into a list of 3 parts:
                # left:  ''
                # middle 'Hong Kong, China'
                # right ',1,2,3'
                split_line = re.split(r"\"*,*\"",country_score)

                print(split_line)
                team = split_line[1]
                print(team)
                empty, gold_medals, silver_medals, bronze_medals = split_line[2].split(",")
                print("SPECIAL: ",team, gold_medals, silver_medals, bronze_medals)

            else: # typically an empty line
                gold_medals=0
                to_write=""
            if int(gold_medals) >= 5:
                to_write_5_medals.append(country_score+"\n")
print (to_write_5_medals)

with open('olympic-medals-5.csv', 'w') as fileobj:
    fileobj.writelines(to_write_5_medals)


