"""
TUPLES
-------------------
employee_1 = ('Joe', 'Bob', 'Service Tech', 'Hourly', 25, 'Seasonal')
employee_2 = ('John', 'Guy', 'Engineer', 'Salary', 38, 'Full Time')
employee_3 = ('Sarah', 'Lee', 'Data Analyst', 'Salary', 35, 'Full Time')

ee1_name = ('Joe', 'Bob')
ee3_postion = ('Data Analyst', 'Salary', 35, 'Full Time')
Created new employee 4 tuple: ('Joe', 'Bob', 'Data Analyst', 'Salary', 35, 'Full Time')

Employee 1 is a full time employee: False
Employee 2 is a full time employee: True
Employee 3 is a full time employee: True
Employee 4 is a full time employee: True

Joe's employee profile details:
      first_name = 'Joe'
      last_name = 'Bob'
      postion = 'Service Tech'
      pay_format = 'Hourly'
      pay_rate = 25
      work_status = 'Seasonal'


SETS
-------------------
location1_set = {'Sarah', 'Frank', 'Heather', 'Joe', 'Alex'}
location2_set = {'Bob', 'Frank', 'Heather', 'Alex', 'Anna'}

location_union = {'Sarah', 'Frank', 'Heather', 'Joe', 'Anna', 'Bob', 'Alex'}
location_intersection = {'Heather', 'Alex', 'Frank'}


DICTIONARIES
-------------------
Name count in text_names_in file:

{'Michael': 1, 'Jackson': 2, 'Prince': 2, 'Madonna': 1, 'U2': 1, 'Bruce': 2, 'Springsteen': 1, 'Run-D.M.C.': 1, 'Van': 1, 'Halen': 1, 'Public': 1, 'Enemy': 1, 'Billy': 4, 'Joel': 1, 'The': 19, 'Police': 1, 'Phil': 1, 'Collins': 1, 'Guns': 1, "N'": 1, 'Roses': 2, 'Def': 1, 'Leppard': 1, 'Janet': 1, 'George': 2, 'Michael/Wham': 1, 'Whitney': 1, 'Houston': 1, 'Metallica': 1, 'N.W.A': 1, 'Dire': 1, 'Straits': 1, 'AC/DC': 1, 'Rush': 1, 'Iron': 1, 'Maiden': 1, 'Judas': 1, 'Priest': 1, 'Lionel': 1, 'Richie': 1, 'Bon': 1, 'Jovi': 1, 'Talking': 1, 'Heads': 1, 'Genesis': 1, 'R.E.M.': 1, 'Duran': 2, 'Motley': 1, 'Crue': 1, 'Cure': 1, 'Journey': 1, 'John': 4, 'Mellencamp': 1, 'Grandmaster': 1, 'Flash': 1, '&': 9, 'Furious': 1, 'Five': 1, 'REO': 1, 'Speedwagon': 1, 'Kool': 2, 'and': 3, 'the': 6, 'Gang': 1, 'L.L.': 1, 'Cool': 1, 'J': 1, 'Tina': 1, 'Turner': 1, 'Queen': 1, 'Beastie': 1, 'Boys': 2, 'Ozzy': 1, 'Osbourne': 1, 'Smiths': 1, 'Huey': 1, 'Lewis': 1, 'News': 1, 'Bryan': 1, 'Adams': 1, 'Hall': 1, 'Oates': 1, 'Pat': 1, 'Benatar': 1, 'Eric': 2, 'B.': 1, 'Rakim': 1, 'Idol': 1, 'Peter': 1, 'Gabriel': 1, 'INXS': 1, 'Tom': 2, 'Petty': 1, 'Heartbreakers': 1, 'Stevie': 3, 'Ray': 1, 'Vaughan': 1, 'Double': 1, 'Trouble': 1, 'Eurythmics': 1, 'Cars': 1, 'Aerosmith': 1, 'ZZ': 1, 'Top': 1, 'Rolling': 1, 'Stones': 1, 'Heart': 1, 'David': 2, 'Bowie': 1, 'Elton': 1, 'Rod': 1, 'Stewart': 1, 'Foreigner': 1, 'Wonder': 1, 'Toto': 1, 'Bob': 1, 'Seger': 1, 'Pointer': 1, 'Sisters': 1, 'DJ': 1, 'Jazzy': 1, 'Jeff': 1, 'Fresh': 2, 'Salt-N-Pepa': 1, 'Fleetwood': 1, 'Mac': 1, "Go-Go's": 1, 'Paul': 3, 'McCartney': 1, 'Pet': 1, 'Shop': 1, 'Don': 1, 'Henley': 1, 'Simon': 1, 'Tracy': 1, 'Chapman': 1, 'Cyndi': 1, 'Lauper': 1, 'Depeche': 1, 'Mode': 1, 'Sonic': 1, 'Youth': 1, 'Pete': 1, 'Townshend': 1, 'Culture': 1, 'Club': 1, 'Gloria': 1, 'Estefan': 1, 'Miami': 1, 'Sound': 1, 'Machine': 1, 'De': 2, 'La': 1, 'Soul': 1, 'Luther': 1, 'Vandross': 1, 'Chicago': 1, 'Bangles': 1, 'Thompson': 1, 'Twins': 1, 'Yes': 1, 'Men': 1, 'at': 1, 'Work': 1, 'Pixies': 1, 'Pink': 1, 'Floyd': 1, 'Robert': 1, 'Palmer': 1, 'Kenny': 1, 'Loggins': 1, 'Whitesnake': 1, 'Sade': 1, 'Steve': 1, 'Winwood': 1, 'Ocean': 1, 'Tears': 1, 'for': 1, 'Fears': 1, 'Bobby': 1, 'Brown': 1, 'Scorpions': 1, 'Simply': 1, 'Red': 2, "B-52's": 1, 'Boston': 1, 'Rick': 2, 
'James': 1, 'Joan': 1, 'Jett': 1, 'Nicks': 1, 'Berlin': 1, 'Sting': 1, 'New': 3, 'Order': 1, 'Poison': 1, 'Pretenders': 1, 'Quiet': 1, 'Riot': 1, 'RATT': 1, 'Clash': 1, 'Stone': 1, 'Squeeze': 1, 'Styx': 1, 'Frankie': 1, 'Goes': 1, 'to': 1, 'Hollywood': 1, 'Edition': 1, 'Stray': 1, 'Cats': 1, 'Paula': 1, 'Abdul': 1, 'Human': 1, 'League': 1, 'Violent': 1, 'Femmes': 1, 'Elvis': 1, 'Costello': 1, 'A-Ha': 1, 'Blondie': 1, 'Eddie': 1, 'Money': 1, 'Anita': 1, 'Baker': 1, 'Sheena': 1, 'Easton': 1, 'Loverboy': 1, 'Asia': 1, 'Skid': 1, 'Row': 1, 'Tiffany': 1, 'Debbie': 1, 'Gibson': 1, 'Crosby': 1, 'Stills': 1, 'Nash': 1, '(&': 1, 'Young)': 1, 'Madness': 1, 'Aretha': 1, 'Franklin': 1, 'Afrika': 1, 
'Bambaataa': 1, 'UB': 1, '40': 1, 'Patti': 1, 'LaBelle': 1, 'Tone-Loc': 1, 'Falco': 1, 'Simple': 1, 'Minds': 1, 'Earth': 1, 'Wind': 1, 'Fire': 1, 'KISS': 1, 'Jam': 1, 'Marvin': 1, 'Gaye': 1, 'Bananarama': 1, 'Kids': 1, 'on': 1, 'Block': 1, 'Squier': 1, 'Slayer': 1, 'Adam': 1, 'Ant': 1, 'Spandau': 1, 'Ballet': 1, 'Milli': 1, 'Vanilli': 1, 'Jesus': 1, 'Mary': 1, 'Chain': 1, 'ABC': 1, 'Cinderella': 1, 'Bonnie': 1, 'Raitt': 1, '10,000': 1, 'Maniacs': 1, 'Accept': 
1, 'Clapton': 1, 'Moe': 1, 'Dee': 1, 'Cult': 1, 'Fixx': 1, 'Air': 1, 'Supply': 1, 'Richard': 1, 'Marx': 1, 'Hornsby': 1, 'Range': 1, 'Starship': 1, 'Replacements': 1, 'Fine': 1, 'Young': 2, 'Cannibals': 1, 'Mr.': 1, 'Mister': 1, 'Boogie': 1, 'Down': 1, 'Productions': 1, 'Irene': 1, 'Cara': 1, 'Lee': 1, 'Roth': 1, 'Twisted': 1, 'Sister': 1, 'Corey': 1, 'Hart': 1, 'Doug': 1, 'E.': 1, 'Laura': 1, 'Branigan': 1, 'Dio': 1, 'Dokken': 1, 'A': 1, 'Flock': 1, 'of': 1, 
'Seagulls': 1, 'Eddy': 1, 'Grant': 1, 'HÃ¼sker': 1, 'DÃ¼': 1, 'Black': 2, 'Flag': 1, 'Dead': 1, 'Kennedys': 1, 'Thorogood': 1, 'Lennon': 1, 'Terence': 1, 'Trent': 1, "D'arby": 1, 'Hot': 1, 'Chili': 1, 'Peppers': 1, 'Springfield': 1, 'Sabbath': 1, 'Howard': 1, 'Jones': 1, 'Orchestral': 1, 'Manoeuvres': 1, 'in': 1, 'Dark': 1, 'Level': 1, '42': 1, 'Europe': 1, 'Waits': 1, 'Mike': 1, 'Oldfield': 1, 'Chris': 1, 'Burgh': 1, 'Alan': 1, 'Parsons': 1, 'Project': 1, 'Farnham': 1}

"""