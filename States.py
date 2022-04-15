from pygame import *
init()
fontsize = 15
allSprites = sprite.Group([])
offset = 0
class text(sprite.Sprite):
    def __init__(self,text,x,y,fontsize):
        self.font = font.SysFont('timesnewroman',fontsize)
        super().__init__()
        self.xpos,self.ypos = x,y
        self.text = []
        for i in text:
            self.text.append(self.font.render(i,False,(0,0,0)))
    def Render(self,window):
        for i in range(len(self.text)):
            window.blit(self.text[i],(self.xpos,self.ypos+(fontsize*i)+(7*i)))
class Object(sprite.Sprite):
    def __init__(self,name,data):
        super().__init__()
        self.image = transform.scale(image.load("Sprites/Select/"+name+".png"),(960,600))
        self.rect = self.image.get_rect()
        self.mask = mask.from_surface(self.image)
        self.state = data
        allSprites.add(self)
class State():
    def __init__(self,name,capitol,capinfo,bird,flower,fInfo,des):
        self.data = [name,capitol,capinfo,bird,flower,fInfo,des]
        self.sprites = sprite.Group([])
        self.text = sprite.Group([])
        self.name = None
        self.flag = None
        self.capitol = None
        self.capInfo = None
        self.bird = None
        self.birdImg = None
        self.birdSong = None
        self.flower = None
        self.flowerImg = None
        self.flowerInfo = None
        self.des = None
    def Load(self):
        self.name = text(self.data[0],25,25,50)
        self.flag = sprite.Sprite()
        self.flag.image = transform.scale(image.load("Sprites/flags/"+self.data[0][0]+".png"),(225,150))
        self.flag.rect = self.flag.image.get_rect(topleft=(25,75))
        self.capitol = text(self.data[1],300,25,30)
        self.capInfo = text(self.data[2],300,75,20)
        self.bird = text(self.data[3],25,375,30)
        self.birdImg = sprite.Sprite()
        self.birdImg.image = transform.scale(image.load("Sprites/Birds/"+self.data[0][0]+".png"),(150,150))
        self.birdImg.rect = self.birdImg.image.get_rect(topleft=(25,450))
        self.birdSong = mixer.Sound("Sounds/"+self.data[0][0]+".mp3")
        self.flower = text(self.data[4],500,375,30)
        self.flowerImg = sprite.Sprite()
        self.flowerImg.image = transform.scale(image.load("Sprites/Flowers/"+self.data[0][0]+".png"),(150,150))
        self.flowerImg.rect = self.flowerImg.image.get_rect(topleft=(500,450))
        self.flowerInfo = text(self.data[5],725,500,20)
        self.des = text(self.data[6],25,250,15)
        self.sprites.add(self.flag,self.birdImg,self.flowerImg)
        self.text.add(self.name,self.capitol,self.capInfo,self.bird,self.flower,self.flowerInfo,self.des)
        return self
    def Render(self,window):
        self.sprites.draw(window)
        for i in self.text:
            i.Render(window)
