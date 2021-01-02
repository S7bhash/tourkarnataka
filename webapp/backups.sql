BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "reviews" (
	"name"	varchar(64),
	"username"	varchar(64),
	"rating"	integer,
	"comments"	text,
	"dates"	datetime,
	FOREIGN KEY("name") REFERENCES "places"
);
CREATE TABLE IF NOT EXISTS "places" (
	"name"	varchar(64),
	"latitude"	varchar(15),
	"longitude"	varchar(15),
	"climate"	varchar(16),
	"language"	varchar(20),
	"description"	text,
	PRIMARY KEY("name")
);
INSERT INTO "reviews" VALUES ('bangalore','S7bhash',4,'Awesome weather','2019/10/29');
INSERT INTO "reviews" VALUES ('coorg','Abc',0,'Worst site in the world','2019-11-05 23:33:13.572767');
INSERT INTO "reviews" VALUES ('coorg','Abc','6/5','Best site in the world','2019-11-05 23:34:20.013766');
INSERT INTO "reviews" VALUES ('murudeshwar','S7bhash',4,'awesome','2019-11-07 15:14:30.053181');
INSERT INTO "reviews" VALUES ('coorg','S7bhash',4,'good place','2019-11-25 20:18:19.199514');
INSERT INTO "reviews" VALUES ('bangalore','Subhash',4,'good place','2019-11-25 22:39:42.289505');
INSERT INTO "reviews" VALUES ('mysore','Subhash',5,'awesome','2019-11-25 22:43:33.509792');
INSERT INTO "reviews" VALUES ('bangalore','S7bhash',4,'great city','2019-11-25 22:45:29.829690');
INSERT INTO "reviews" VALUES ('mysore','S7bhash',4.8,'greatest place','2019-11-25 23:22:52.494682');
INSERT INTO "reviews" VALUES ('bangalore','tester',4.5,'great place and weather','2019-11-25 23:35:16.925772');
INSERT INTO "reviews" VALUES ('bangalore','tester',4.5,'great place and weather','2019-11-25 23:36:04.509575');
INSERT INTO "reviews" VALUES ('bangalore','tester',4,'great place and weather','2019-11-25 23:38:17.046566');
INSERT INTO "reviews" VALUES ('coorg','tester',4.1,'cool place','2019-11-25 23:38:42.305977');
INSERT INTO "reviews" VALUES ('coorg','tester',4.1,'cool place','2019-11-25 23:40:27.756217');
INSERT INTO "reviews" VALUES ('gokarna','S7bhash',3.8,'good place','2019-11-26 00:02:08.976165');
INSERT INTO "places" VALUES ('bangalore','12.97168','77.5946°','moderate','kannada',' Having evolved gradually from being the Garden City to the Silicon Valley of India, Bengaluru is the third largest and one of the most livable cities in India. Bangalore is loved for its pleasant weather, beautiful parks and lakes all around the town.

When in Bangalore, one can choose to take a long, stroll through the greenery of Cubbon Park, shop in many modern malls or street side markets or hop into one of the several acclaimed craft breweries in the city for a cold and refreshing drink. Bangalore had come to be renowned for its eateries, street food corners, quirky cafes, coffee roasters and pubs dotting every corner of the city, serving cuisines from all over the world. Brunches, buffets, burgers, rooftop cafes, late-night eats - Bangalore has it all. ');
INSERT INTO "places" VALUES ('gokarna','14.5479°','74.3188°','humid','kannada,konkani','With its pristine beaches and breathtaking landscapes, Gokarna is a Hindu pilgrimage town in Karnataka and a newly found hub for beach lovers and hippies.

Situated on the coast of Karwar, Gokarna is a small town in Karnataka, primarily known for two reasons - its beaches and temples. Gokarna can be different things to different people. Every year hordes of tourists visit Gokarna in search of sanctity and salvation on one hand and respite and relaxation on the other. The out-of-town beaches are a curious contrast to the life inside the town. Palm clad beaches are dotted with foreign tourists in a majority and very few Indians are seen across. Gokarna is not very conventionally touristy. The beaches are meant for a slow, relaxed holiday and everything on the beach goes at the same relaxed pace. Full of coconut and palm trees, the ocean and clean sands, Gokarna is a ''one of its kind place'' in the country.
');
INSERT INTO "places" VALUES ('coorg','12.3375','75.8069','monsoon','Kodagu','Located amidst imposing mountains in Karnataka with a perpetually misty landscape, Coorg is the place to be for all nature lovers.  This popular coffee producing hill station is not only popular for its beautiful green hills and the streams cutting right through them. It also stands as a popular destination because of its culture and people. The Kodavas, a local clan specialising in martial arts, are especially notable for their keen hospitality. ');
INSERT INTO "places" VALUES ('hampi','15.3350°',' 76.4600°','hot and humid','kannada','Hampi, the city of ruins, is a UNESCO World Heritage Site. Situated in the shadowed depth of hills and valleys in the state of Karnataka, this place is a historical delight for travellers. Surrounded by 500 ancient monuments, beautiful temples, bustling street markets, bastions, treasury building and captivating remains of Vijayanagar Empire, Hampi is a backpacker''s delight. Hampi is an open museum with 100+ locations to explore and a favourite way to see the city from the perspective of its history.');
INSERT INTO "places" VALUES ('mysore','12.2958°','76.6394°','humid ','kannada',' Famously known as The City of Palaces, it wouldn’t be wrong to say that Mysore is one of the most flamboyant places in the country. It is replete with the history of its dazzling royal heritage, intricate architecture, its famed silk sarees, yoga, and sandalwood, to name just a few. Located in the foothills of the Chamundi Hills, Mysore is the third most populated city in the state of Karnataka, and its rich cultural heritage draws millions of tourists all year round.

Mysore is steeped in royal history – it was one of the three largest Princely States in the erstwhile British Empire of India. To this day, the Mysore Palace stands tall as one of the most spectacular palaces all over the country. A very famous tourist spot that sees thousands of visitors milling in and around it every day, the Mysore Palace is renowned for its architecture, design, artisanship and ancient upholstery. A mesmerizing example of Indo-Saracenic architecture, every inch of the palace drips with opulence and intricate details, and every room that you visit stands out in terms of its elaborate architecture, beautiful paintings, rich colours and stained-glass windows. On every Sunday, and during the Dussehra celebrations, the palace is spectacularly lit up once dusk falls.
');
INSERT INTO "places" VALUES ('badami','15.9186°','75.6761°','BSh','tamil,kannada,konkani','Located in a valley of rugged red sandstone, surrounding the Agastya Lake, Badami (formerly known as Vatapi) is an archaeological delight owing to its beautifully crafted sandstone cave temples, fortresses and carvings.

Once the royal capital of the Chalukyas, Badami continues to enjoy a unique place, being the home to a number of examples of Dravidian architecture which sustains and enhances instances of both south and north Indian style of architecture. There are three Hindu Temples and one Jain Temple in Badami Caves.
');
INSERT INTO "places" VALUES ('chikmagalur','13.3161°','75.7720°','moderate to cool','kannada','Famously known as the ‘Coffee Land of Karnataka’, Chikmagalur is situated in the foothills of the Mullayangiri Range in Karnataka and stands at an altitude of 3400 feet. If you love the aroma of freshly brewed coffee in the mornings, you are going to love Chikmagalur, which has a perpetual fragrance of coffee lingering in the air. Famous for its tall mountains, lush green forests and its tranquil environment (apart from its coffee production), Chikmagalur is a very popular tourist destination and is a quaint getaway from the busy life of the city.');
INSERT INTO "places" VALUES ('kabini','12.52295','76.9384','hot ','kannada','Once a private hunting area for the British, this famous wildlife destination has a rich variety of flora and fauna making it a gorgeous tourist spot.

One of the best wildlife sanctuaries in Karnataka, the Kabini Wildlife Sanctuary was once a private hunting area for the British. Today, it attracts tourists from all over. It is a must see for all nature lovers and those looking for a perfect vacation amidst the lush greenery and imposing waterfalls. Kabini has in store hints of various elements of nature, be it a huge variety in the plantation, abundance of wildlife ranging from carnivores to mammals to birds or the terrain where each type is a part of and a compliment to the other.
');
INSERT INTO "places" VALUES ('jog falls','14.2004°','74.7922°','cool','Joga jalapatha ',' The second-highest plunge waterfall of India, Jog Falls is a major tourist attraction in Karnataka. Located on the border of Shimoga and Uttara Kannada districts of Karnataka, Jog waterfalls is the highest waterfall in the state.

Also known as Gerosappa Falls or the Joga Falls, these falls are one of the most important attractions in all of South India. Second, only to the Nohkalikai Falls of Meghalaya, Jog falls drops about a huge 253 m (850 ft. ) in a single fall. However, due to the construction of Linganamakki Dam, the flow in the falls is hugely restricted before monsoons.');
INSERT INTO "places" VALUES ('murudeshwar','14.0940°','74.4899°','hot and humid','tulu','With its major attraction as the huge Shiva temple, Murudeshwar is a religious site which also serves as the connecting point for popular scuba diving destination Netrani.

Murudeshwar is home to the second tallest statue of Lord Shiva in the world. With the shimmering Arabian Sea on three sides and the magnificent Western Ghats imposing their presence on this town, it is a favourite picnic spot for the folks from Kerala and Karnataka. The beaches and the adventure activities around Netrani island are major attractions for the tourists. The temple and fort are also the most visited spots, captivating one with their rustic charm and beauty. Nearby Netrani island is also a very popular spot for tourists as it offers excellent snorkelling and scuba diving opportunities. The Murudeshwar beach, however, has become a little overcrowded and dirty due to human intervention and could be avoided.
');
INSERT INTO "places" VALUES ('udupi','13.3409°','74.7421°','pleasant in winter','tulu',' Udupi is a coastal town in Karnataka, most famous for its vegetarian cuisine and South Indian restaurants all over the country. With carefully carved temples, laidback beaches and unexplored forests, Udupi is also the place where the educational hub of Manipal is located. Situated 60 km. from Mangalore, Udupi is famous for its culture.

Surrounded by the Arabian Sea on one side and the Western ghats on the other, this pilgrim centre is the most important city in Karnataka after Bangalore and Mangalore. Being a pilgrim centre, one of the most important attractions here is the Krishna Temple. Udupi is also known as Rajata Peetha and Shivalli locally.');
INSERT INTO "places" VALUES ('shravanabelagola','12.8519°','76.4807°','tropical','kannada',' Sravanbelagola is an important Jain pilgrimage centre with a 57 m tall monolithic sculpture of Lord Gomateswara called Bahubali statue as its prime attraction. Located 144 km from Bengaluru in Hassan District of Karnataka, the collection of Jain Temples in Sravanbelagola attracts a number of pilgrims every year.

Wedged between Chandigiri and Vindyagiri hills on the side of the tank of town called ''Belagola''. ''Bela'' means white and ''kola'' means the pond in Kannada. It takes a full day to visit all the monuments. For those who find it difficult to climb the hill, Dolis or Palanquin are available of INR 800 to and fro. Every 12 years, Mahamasthabhisheka of Lord Bahubali is performed as a part of Jain culture.
');
INSERT INTO "places" VALUES ('pattadakal
','15.9488°','75.8164°','very hot','kannada,telugu,tulu','Pattadakal is a tiny village, also known as Raktapura or Pattadakallu, houses a series of ten magnificent stone temples which date back to the 7th and 8th century. Out of these ten, nine are Hindu temples and one is a Jain temple. Lying close to the Badami and Aihole centres of Chalukya monuments, it is a protected site, managed by ASI (Archaeological Survey of India).
These grand, imposing structures were inscribed as UNESCO World Heritage Site in 1987. All ten temples are majestic in their sheer size and detailed architecture, reflective of a blend of North Indian Nagara and South Indian Dravidian construction styles. Lying alongside the Malaprabha river, they have aptly earned the epithet “cradle of Indian temple architecture”. The friezes on temple walls depict stories from various Hindu scriptures and tales, such as Mahabharata, Ramayana, Bhagavata Purana, Panchatantra, and Kir?t?rjun?ya.');
INSERT INTO "places" VALUES ('devbagh','16.0212°','73.5182° ','tropical and heavy rain','kannada','Pristine blue water, picture perfect backdrop of beautiful mountains and lush green belt of casuarinas trees blend together perfectly to give you a destination not to be missed i.e. Devbagh.

It is an amazing exotic island with all kinds of elements clubbed together. Lying along the coastline of Arabian Sea about 2 kms from the southern part of Goa, Devbagh is a spot for endless strolls along the sand, a place to embrace the beauty of nature and a getaway to lose oneself in the entrancing ambiance of Devbagh. With splendid weather throughout the year, the beach town is famous for its sunset and sunrise, fresh seafood and romantic setting being secluded from the hustle bustle of the mainland. A beautiful picturesque island, Devbagh is a perfect destination for all kind of vacation makers oozing a rustic charm. The place is a splendor, a blessing in disguise and should not be missed.
');
INSERT INTO "places" VALUES ('nagarhole','12.0314°','76.1207°','tropical','kannada,english,hindi','Nagarhole is southern storehouse of rich flora and fauna and is host to Nagarhole national park, celebrated as one of the best wildlife parks as well as the Bandipur bird sanctuary.

Nagarhole dominated by its splendid display of nature''s offerings can provide you with a complete tourist experience coming full circle with a number of temples and other elements of culture. When you are not busy spotting Asiatic elephants, Indian Bisons or beautiful birds around the place, you can witness your breath being taken away by the waterfalls in the area. Nagarhole means ''snake river'' and derives its name from the unforgiving wild nature of the river that flows through the forests.
');
INSERT INTO "places" VALUES ('halebidu','13.2130°','75.9942°','tropical and less rainfall','kannada',' Halebid (or Halebidu) is a city located in the Hassan district of Karnataka state. Formerly known as Dwarasamudra, Halebid is a city with adorned with a beautiful collection of temples, shrines and sculptures. It is also known as the Gem of Indian architecture owing to its sterling Hoysala architecture, its magnificent temple complexes and some stunning Jain sites. Once the majestic capital of the Hoysala empire, the city is in ruins now.
A little stuck in history, Halebid can be a great showcase of culture, architecture and imprints of certain significant events of the past. Halebid was the imperial capital of the great Hoysala Empire during the 12th and 13th century. It is home to the distinguished Hoyaleswara and Kedareshwara temples and famous for its sculptures and panels designed in the prominent Hoysala style. ');
INSERT INTO "places" VALUES ('dandeli','15.2361°','74.6173°','Aw and tropical ','kannada','Located in Uttara Kannada District of Karnataka, Dandeli is bestowed with the lush green forests and lies on the banks of the Kali river. 

Dandeli can be the ideal spot for river rafting. One can indulge in maximum excitement given the numerous options such as mountain biking, trekking, cycling, kayaking and canoeing. The Dandeli Wildlife Sanctuary is another element of excitement that the place has to offer where one can spot Bisons and Black Panthers.
');
INSERT INTO "places" VALUES ('bijapur','16.8302°','75.7100°','moderate','kannada','Famous for the Gol Gumbaj and other monuments of historical heritage, Bijapur is a tourist destination in Karnataka that makes the visitors travel back in time.

Bijapur is an important commercial district in the state of Karnataka. Built around the 10th-11th century by the Kalyani Chalukyas, Bijapur was known as Vijayapura in those times. Vijaypura literally means the City of Victory. Ibrahim Rauza is another important monument of Bijapur and is also known as the Taj Mahal of the Deccan. Among other important attractions, there are various mosques including Jumma Masjid, palaces citadels.
');
INSERT INTO "places" VALUES ('kudremukh','13.2226° ','75.2508°','monsoon','kannada','With the promise of a picturesque view of a mountain in the shape of a horse face, Kudremukh is famous for its biodiversity and scenic beauty.
A popular hill-station among the Bangalore crowd, Kudremukh is actually a hill range in the Chikmagalurdistrict of Karnataka. With its rolling meadows, grasslands and dense forests, this place is a bio-diversity hotspot. Kudremukh is an enchanting place to visit, still retaining much of its natural beauty despite persistent threats from various sources to its ecology. At an altitude of 1894 m above sea level, the Kudremukh Peak is a paradise for trekkers and naturists alike, with its mountainous paths and floral and faunal diversity. Varaha Parvatha, another mountain range nearby at a height of 1458m above sea level is a part of the UNESCO World Heritage Site.
');
INSERT INTO "places" VALUES ('nandi hills','13.3702°','77.6835°','cool climate','kannada','It is often said that ''the best places are off the beaten path'', and Nandi Hills is a clear testimony to that. Located around 60 kilometres away from Bangalore, Nandi Hills is one such tourist spot that has gradually been discovered by visitors over the years, and has now become a well-known weekend getaway. Situated at a height of 4851 feet above sea level, you can see convoy of weekenders from Bangalore during early hours catching the glimpse of sunrise.');
INSERT INTO "places" VALUES ('kemmanagundi','13.5500°',' 75.7500°','pleasant climate','kannada','A hill-station of widespread views and scents of beautiful gardens, Kemmanagundi or KR hills, homes the tallest peak of Karnataka, Mullayanagiri');
INSERT INTO "places" VALUES ('shivagange','13.1681°',' 77.2222°','local steppe climate','kannada','combination of temples and scenic beauty that makes it both a pilgrimage as well as an adventure spot,hill rock looks like shiva linga');
INSERT INTO "places" VALUES ('maravanthe','13.7258°','74.6488°','mildly warm to stiflingly hot','tulu,kannada','major attraction is the Virgin Beach characterised by white sands and spectacular sunsets');
INSERT INTO "places" VALUES ('mangalore','12.9141°','74.8560°','heavy monsoon rainfall','kannada','known for its swaying coconut palms, beautiful beaches and temple architecture');
INSERT INTO "places" VALUES ('savandurga','12.9206°','77.2944° ','moderate','kannada,hindi','considered to be one of the largest single rock formations in the whole of Asia,provides the opportunity for rock climbing');
INSERT INTO "places" VALUES ('chikballapur','13.4355°','77.7315°','tropical','kannada','an important port link in North Bangalore area and an educational hub');
INSERT INTO "places" VALUES ('srirangapatna','12.4237°','76.6829°','BSh','kannada,telugu','an egg-shaped island town,most important Vaishnavite centres of pilgrimage- the Ranganathaswamy temple, is the major attraction');
INSERT INTO "places" VALUES ('shimoga','13.9299°','75.5681°',' tropical wet and dry','kannada','main city of Shimoga District derives its name from the words ''Shiv-Mukha'' implying ''Face of Lord Shiva');
INSERT INTO "places" VALUES ('honnemaradu','14.1789°','74.8756°','hot ','kannada',' deserted village is like a live amusement park,the only attraction is the water sports done at the Honnemaradu lake');
INSERT INTO "places" VALUES ('Hassan','12.1212','12.1212','hot','kannada','andiasnasnixu isdc jhdcbc  duhc wcjwdc wjwcjh');
COMMIT;
