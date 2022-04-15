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
delawareData = State(["Delaware"],["Capitol: Denver","Population: 715,522"],["Established in 1867","Rank in state: 1st"],["Lark Bunting","Calamospoza Melanocoryso"],["Rocky Mountain Columbine","Columbine"],["Medicinal uses: Colorado columbine is the state flower of Colorado. All parts of the plant are poisonous if ingested.The seed was chewed, or an infusion of the root was used, to treat abdominal pains and general sickness by Native Americans. The seed was also used as a parasiticide to rid the hair of lice."],["Flag was adopted in 1964","The colors of the flag symbolize Colorado's geographical features","The gold symbolizes the states abundant sunshine","The white represents snow-capped mountains","The blue symbolizes clear blue skies","The red represents the color of much of the state's soil"])
#florida

#georgia

#hawaii

#idaho
idaho = Object("Idaho","test")
#illinois

#indiana

#iowa

#kansas

#kentucky

#louisiana

#maine
maineData = State(["Maine"],["Capitol: Augusta","Population: 197,191"],["Established in 1832","Rank in state: 12th"],["Black-Capped Chickadee","Poecile atricapillus"],["White Pine Cone and Tassel","pinus genus"],["Medicinal uses: White pine has been used for generations as a natural herbal remedy."],["Adopted in 1901","The current state flag was established in February 1909.","Its coat of arms shows a moose-and-pine-tree emblem on a shield supported by a farmer and a sailor;","a ribbon below bears the state name, and above is the North Star and the Latin motto “Dirigo” (“I direct”)."])
maine = Object("Maine",maineData)
#maryland

#massachusetts

#michigan

#minnesota

#mississippi

#missouri

#montana

#nebraska

#nevada
nevada = Object("Nevada","test")

#new hampshire

#new jersey

#new mexico

#new york

#north carolina

#north dakota

#ohio

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