#alabama
alabamaData = State(["Alabama"],["Capitol: Montgomery","Population: 200,603"],["Established in 1846","Rank in state: 17th"],["Yellowhammer (Northern flicker)","Colaptes auratusa"],["Camellia","Genus: Theaceae,"],["Medicinal uses:The flowers are astringent, antihemorrhagic, haemostatic, salve and tonic.","When mixed with sesame oil they are used in the treatment of burns and scalds."],["Flag was adopted in 2015","U.S. state flag consisting of a white field with a red saltire (diagonal cross),represented the sepration of Alabama from the Union"])
alabama = Object("Alabama",alabamaData)
#alaska
alaskaData = State(["Alaska"],["Capitol: Juneau","Population: 31,275"],["Established in 1900","Rank in state: 45th"],["Willow ptarmigan","Lagopus lagopusa"],["Alpine Forget-me-not","Genus: Scorpion Grasses"],["Medicinal uses:Used for its therapeutic properties, forget-me-nots can be used as an astringent in poultices for wounds to tighten tissues."],["Flag was adopted in 1927","Eight gold stars, in the shape of the big dipper, on a blue background.","The blue field is for the Alaska sky and the forget-me-not, an Alaskan flower.","The North Star is for the future of the state of Alaska, the most northerly in the Union.","The dipper is for the Great Bear – symbolizing strength (sic)."])
alaska = Object("Alaska",alaskaData)
#arizona
arizonaData = State(["Arizona"],["Capitol: Phoenix","Population: 1,608,139"],["Established in 1889","Rank in state: 1st"],["Cactus wren","Campylorhynchus brunneicapillus"],["Saguaro Cactus Blossom","Genus: Carnegiea familyr"],["Medicinal uses:They have high moisture retention to hydrate your body.","Saguaros are also loaded with Vitamin C, Vitamin B12 and other key minerals","to nurture your organs and enable better functioning."],["Flag was adopted in 1917","The red and yellow also symbolize Arizona's picturesque landscape.","The center star signifies copper production; Arizona produces more copper than any other state in the US.","The white represents snow-capped mountains","The colors of red and blue are the same shade used on the flag of the United States."])
arizona = Object("Arizona",arizonaData)
#arkansas
arkansasData = State(["Arkansass"],["Capitol: Little Rock","Population: 202,591"],["Established in 1821","Rank in state: 21st"],["Northern mockingbird","Mimus polyglottoss"],["Apple Blossom","Genus: Apples"],["Medicinal uses: Apple blossoms are generally very high in antioxidants and important in ridding the body of free radicals. A tea of dried Apple blossoms may be consumed as a stress reliever, digestion aid or to clear complexion."],["Flag was adopted in 1913","The diamond represents Arkansas' status as the only diamond-bearing state in the Union.","25 of white stars around the border of the diamond represent Arkansas' position as the 25th state to join the Union.","The star above ARKANSAS represents the Confederacy.","The three stars on the bottom are for The three nations to which Arkansas has belonged (France, Spain, and the U.S.) The Louisiana Purchase, which brought Arkansas into the U.S was signed in 1803.","Arkansas was the third state (after Louisiana and Missouri) formed from the Louisiana Purchase"])
arkansas = Object("Arkansas",arkansasData)
#california
californiaData = State(["California"],["Capitol: Sacramento","Population: 524,943"],["Established in 1854","Rank in state: 9th"],["California quail","Callipepla californica"],["California poppy","Genus: Eschscholzia"],["Medicinal Uses:It is the state flower of California.","People use the parts that grow above the ground for medicine.","California poppy is used for trouble sleeping (insomnia), aches, nervous agitation, bed-wetting in children, and diseases of the bladder and liver. It is also used to promote relaxation."],["Flag was adopted in 1911","The bear on the flag represents the strength of the state.","The star represents sovereignty.","The red color signifies courage and the white background stands for purity."])
california = Object("California",californiaData)
#colorado
coloradoData = State(["Colorado"],["Capitol: Denver","Population: 715,522"],["Established in 1867","Rank in state: 1st"],["Lark Bunting","Calamospoza Melanocoryso"],["Rocky Mountain Columbine","Columbine"],["Medicinal uses: Colorado columbine is the state flower of Colorado. All parts of the plant are poisonous if ingested.The seed was chewed, or an infusion of the root was used, to treat abdominal pains and general sickness by Native Americans. The seed was also used as a parasiticide to rid the hair of lice."],["Flag was adopted in 1964","The colors of the flag symbolize Colorado's geographical features","The gold symbolizes the states abundant sunshine","The white represents snow-capped mountains","The blue symbolizes clear blue skies","The red represents the color of much of the state's soil"])
colorado = Object("Colorado",coloradoData)
#connecticut
connecticutData = State(["Connecticut"],["Capitol: Hartford","Population: 121,054"],["Established in 1875","Rank in state: 29th"],["American robin","Turdus migratorius"],["Mountain Laurel","Genus: Kalmia"],["Medicinal uses:Mountain laurel is a plant. The fresh or dried leaves are used to make medicine.","People apply mountain laurel directly to the affected area to t reat ringworm of the scalp (tinea capitis), psoriasis, herpes, and syphilis."],["Flag was adopted in 1897","The grape vines represent the three oldest settlements (Windsor, Wethersfield, and Hartford) (or possibly the three separate settlements, Connecticut Colony, Saybrook Colony, and New Haven Colony, which had been absorbed into Connecticut by that time).","Connecticut's motto, Qui Transtulit Sustinet, means He who transplanted continues to sustain."," It is an adaptation of Psalms , Chapter 79, verse 3, of the Latin Vulgate Version of the Bible. The background of Connecticut's flag is azure blue.","A white baroque shield is located in the center and has three green and purple grape vines.","There is a white banner trimmed in gold placed below the shield, with the state's motto in Latin written in black text."])
connecticut = Object("Connecticut",connecticutData)
#delaware
delawareData = State(["Delaware"],["Capitol: Dover","Population: 26,047"],["Established in 1777","Rank in state: 1st"],["Delaware Blue Hen","Gallus gallus"],["Peach Blossom","Thyatira"],["Medicinal uses: Peach blossom contains compounds that can dilate blood vessels,","clear the context, moisturize the skin,","promote blood circulation, but also benefit the line of water,","blood circulation, laxative effect"],["Adopted on July 24, 1913,","the Delaware state flag has a background of colonial blue surrounding a diamond of buff color in which the coat of arms of the state is placed.","Below the diamond are the words “December 7, 1787,” indicating the day on which Delaware was the first state to ratify the United States constitution","The coat of arms featuring a shield with an ox, an ear of corn and wheat, which represent the state's agriculture.","There is a sailing ship above the shield representing the coastal commerce and the shipbuilding industry."])
delaware = Object("Delaware",delawareData)
#florida
floridaData = State(["Florida"],["Capitol: Tallahassee","Population: 196,169"],["Established in 1824","Rank in state: 1st"],["Northern mockingbird","Mimus polyglottos"],["Orange Blossom"," genus citrus"],["Medicinal uses: Reduces cortisol levels, lowers blood pressure,","improves menopausal symptoms, Reduces inflammation,","acts as an antimicrobial substance, exerts antispasmodic effects,","acts as an anticonvulsant."],["Was adopted in1868(modifications made in November 1900 and May 1985).","The Florida state flag's current design features diagonal red bars and the state seal","To art majors, it's a saltire, a heraldic symbol. To theologians, it's a St. Andrew's Cross,","named for the Christian apostle who was nailed upon it.","The seal features a brilliant sun, a cabbage palmetto tree,","a steamboat sailing and a Native American Seminole woman scattering flowers."])
florida = Object("Florida",floridaData)
#georgia
georgiaData = State(["Georgia"],["Capitol: Atlanta","Population: 498,715"],["Established in 1868","Rank in state: 1st"],["Brown Thrasher","Toxostoma rufum"],["Cherokee Rose","rose"],["Medicinal uses: Treatment of night sweats, frequent urination, bed wetting,","ongoing diarrhea, ongoing cough, high blood pressure,","and swelling (inflammation) of the intestine (enteritis)"],["Georgia was adopted on May 8, 2003.","The flag bears three stripes consisting of red-white-red,","featuring a blue canton containing a ring of 13 white stars encompassing the state's coat of arms in gold.","In the coat of arms, the arch symbolizes the state's constitution while the pillars represent the three branches of government.","The words of the state motto, 'Wisdom, Justice, and Moderation', are wrapped around the pillars,","guarded by a male figure dressed in colonial attire from the American Revolutionary War.","Within the arms, a sword is drawn to represent the defense of the state's constitution with an additional motto, In God We Trust, featured below these elements.","The ring of stars that encompass the state's coat of arms represents Georgia as one of the original Thirteen Colonies."])
georgia = Object("Georgia",georgiaData)
#hawaii
hawaiiData = State(["Hawaii"],["Capitol: Honolulu","Population: 350,964"],["Established in 1959","Rank in state: 1st"],["Hawaiian goose","Branta sandvicensis"],["'Ohia Lehua","Metrosideros"],["Medicinal uses: Its wood was used as kapa cloth beaters, as boards for pounding poi,","and for building structures and statues.","Its flowers were used for medicinal purposes, like easing the pain of childbirth."],["December 29, 1845 (last modified in 1898).","Eight alternating horizontal stripes of white, red, and blue, with the United Kingdom's Union Flag in the canton.","The flag's red stripes are said to symbolize Hawaii gods,","while the white represents truth, and the blue signifies the ocean.","The Hawaiian flag originally represented the Kingdom of Hawaii.","After the overthrow of the monarchy the flag came to represent the Republic and then the Territory of Hawaii."])
hawaii = Object("Hawaii",hawaiiData)
#idaho
idahoData = State(["Idaho"],["Capitol: Boise","Population: 235,684"],["Established in 1865","Rank in state: 1st"],["Mountain bluebird","Sialia currucoides"],["Syringa","lilac"],["Medicinal uses: The herbal tea from a Syringa,","is used against helminths, malaria, sore throat and fever.","The essential oil is applied to the skin for the treatment of various skin problems such as rashes, burns and wounds."],["The seal of the Territory of Idaho was adopted in 1863 and redrawn several times before statehood in 1890.","Idaho has a game law, which protects the elk and moose, and an elk's head rises above the shield.","The state flower, the wild syringa or mock orange, grows at the woman's feet,","while the ripened wheat grows as high as her shoulder.legislation specified that the flag was to be blue with the name of the state.","However, the legislation gave the Idaho Adjutant General control over the final design,","and it was suggested to honor the First Idaho Infantry by using their battle flag."])
idaho = Object("Idaho",idahoData)
#illinois
illinoisData = State(["Illinois"],["Capitol: Springfield","Population: 114,394"],["Established in 1839","Rank in state: 1st"],["Northern cardinal","Cardinalis cardinalis"],["Violet","viola"],["Medicinal uses: Some people use sweet violet for respiratory tract conditions,","usually dry or sore throat, stuffy nose, coughs, hoarseness, and bronchitis.","Other uses include treating pain in the minor joints, fever, skin diseases, headache,","trouble sleeping (insomnia), and tuberculosis."],["Adopted on June 27, 1969.","The state's seal was based upon the design of the seal of the United States.","It features an eagle with a banner that has the state's motto: State Sovereignty, National Union.","It also features the date of 1818, which is when Illinois became a state."])
illinois = Object("Illinois",illinoisData)
#indiana
indianaData = State(["Indiana"],["Capitol: Indianapolis","Population: 887,642"],["Established in 1825","Rank in state: 1st"],["Northern cardinal","Cardinalis cardinalis"],["Peony","Paeonia"],["Medicinal uses: The roots are commonly used in Traditional Chinese Medicine for many purposes.","Peony might block chemicals that usually cause pain and swelling.","It might also prevent blood clotting, kill cancer cells, and act as an antioxidant."],["It was adopted in 1917","The torch stands for liberty and enlightenment;","the rays represent their far-reaching influence.","The thirteen stars in a circle represent the original thirteen states;","the five stars in the circle represent the next five states;","the large star is Indiana, the nineteenth state."])
indiana = Object("Indiana",indianaData)
#iowa
iowaData = State(["Iowa"],["Capitol: Des Moines","Population: 214,133"],["Established in 1857","Rank in state: 1st"],["Eastern goldfinch","Spinus tristis"],["Wild Rose","genus rosa"],["Medicinal uses: The wild rose is great for deterring feral cats and wild dogs from attacking animals hiding within its thicket.","Wild Rose petals and rose hips are used by the Kumeyaay in food and tea.","An infusion of petals is given to babies with a fever."],["Was adopted in 1921","A vertical tricolor consisting of blue, white, red.","The center stripe is twice the width of the other two and contains an eagle holding a ribbon.","The flag consists of three vertical stripes: the blue stripe stands for loyalty, justice and truth;","the white stripe for purity; and the red stripe for courage."])
iowa = Object("Iowa",iowaData)
#kansas
kansasData = State(["Kansas"],["Capitol: Topeka","Population: 126,587"],["Established in 1861","Rank in state: 1st"],["Western meadowlark","Sturnella neglecta"],["Wild Native Sunflower","Helianthus"],["Medicinal uses: The Wild Native Sunflower ranged from wart removal, sunstroke treatment, snake bite remedies,","body ointments, cauterization and healing of wounds, to treatment of chest pains."],["Adopted in 1927","The flag contains the state seal of Kansas,","the word KANSAS in yellow, a sunflower, and a yellow and blue bar.","The flag is full of symbolism. The gold and blue bar symbolizes that Kansas was part of the Louisiana Purchase.","When looked at closely, the state seal tells us much about Kansas in 1861."])
kansas = Object("Kansas",kansasData)
#kentucky
kentuckyData = State(["Kentucky"],["Capitol: Frankfort","Population: 25,527"],["Established in 1793","Rank in state: 1st"],["Northern cardinal","Cardinalis cardinalis"],["Goldenrod","Solidago"],["Medicinal uses: Goldenrod has also been used to treat tuberculosis, diabetes,","enlargement of the liver, gout, hemorrhoids, internal bleeding,","asthma, and arthritis."],["1918 was the year it was adopted.","The flag of Kentucky features the state's seal.","The design of the seal features a pioneer and a statesman in an embrace.","It is believed by many that the pioneer is supposed to be Daniel Boone, while the statesman is Henry Clay.","However, officially, it is said that this image symbolizes all frontiersmen and statement.","The flag shows the State's (Commonwealth's) seal on navy blue, surrounded by the words ``Commonwealth of Kentucky” above and Sprays of goldenrod extend in a half circle around the picture which is Kentucky's state flower.","Kentucky state flag flying. The seal depicts a pioneer and a statesman embracing."])
kentucky = Object("Kentucky",kentuckyData)
#louisiana
loisianaData = State(["Louisiana"],["Capitol: Baton Rouge","Population: 227,470"],["Established in 1882","Rank in state: 1st"],["Brown pelican","Pelecanus occidentalis"],["Magnolia","Magnolia"],["Medicinal uses: The extract of the bark of Magnolia trees has been used for some 1,000 years","in traditional Chinese and Japanese medicine for treatment of maladies ranging from asthma to depression to headaches to muscle pain."],["Adopted in 1861.","It consists of a 'pelican in her piety',","the heraldic charge representing a mother pelican'","in her nest feeding her young with her blood' on an azure field with state motto reworded to 'Union Justice [and] Confidence.'","First adopted in 1912, it was last modified in 2010.","The flag consists of a solid blue field, symbolizing truth.","The coat-of-arms is featured with the pelican feeding its young, in white in the center.","A ribbon beneath contains the motto of the state, 'Union, Justice and Confidence'."])
loisiana = Object("Loisiana",loisianaData)
#maine
maineData = State(["Maine"],["Capitol: Augusta","Population: 197,191"],["Established in 1832","Rank in state: 12th"],["Black-Capped Chickadee","Poecile atricapillus"],["White Pine Cone and Tassel","pinus genus"],["Medicinal uses: White pine has been used for generations as a natural herbal remedy."],["Adopted in 1901","The current state flag was established in February 1909.","Its coat of arms shows a moose-and-pine-tree emblem on a shield supported by a farmer and a sailor;","a ribbon below bears the state name, and above is the North Star and the Latin motto “Dirigo” (“I direct”)."])
maine = Object("Maine",maineData)
#maryland
marylandData = State(["Maryland"],["Capitol: Annapolis","Population: 38,394"],["Established in 1694","Rank in state: 1st"],["Baltimore oriole","Icterus galbula"],["Black-Eyed Susan","Coneflowers"],["Medicinal uses: The stem is an effective treatment for those suffering from high blood pressure,","and the entire plant treats ulcers and bodily swelling."],["Maryland's flag bears the arms of the Calvert and Crossland families.","Calvert was the family name of the Lords Baltimore who founded Maryland,","and their colors of gold and black appear in the first and fourth quarters of the flag.","Crossland was the family of the mother of George Calvert, first Lord Baltimore."])
maryland = Object("Maryland",marylandData)
#massachusetts
massachusettsData = State(["Massachusetts"],["Capitol: Boston","Population: 675,647"],["Established in 1630","Rank in state: 1st"],["Black-capped chickadee","Poecile atricapilla"],["Mayflower","Epigaea Repens"],["Medicinal uses: The Mayflower is one of the most effective remedies for cystitis,","urethritis, prostatitis, bladder stones and","particularly acute catarrhal cystitis."],["Adopted in 1907","The shield depicts an Algonquian Native American with bow and arrow;","the arrow is pointed downward, signifying peace.","A white star with five points appears next to the figure's head, signifying Massachusetts as a U.S. state."])
massachusetts = Object("Massachusetts",massachusettsData)
#michigan
michiganData = State(["Michigan"],["Capitol: Lansing","Population: 112,644"],["Established in 1847","Rank in state: 1st"],["American robin","Turdus migratorius"],["Dwarf Lake Iris","Irises"],["Medicinal uses: None, since it is an endangered species of flowers"],["Adopted in 1911","The state coat of arms depicts a blue shield, upon which the sun rises over a lake and peninsula,","and a man with a raised hand representing peace and holding a long gun representing the fight for state and nation as a frontier state."])
michigan = Object("Michigan",michiganData)
#minnesota
minnesotaData = State(["Minnesota"],["Capitol: Saint Paul","Population: 311,527"],["Established in 1849","Rank in state: 1st"],["Common loon","Gavia immer"],["Pink & White Lady Slipper","Cypripedium"],["Medicinal uses: The root of lady's slipper was used as a remedy for nervousness,","tooth pain, and muscle spasms."],["Adopted in 1983","The star represents 'L'etoile du Nord' and Minnesota's natural wealth,","the blue background represents Minnesota's lakes and rivers,","the white represents winter, and the green represents farmland and forests.","The waves represent the name Minnesota, a Dakota word which means 'sky-tinted waters'."])
minnesota = Object("Minnesota",minnesotaData)
#mississippi
mississippiData = State(["Mississippi"],["Capitol: Jackson","Population: 153,701"],["Established in 1822","Rank in state: 1st"],["Northern mockingbird","Mimus polyglottos"],["Coreopsis","Asteraceae"],["Medicinal uses: Native Indians have used this plant to treat several disorders,","including diarrhea, internal pain, and bleeding,","to strengthen blood and as an emetic"],["Adopted in 2021","The new state flag features a magnolia flower,","a symbol of hospitality, surrounded by 20 stars, signifying Mississippi's status as the 20th state in the union,","and a gold five-point star to reflect Mississippi's indigenous Native American tribes."])
mississippi = Object("Mississippi",mississippiData)
#missouri
missouriData = State(["Missouri"],["Capitol: Jefferson City","Population: 43,079"],["Established in 1826","Rank in state: 1st"],["Eastern bluebird","Sialia sialis"],["White Hawthorn Blossom","Crataegus"],["Medicinal uses: Hawthorn is the oldest known medicinal plant.","The fruit, leaves, and flowers are typically used as a heart tonic, an astringent,","for muscle spasms, and for high blood pressure and high cholesterol."],["Adopted in 1913","The Oliver flag embraced national pride,","and at the same time expressed characteristics of Missouri and Missourians.","The three large stripes were symbolic of the people of the state—the blue stripe represented vigilance, permanency,","and justice, the red represented valor, and the white stripe symbolized purity."])
missouri = Object("Missouri",missouriData)
#montana
montanaData = State(["Montana"],["Capitol: Helena","Population: 28,190"],["Established in 1875","Rank in state: 1st"],["Western meadowlark","Sturnella neglecta"],["Bitterroot","Bitterroot"],["Medicinal uses: Bitterroot can be chewed as a cure for toothaches and sore throats,","made into cough syrup, or placed on the hot stones in the sweatlodge to create a decongestant steam."],["Adopted in 1905","The state flag of Montana shall be a flag","having a blue field with a representation of the great seal of the state in the center","and with golden fringe along the upper and lower borders of the flag;","the same being the flag borne by the 1st Montana Infantry, U.S.V., in the Spanish-American War."])
montana = Object("Montana",montanaData)
#nebraska
nebraskaData = State(["Nebraska"],["Capitol: Lincoln","Population: 55,274"],["Established in 1861","Rank in state: 1st"],["Western meadowlark","Sturnella neglecta"],["Goldenrod","Solidago"],["Medicinal uses: Goldenrod has also been used to treat tuberculosis, diabetes,","enlargement of the liver, gout, hemorrhoids, internal bleeding,","asthma, and arthritis."],["Adopted in 1925","A depiction of the Missouri River is located on the seal.","A cabin and wheat represent the importance of settlers and the agriculture of the state.","A blacksmith with his anvil is also found on the seal,","representing the state's history of blacksmithing."])
nebraska = Object("Nebraska",nebraskaData)
#nevada
nevadaData = State(["Nevada"],["Capitol: Carson City","Population: 55,274"],["Established in 1861","Rank in state: 1st"],["Mountain bluebird","Sialia currucoides"],["Sagebrush","Mugworts"],["Medicinal uses: Sagebrush has been used for thousands of years for medicine,","ceremony, fiber, dye, and more.","Many tribes traditionally used sagebrush as a medicine to treat a variety of ailments including as a tea for stopping internal bleeding,","treating headaches and colds."],["Adopted in 1991.","The state flag of Nevada features a variant of the state's emblem located in the canton.","Broken down, the emblem contains a silver star, which symbolizes the nickname 'The Silver State.'","The flag also features the motto, 'Battle Born,' which references Nevada's statehood during the Civil War."])
nevada = Object("Nevada",nevadaData)
#new hampshire

