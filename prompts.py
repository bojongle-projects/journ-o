import random





##present the journ-o with an ideology to follow

ideologyList = ["Neo-Liberal", "Neo-fascist", "Utilitarian", "Neo-Progressive", "Neo-Conservative", "Paeleo-Conservative"]

selectedIdeology = random.choice(ideologyList)





##present the program with a list of topics
#these topics should be typical subjects in news


topicList = ["Technology", "Breaking News", "Sports", "Politics", "Entertainment", "Celebrity News" "World News", "Crime", "Health" ,"Business", "Weather", "Social Media", "Weather", "Fashion", "Travel", "Global Warming", "Space", "Military", "Election", "Nuclear War", "Nuclear", "Food", "Global Disaster","Social Ills", "Criminal Code", "Androids", "Artificial Intelligence ", "Pandemic", "Blizzard", "Fire", "Tsunami"]

selectedTopic = random.choice(topicList)

##present the program with a list of feeling

feelingList = ["Elated", "Happy", "Pleased", "Displeased", "Angry", "Disgusted", "Relaxed", "Terrified", "Optimistic", "Pessimistic", "Less Optimistic", "Little Change in Opinion", "Positive", "Negative"]

selectedFeeling = random.choice(feelingList)
##present the program with a list of characteristics
#these characterists will be used to create the personality profile


picheristicList = ["Introvert", "Extrovert", "Embrace Change", "Resist Change"]

selectedPicheristic = random.choice(picheristicList)
##present the program with a list of locations for the event to take place in


