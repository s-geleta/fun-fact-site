from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

fun_facts = [
    "Water can boil and freeze at the same time: This phenomenon, known as the triple point, occurs under specific conditions of temperature and pressure.",
    "Octopuses have three hearts: Two pump blood to the gills, while the third pumps it to the rest of the body.",
    "Bananas are berries, but strawberries aren’t: Botanically speaking, bananas qualify as berries, but strawberries do not because their seeds are on the outside.",
    "Honey never spoils: Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible. Honey’s longevity is due to its low moisture content and acidic pH, which create an inhospitable environment for bacteria and microorganisms.",
    "The mantis shrimp can throw the fastest punch in the natural world: It can strike with its claws at a speed of 50 miles per hour, delivering a force of over 1,500 newtons, enough to shatter glass and even create underwater shockwaves.",
    "Plants communicate using an underground network: Often referred to as the “Wood Wide Web,” plants use a network of fungi called mycorrhizae to communicate and share resources, such as warning neighbors about insect attacks or sharing nutrients.",
    "Birds are the living descendants of dinosaurs: Specifically, birds are considered to be modern-day theropods, a group of dinosaurs that includes the mighty Tyrannosaurus rex, making them the only surviving dinosaurs.",
    "The Pistol Shrimp can create a bubble hot as the sun: When it snaps its claw shut at high speed, it creates a bubble that reaches temperatures of over 4,700 degrees Celsius (nearly the temperature of the sun’s surface) for a brief moment, producing a loud popping noise and a flash of light.",
    "Butterflies taste with their feet: Their taste sensors are located on their feet, allowing them to taste their food by standing on it, helping them find food and the right plants on which to lay their eggs.",
    "A single teaspoon of neutron star would weigh about 6 billion tons: Neutron stars are the remnants of supernova explosions and are incredibly dense, with just a sugar-cube-sized amount of material weighing as much as all of humanity.",
    "Venus rotates in the opposite direction to most planets: This means the Sun rises in the west and sets in the east on Venus.",
    "A day on Venus is longer than a year on Venus: Venus takes about 243 Earth days to rotate once but only about 225 Earth days to orbit the Sun.",
    "There are more trees on Earth than stars in the Milky Way: Estimates suggest there are around 3 trillion trees on Earth and 100-400 billion stars in the Milky Way.",
    "Mercury and Venus are the only two planets in our solar system without moons: Every other planet has at least one moon, with Jupiter leading the count with 79 known moons.",
    "Neptune was the first planet to get its existence predicted by mathematical calculations before it was actually seen by a telescope. This discovery in the 19th century was a remarkable testament to the power of Newton’s laws of gravity.",
    "A year on Mercury is just 88 Earth days long: Despite its proximity to the Sun, Mercury has a very elongated orbit that allows it to complete its orbit in less than three Earth months.",
    "The largest volcano in the solar system is on Mars: Olympus Mons is about 13.6 miles (22 kilometers) high, which makes it nearly three times the height of Mount Everest, Earth’s tallest mountain above sea level.",
    "Saturn’s rings are made primarily of ice particles, with a smaller amount of rocky debris and dust. Despite their impressive appearance, the rings are only about 20 meters thick in some places.",
    "The temperature in the void of space is about 2.7 Kelvin (-270.45 Celsius or -454.81 Fahrenheit). This cold temperature is due to the cosmic microwave background radiation, which is a remnant from the Big Bang.",
    "The Hubble Space Telescope can see about 13.4 billion light-years away: This means it can observe objects in the universe as they were just 400 million years after the Big Bang, providing invaluable insights into the early universe.",
    "Vatican City is the smallest country in the world, measuring just 44 hectares (110 acres).",
    "Canada has the longest coastline of any country, stretching over 202,080 kilometers (125,567 miles).",
    "Russia is the largest country by land area, covering more than 17 million square kilometers (6.6 million square miles).",
    "Japan has over 6,800 islands.",
    "Australia is the only country that is also a continent.",
    "Brazil has the Amazon River, which is the largest river by volume.",
    "China has a single time zone across the entire country, despite its wide geographical spread.",
    "India is the world’s largest democracy.",
    "Indonesia is the country with the most active volcanoes.",
    "Monaco is the most densely populated country in the world.",
    "The Great Pyramid of Giza was the tallest man-made structure for over 3,800 years.",
    "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
    "The first computer programmer was Ada Lovelace, who wrote algorithms for Charles Babbage’s Analytical Engine in the mid-1800s.",
    "The wheel was invented more than 5,000 years ago",
    "The Roman Empire was the largest empire of the classical antiquity period, covering over 5 million square kilometers at its peak: It had a profound and lasting influence on the development of Western civilization.",
    "The first known use of the word “coffee” in English was in 1582, derived from the Dutch ‘koffie,’ which came from the Ottoman Turkish ‘kahve,’ which in turn was borrowed from the Arabic ‘qahwah’: The origin of coffee itself is thought to have been Ethiopia.",
    "The Great Wall of China is longer than previously thought: Recent surveys found that it stretches over 13,000 miles (21,000 kilometers) – far longer than earlier estimates of about 5,500 miles (8,850 kilometers).",
    "Leonardo da Vinci could write with one hand and draw with the other at the same time",
    "The first recorded Olympic Games took place in Olympia, Greece, in 776 B.C.: They were held every four years for over a millennium, until they were banned by Emperor Theodosius I in 393 A.D. for being a “pagan cult.”",
    "The concept of zero as a number was first used in India: The mathematical concept of zero significantly contributed to the development of mathematics and was later transmitted to the Arab world and then to Europe",
    "The first email was sent by Ray Tomlinson to himself in 1971.",
    "The Internet carries over 4.66 billion web pages as of my last update.",
    "The 90 percent of the world’s currency exists only in digital form.",
    "The first smartphone was IBM’s Simon, introduced in 1994: It combined a mobile phone with features of a PDA.",
    "The World Wide Web was invented by Tim Berners-Lee in 1989: He also introduced the first web browser in 1990.",
    "The first successful human genome sequencing was completed in 2003, as part of the Human Genome Project, at a cost of nearly $3 billion. Today, it can be done for a few hundred dollars.",
    "Bitcoin, the first decentralized cryptocurrency, was created by an anonymous person or group of people using the name Satoshi Nakamoto in 2009.",
    "The first computer mouse was invented by Douglas Engelbart in 1964: It was made of wood and had one button.",
    "Google was originally called “Backrub”: It was renamed Google in 1997, a play on the mathematical term “googol,” representing a 1 followed by 100 zeros.",
    "The QR code (Quick Response Code) was first developed in 1994 by Denso Wave, a Japanese company, for tracking automotive parts.",
    "The human body contains around 37.2 trillion cells.",
    "Stomach acid is strong enough to dissolve stainless steel.",
    "Your heart beats over 100,000 times a day.",
    "Humans shed about 600,000 particles of skin every hour.",
    "The average human adult has 206 bones.",
    "Human saliva contains a painkiller called opiorphin that is six times more powerful than morphine.",
    "The human liver can regenerate itself; as little as 25 percent of a liver can grow back to its full size.",








]


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/funfact', methods=['GET'])
def get_fun_fact():
    fact_of_the_day = random.choice(fun_facts)
    return jsonify(fact=fact_of_the_day)

if __name__ == '__main__':
    app.run(debug=True)