#new jersey

#new mexico

#new york

#north carolina

#north dakota

#ohio
ohioData = State(["Ohio"],["Capitol: Columbus","Population: 905,748"],["Established in 1816","Rank in state: 1st"],["Northern cardinal","Cardinalis cardinali"],["Red Carnation","Pink"],["Medicinal uses: Carnation is used for treating muscle spasms and improve heart health."],["Adopted 1902","The Ohio flag has three red and two white horizontal stripes.","At its staff end is a blue triangular field with the apex at the center of the middle red stripe.","There are 17 white, five-pointed stars grouped around a red disc superimposed upon a white circular O."])
ohio = Object("Ohio",ohioData)
#oklahoma

#oregon

#pennsylvania

#rhode island

#south carolina
south_carolinaData = State(["South Carolina"],["Capitol: Columba","Population: 136,632"],["Established in 1790","Rank in state: 27th"],["Carolina wren","Thryothorus ludovicianus"],["Yellow Jessamine","Gelsemium"],["Medicinal uses: Yellow jasmine has a strong tranquilizing action, so it became a popular pain reliever and sedative, as well as an antispasmodic for asthma, whooping cough, and croup."],["The flag of South Carolina is a symbol of the U.S. state of South Carolina consisting of a blue field with a white palmetto tree and white crescent.  The crescent symbol represents the silver emblem worn on the caps of South Carolina troops during the revolutionary war. The Sabal Palmetto is a symbol of courage and strength. During the Revolutionary War's Battle of Sullivan's Island, a fort was crafted out of horizontal palmetto trunks. Adopted in 1861."])
south_carolina = Object("South Carolina",south_carolinaData)
#south dakota
south_dakotaData = State(["South Dakota"],["Capitol: Pierre","Population: 13,646"],["Established in 1889","Rank in state:49th"],["Ring-necked pheasant","Phasianus colchicus"],["American Pasque","Anemone"],["Medicinal uses: Pasque also increases venous circulation, to induce sweating and break fever (diaphoretic), and eruptive infections."],["Flag was adopted in 1909","The symbols on the great seal of South Dakota represent the state's commerce, industry, and natural resources. Under God the People Rule South Dakota's state motto appears at the top of the inner circle, which has a background of sky and hills."])
south_dakota = Object("South Dakota",south_dakotaData)
#tennessee
tennesseeData = State(["Tennessee"],["Capitol: Nashville","Population: 689,447"],["Established in 1826","Rank in state: 7th"],["Northern mockingbird","Mimus polyglottos"],["Tennessee Coneflower","Coneflower"],["Medicinal uses: Echinacea was used during the 18th and 19th centuries to treat a variety of ailments including malaria, blood poisoning, and syphilis."],["The designer chose white for purity, blue to denote respect for Tennessee, red as the traditional color for America; stars to symbolize the state's three Grand Divisions; wheat for agricultural heritage; and the gavel for the power of the people vested in the state's legislative body. Adopted in 1905."])
tennessee = Object("Tennessee",tennesseeData)
#texas
texasData = State(["Texas"],["Capitol: Austin","Population: 961,855"],["Established in 1845","Rank in state: 2nd"],["Northern mockingbird","Mimus polyglottos"],["Bluebonnet","Lupine"],["Medicinal uses: Bluebonnets can be used as a legume, bluebonnets have roots that work with a bacterium called Rhizobium to improve plant growth and flowering."],["Flag was adopted in 1836","It specified that the flag should consist of a blue perpendicular stripe of the width of one-third of the whole length of the flag and a white star of five points in the center thereof and two horizontal stripes of equal length and breadth, the upper stripe of white, the lower of red, of the length of two thirds of the length of the whole flag."])
texas = Object("Texas",texasData)
#utah
utahData = State(["Utah"],["Capitol: Salt Lake City","Population: 199,723"],["Established in 1856","Rank in state: 22st"],["California Gull","Larus californicus"],["Sego Lily","Calochortus"],["When eaten, the palatability of the herbage is good for sheep and fair for cattle. Horses do not graze it. The bulbs are eaten, and also gathered and stored by pocket gophers and other rodents."],["According to the organization, the gold beehive represents Utah as the Beehive State and the state's motto of Industry. The star below the beehive represents Utah's statehood and joining of the Union in 1896, and the triangular saltire symbolizes Utah's moniker as the Crossroads of the West. Adopted in 2011."])
utah = Object("Utah","test") 
#vermont
vermontData = State(["Vermont"],["Capitol: Montpelier","Population: 7,855"],["Established in 1805","Rank in state: 50th"],["Lark Hermit","thrushlam Catharus guttatus"] ["RockyRed CloveroweCloverfloweIT has been used to treat whooping cough,respiratory problems, and skin inflammations.Flag wAdopt in 1923. Multiple versions of the flag have been included throughout history. Originally, the flag was the same as the flag of the Green Mountain Boys.loravermontect"])
vermont = Object("Vermont",vermontData)
#virginia
virginiaData = State(["Virginia"],["Capitol: Richmond","Population: 226,610"],["Established in 1780","Rank in state: 19th"],["Northern Cardinal","Cardinalis cardinalis"],["American Dogwood","Cornus"],["People use dogwood for headaches, fatigue, fever, and ongoing diarrhea. It is also used to increase strength, to stimulate appetite, and as a tonic. Some people apply American dogwood directly to the skin for boils and wounds"],["The reverse showed women symbolizing liberty, eternity, and agriculture. The design on the obverse now appears on the state flag. It features a woman personifying virtue and dressed as an Amazon. She wears a helmet and holds a spear and sword above the Latin motto “Sic semper tyrannis” (“Thus always to tyrants”). Adopted in 1861."])
colorado = Object("Colorado",coloradoData)
#washington
washingtonData = State(["Washington"],["Capitol: Olympia","Population: 46,478"],["Established in 1885","Rank in state: 38th"],["Willow goldfinch","Spinus tristis"],["Coast Rhododendron","Rhododendron L."],["Rhododendron is one of the naturally occurring plants which possess various health benefits, such as prevention and treatment of diseases associated with heart, dysentery, diarrhea, detoxification, inflammation, fever, constipation, bronchitis and asthma."],["Adopt 1923. The flag of Washington consists of the state seal, displaying an image of its namesake George Washington, on a field of dark green with gold fringe being optional. It is the only U.S. state flag with a field of green as well as the only state flag with the image of an American president."])
washington = Object("Washington",washingtonData)
#west virginia
west_virginiaData = State(["West Virginia"],["Capitol: Charleston","Population: 51,400"],["Established in 1885","Rank in state: 38th"],["Northern cardinal","Cardinalis cardinalisa"],["Rhododendron","Rhododendron"],["Medicinal uses:Rhododendron is one of the naturally occurring plants which possess various health benefits, such as prevention and treatment of diseases associated with heart, dysentery, diarrhea, detoxification, inflammation, fever, constipation, bronchitis and asthma."],["The current state flag of West Virginia consists of a pure white field bordered on four sides by a stripe of blue. The white of the field symbolizes purity, while the blue border represents the Union. Adopted in 1929.The present flag consists of a pure white field bordered by a blue stripe with the coat of arms of West Virginia in the center, wreathed by Rhododendron maximum and topped by an unfurled red ribbon reading, State of West Virginia. It is the only state flag to bear crossing rifles."])
west_virginia= Object("West Virginia",west_virginiaData)
#wisconsin
wisconsinData = State(["Wisconsin"],["Capitol: Madison","Population: 269,840"],["Established in 1838","Rank in state: 15th"],["American robin","Turdus migratoriusn"],["Wood Violet","Violetn"],["Violet is moist and cooling and the leaves ease inflammation, and when used externally, soothe skin irritations and swelling. It has an affinity for the lymphatic system and can promote healthy lymphatic function. "],["The tools of the important trades of the times lie within the shield: the symbols for agriculture (plow), mining (pick and shovel), manufacturing (arm and hammer), and navigation (anchor). The badger, which is the state animal, sits above the shield. It represents the name given to the lead miners ADOPTED IN 1848."])
wisconsin = Object("Wisconsin",wisconsinData)
#wyoming
wyomingData = State(["Wyoming"],["Capitol: Cheyenne","Population: 64,019"],["Established in 1869","Rank in state: 36th"],["Western meadowlark","Sturnella neglectag"],["Indian Paintbrush","Castillejag"],["Medicinal uses: People use the Indian Paintbrush as a medicine to treat rheumatism and as a bath rinse to make their hair glossy."],["Flag was adopted in 1917","The flag of the state of Wyoming consists of the silhouette of an American bison.","The red symbolizes the Native Americans and the blood of pioneers who gave their lives. The white is a symbol of purity and uprightness."])
wyoming = Object("Wyoming",wyomingData)