locationList = ["Canada", "United States", "Russia", "China", "United Kingdom", "France", "Germany", "Brazil", "Pakistan", "Turkey", "Egypt" "Dubai", "Mexico", "Canada", "Italy", "Poland", "Ukraine", "Argentina", "Australia", "Canada", "Switzerland", "Spain", "Peru", "Indonesia", "Iran", "Colombia", "Mongolia", "Haiti", "Uganda", "New Belgium", "Mali", "South Africa", "India", "Finland", "Egypt", "Saudi Arabia", "Morocco", "Tanzania", "Saudi Arabia", "Eritrea", "Denmark", "Cambodia", "Belgium", "Syria", "Romania", "Sweden", "Burma", "Bolivia", "Iran", "Thailand", "Kyrgyzstan", "Malawi", "Nepal", "Iran", "Burma", "Mexico", "Ukraine", "Nigeria", "Brazil", "Somalia", "Kenya", "Japan", "Columbia", "Dominican Republic", "Myanmar", "United Kingdom", "Serbia", "Nicaragua", "Republic of the Congo", "Agency Dubai", "Bolivia", "Venezuela", "Chile", "Bangladesh", "Turkish Republic", "Egypt", "Georgia", "Australia", "China", "Germany", "Thailand", "Slovakia", "Twila", "Anchorage", "New York", "The Chrysler", "Knoxville", "Houston", "Fair, Kentucky", "Juniata, United States", "Ohio State University", "James Madison University", "Miami", "The United States", "SPC", "Georgia", "Georgia Institute of Technology", "Five Friends", "Leon State University", "National Republic", "Long Beach State", "Texas State University", "Lafayette", "Arizona State University", "Madison Square Garden", "California", "United States", "Shost Road", "Hancock Village Parks", "University of North Carolina", "Nebraska", "Ohio Air Base", "Southern California", "New Jersey", "Indiana", "Seattle", "Judah A. Gribben Mayfield", "Sioux Falls", "South Philadelphia", "Bowman Lake, Illinois", "Miami University", "Los Angeles", "NC State", "Southern California ", "Georgian College", "Cuhio", "Harvard", "State College, Pennsylvania", "UC San Diego", "New Orleans", "University of Baltimore", "Fort Worth", "Niagara University", "Nove Bay", "Acadia University", "The Other Country", "City Centre", "Mackinaw City", "Back Mountain Cats Hill", "University of California", "North Dakota", "North Carolina", "Santa Barbara", "State University of New York", "Jacksonville", "University of Florida", "UC Riverside", "Gayety Park", "Colorado Springs", "Tennessee State University", "Capitol City", "Indiana State University", "California State University", "WilliamH. Baldwin", "Coast Guard Air Station", "Sasha.", "New Jersey ", "Bethune", "University of Pennsylvania ", "Penn State", "Berkeley", "Guam State College", "Byaman County", "The Great Lakes", "Crescent City, Ohio ", "Fairfield, Texas", "University of Maryland", "Brooklyn College", "Columbia College", "Mayfield County", "Clifford, United States", "Fordham University", "Los Angeles", "Memphis", "Birmingham University", "SpokaneMaryland", "Washington", "MARS U", "University of New York", "Leavenworth", "Orange County Sheriff", "Western Michigan", "Michigan", "Springfield, United States", "Cabbot", "Phoenix", "Michigan", "South Carolina", "Star City, Montana", "Saddle Ridge", "Funky Hill", "USC", "Washington", "Baltimore", "Mills Creek", "Emmons County", "Berryville", "Portland, Maine", "California State University ", "City Centre", "Solar State", "City Centre", "Jenkins County", "Houraldville", "University of Houston", "University of North Carolina ", "Downtown Oakland", "Raleigh State University", "Knox Memorial", "Maine", "Houston", "Utah", "Montclair State University ", "Alexandria", "Milwaukee", "Sioux City", "Reims ", "Owlet Creek", "University of Miami", "Palm Beach County Shooting Range", "Mecca", "Elkhart", "Towson", "Los Angeles", "Elgin, Illinois", "Raleigh", "Hampshire", "University of Rhode Island", "Waynesburg", "AtLanta", "Las Vegas", "Chicago State College", "Madison", "Berkeley", "StarK-State University ", "Monticello", "University of California", "East Brunswick", "Citizen, Aleven", "Orlando", "Linton Parkway Square", "Florida State University", "The Other Country", "Plymouth, United States", "Nashville", "South Feliptaphone", "Umon", "La Valor StateP.", "Virginia Commonwealth University", "Palm Beach", "New Mexico State ", "Bishops", "Delaware Avenue", "Bedrock, NY", "Broad Freeport", "Towson", "Pennsylvania", "Between College", "Western Kentucky University", "Miami Beach", "Alabama", "Kansas City", "Brigham Young University", "Airport", "Seattle", "University of Texas", "Southeast University", "Florida", "Baltimore", "Stony Brook", "Charlotte", "Connecticut", "Crichton ", "Hinton", "Waterford", "Pasadena", "Florida International University", "San Jose", "Lumskin Main Park", "Wesleyan University", "New York City Port 300t", "Auburn", "Los Angeles Federal University", "Mallot", "Rose Hill", "The Rectory", "Chicago State University", "Houston", "City Centre", "Illinois", "Milwaukee", "Montgomery Village", "Clarion", "School of Business", "Florida State University", "Alabama", "Dayton", "Arkansas", "Sacramento", "Staten Island ", "Central College", "Columbia University", "West Park Middle School", "Irvine", "Momentum County", "Hazel Ione", "Balkan City", "Connecticut State University", "Santa Barbara County", "University of Miami", "Toledo University", "California State University ", "Wayne", "Indiana University", "City Centre", "Hartford", "Ohio", "Tallahas", "Two Shores ", "Washington DC ", "Jacksonville", "New York City", "Sept", "West Richmond Bike Colorado", "Rochester", "San Fransisco", "Baylor", "Siena", "Texas A&amp M", "Waverly Beach Massachusetts", "New York", "Shannon-Dustin", "UBC", "Tricounty County", "Bradford City", "Toronto", "Carolina University", "Miami Dade Community College", "Purdue University", "Brazil", "University of Illinois", "Vice City Presley", "Hopkins University", "Tennessee and Beach", "University of Colorado", "Georgia Institute of Technology", "Florida State University", "USC", "Florida State University", "Washington", "Santa Monica", "North Carolina State University", "New York College of Medicine", "Alaska Mission College", "Boston", "University of Chicago", "Johnson and Wales University", "State State", "St. John", "Jacobs University", "University of Washington", "Harrisburg", "Austin", "Cincinnati", "Webster", "University of Houston", "Crown Station", "Ebony Valley", "Indiana (J.R. & L.M Horton ), Richmond University", "Algiers", "University of Nevada ", "University of Illinois", "Providence College", "Southern Peace Center", "Southern College", "University of Tennesee", "West Virginia", "Florida International University", "Harvard University", "University of Pittsburgh", "Humboldt State University", "Lauren", "Leviathan", "Broadway", "Maritime Federal University", "Oklahoma State University", "New Hampshire", "Universize University", "University of Maine", "University of Texas", "Knight Hall ", "Pleasant Library", "Lawrence", "Queen", "Holbrook University", "Virginia Tech.", "Northern Vermont", "Ball State University", "East Carolina University", "St. Petersburg", "University of Arizona", "Georgia State University", "University of Dayton", "Schmidt College", "Cambridge", "New York Brooklyn", "University of Kansas", "University of California", "Clemson", "University of Iowa", "Milton, NY", "Cornell", "Ulysses College", "USIR University", "Alabama", "Brooklyn College", "University of Pittsburgh", "Florida", "University"]
selectedLocation = random.choice(locationList)


##present the program with a format for the articles 

formatingList = ["Expose", "documentation", "news-article", "script", "essay", "short story where you kill everyone by accident", "styleguide", "encyclopedia-text", "financial reports", "recipe", "logbook", "Peer reviewed research paper"]
selectedFormatting = random.choice(formatingList)





#comment out to allow it to work!
print ("The next thing you write will be a " + selectedFormatting + " about " + selectedTopic +  " that happens in/at " + selectedLocation + " have the author feel " +selectedFeeling + " towards the topic while representing " + selectedIdeology + "'s beleifs") 



