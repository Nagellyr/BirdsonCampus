birds = {
  "1": {
    "id": "1",
    "title": "Common Pigeon",
    "image": "https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/1491/2024/07/01121157/The-Rock-Dove-e1719850353334.png",
    "summary": "Common pigeons, also known as Rock Pigeons, are urban survivors.They are often seen strutting in open areas or pecking at crumbs. They're  familiar around campus and are unafraid of humans. Their iridescent neck feathers shimmer green and purple in the sun. Flocks of them often gather around food spots and can be heard with a gentle cooing sound.",
    "identifying_traits": ["Gray feathers", "Iridescent neck", "Red feet"],
    "wingspan_cm": 67,
    "locations": ["College Walk", "South Entrance", "Morningside Park", "Central Park", "Riverside Park"],
    "popular":True
  },
  "2": {
    "id": "2",
    "title": "House Sparrow",
    "image": "https://www.allaboutbirds.org/guide/assets/photo/305880301-1280px.jpg",
    "summary": "These small, noisy birds love busy areas. Males have a black bib and gray crown, while females are light brown throughout. House sparrows nest in ledges and crevices and gather in groups near food. They're especially common under outdoor seating areas.",
    "identifying_traits": ["Brown body", "Black throat (males)", "Short beak"],
    "wingspan_cm": 22,
    "locations": ["College Walk", "South Entrance", "Morningside Park", "Central Park", "Riverside Park"],
    "popular":True
  },
  "3": {
    "id": "3",
    "title": "American Robin",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/American_robin_%2871307%29.jpg/500px-American_robin_%2871307%29.jpg",
    "summary": "A common sign of spring, robins are known for their cheerful morning call and bright orange chest. They hop around lawns looking for worms. They're one of the most recognizable birds on campus and often perch in trees or forage on the grass in the early morning.",
    "identifying_traits": ["Red-orange belly", "Gray back", "Yellow beak"],
    "wingspan_cm": 36,
    "locations": ["Butler Lawn", "College Walk"],
    "popular":True
  },
  "4": {
    "id": "4",
    "title": "Mourning Dove",
    "image": "https://www.outdooralabama.com/sites/default/files/Wildlife/Birds/MourningDove-USFWS.jpg",
    "summary": "Softly cooing and often overlooked, these doves perch on wires or forage for seeds on the ground. Their pointed tails and soft gray-brown color make them easy to identify. They fly off in fast, darting movements.",
    "identifying_traits": ["Gray-pink body", "Pointed tail", "Soft cooing"],
    "wingspan_cm": 48,
    "locations": ["South Lawn", "College Walk"]
    
  },
  "5": {
    "id": "5",
    "title": "Red-winged Blackbird",
    "image": "https://indianaaudubon.org/wp-content/uploads/2016/04/RedWingedBlackbird2.jpg",
    "summary": "These birds are mostly black but have a brilliant red-and-yellow patch on each wing. Males are more vivid than females. They often nest in marshy or grassy areas. You might hear their conk-la-reee call before you see them.",
    "identifying_traits": ["Black body", "Red/yellow wing patch", "Pointed beak"],
    "wingspan_cm": 35,
    "locations": ["Riverside Park", "Morningside Park"]
  },
  "6": {
    "id": "6",
    "title": "Common Starling",
    "image": "https://www.allaboutbirds.org/guide/assets/photo/303928891-720px.jpg",
    "summary": "These glossy, dark birds have a speckled pattern and often gather in noisy, swirling flocks. In sunlight, their feathers shine purple and green. They can mimic other birds and sounds. They're often seen on fences or high ledges.",
    "identifying_traits": ["Speckled feathers", "Glossy black body", "Short tail","Yellow Beak"],
    "wingspan_cm": 38,
    "locations": ["Riverside Park", "South Entrance"],
    "popular":True
  },
  "7": {
    "id": "7",
    "title": "Song Sparrow",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Song_sparrow_in_Prospect_Park_%2893031%29.jpg/500px-Song_sparrow_in_Prospect_Park_%2893031%29.jpg",
    "summary": "This small bird has a streaked breast and a melodious song. They’re often seen perching low in shrubs or hopping along the ground. While they may look plain at first glance, their varied song is distinctive and sweet.",
    "identifying_traits": ["Brown streaked breast", "Long tail", "Melodious song"],
    "wingspan_cm": 22,
    "locations": ["East Campus", "Butler Lawn"]
  },

  "8": {
    "id": "8",
    "title": "Snowy Owl",
    "image": "https://images.foxtv.com/static.fox5ny.com/www.fox5ny.com/content/uploads/2025/01/932/524/untitled-40.png?ve=1&tl=1",
    "summary": "Rare on campus, but spotted a few winters ago perched on Low Steps. Snowy owls are large, mostly white, and active during the day. They migrate from the Arctic during harsh winters. Their appearance usually draws birders and photographers.",
    "identifying_traits": ["White feathers", "Golden eyes", "Thick body"],
    "wingspan_cm": 138,
    "locations": ["Low Steps"]
   
  }
}
def get_all_birds():
    return birds

def get_bird_by_id(bird_id):
    return birds.get(bird_id)

    
def get_popular_birds():
    return [bird for bird in birds.values() if bird.get("popular")]



def get_quiz_questions():
    return [
        {
            "name": "q1",
            "question": "Which bird is known for its red breast and early morning song?",
            "options": ["Common Starling", "House Sparrow", "American Robin", "Common Pigeon"],
            "answer": "American Robin"
        },
        {
            "name": "q2",
            "question": "Which bird is commonly found in cities and known for cooing sounds?",
            "options": ["House Sparrow", "Common Starling", "Common Pigeon", "American Robin"],
            "answer": "Common Pigeon"
        },
        {
            "name": "q3",
            "question": "Which bird is small, brown, and often nests in buildings?",
            "options": ["Common Starling", "American Robin", "House Sparrow", "Common Pigeon"],
            "answer": "House Sparrow"
        },
        {
            "name": "q4",
            "question": "Which bird has iridescent feathers and forms large noisy flocks?",
            "options": ["Common Starling", "House Sparrow", "Common Pigeon", "American Robin"],
            "answer": "Common Starling"
        },
        {
            "name": "q5",
            "question": "Drag each bird name to the correct photo.",
            "type":"drag-match",
            "correct_map":{
              "pigeon": "pigeon",
              "sparrow": "sparrow",
              "robin": "robin",
              "starling": "starling"
            },
            "options":[
              {
                "label": "Common Pigeon",
                "value": "pigeon",
                "image": "https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/1491/2024/07/01121157/The-Rock-Dove-e1719850353334.png"
              },
              {
                 "label": "House Sparrow",
                 "value": "sparrow",
                 "image": "https://www.allaboutbirds.org/guide/assets/photo/305880301-1280px.jpg"
              },
              {
                "label": "American Robin",
                "value": "robin",
                "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/American_robin_%2871307%29.jpg/500px-American_robin_%2871307%29.jpg"

              },
              {
                "label": "Common Starling",
                "value": "starling",
                "image": "https://www.allaboutbirds.org/guide/assets/photo/303928891-720px.jpg"
            }
            ]
        },
        
    ]
