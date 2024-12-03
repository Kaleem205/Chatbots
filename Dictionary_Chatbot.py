# !pip install rapidfuzz


# random ko import is lia karaya ha taka jo functions ha
# i am using this mainly in selecting responses for conversations
# using random.choice in the handle_converstaions
import random

#splits (tokens ) or we can say string into list of words or tokens
from nltk.tokenize import word_tokenize

# fuzz provides tools to compute similarity scores between strings, helping to determine how closely two strings match.
from rapidfuzz import fuzz
# natural language tool kitt for functions or we can some build in functions
import nltk

# Preload NLTK resources
nltk.download('punkt_tab')
nltk.download('punkt')

# Separate dictionaries for each product category
shirts_data = {
    "Basic shirt": {
        "price": "$20",
        "colors": ["red", "blue", "green"],
        "quality": "High",
        "in_stock": True
    },
    "Polo shirt": {
        "price": "$25",
        "colors": ["white", "navy blue", "gray"],
        "quality": "Comfortable",
        "in_stock": False
    },
    "Formal shirt": {
        "price": "$35",
        "colors": ["white", "blue", "pink"],
        "quality": "Elegant",
        "in_stock": True
    },
    "Graphic Tee shirt": {
        "price": "$18",
        "colors": ["black", "white", "yellow"],
        "quality": "Trendy",
        "in_stock": False
    },
    "Casual shirt": {
        "price": "$22",
        "colors": ["light gray", "olive", "beige"],
        "quality": "Casual",
        "in_stock": True
    },
    "Sweatshirt": {
        "price": "$30",
        "colors": ["red", "black", "gray"],
        "quality": "Cozy",
        "in_stock": True
    },
    "Denim shirt": {
        "price": "$28",
        "colors": ["blue", "black", "light blue"],
        "quality": "Durable",
        "in_stock": True
    },
    "Hawaiian shirt": {
        "price": "$40",
        "colors": ["blue", "green", "yellow"],
        "quality": "Lightweight",
        "in_stock": False
    },
    "Chambray shirt": {
        "price": "$32",
        "colors": ["light blue", "dark blue"],
        "quality": "Breathable",
        "in_stock": True
    },
    "Turtleneck shirt": {
        "price": "$36",
        "colors": ["black", "gray", "navy"],
        "quality": "Warm",
        "in_stock": True
    },
    "Flannel shirt": {
        "price": "$38",
        "colors": ["red", "green", "blue"],
        "quality": "Soft",
        "in_stock": False
    },
    "Tank top": {
        "price": "$15",
        "colors": ["white", "black", "red"],
        "quality": "Breathable",
        "in_stock": True
    },
    "Long sleeve shirt": {
        "price": "$25",
        "colors": ["white", "black", "green"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "Button-up shirt": {
        "price": "$30",
        "colors": ["white", "blue", "gray"],
        "quality": "Formal",
        "in_stock": True
    },
    "Linen shirt": {
        "price": "$28",
        "colors": ["beige", "light gray", "navy"],
        "quality": "Lightweight",
        "in_stock": True
    },
    "Hoodie shirt": {
        "price": "$35",
        "colors": ["black", "gray", "blue"],
        "quality": "Casual",
        "in_stock": True
    },
    "V-neck shirt": {
        "price": "$22",
        "colors": ["white", "red", "black"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "Houndstooth shirt": {
        "price": "$40",
        "colors": ["black", "white", "gray"],
        "quality": "Stylish",
        "in_stock": False
    },
    "Rugby shirt": {
        "price": "$45",
        "colors": ["green", "yellow", "blue"],
        "quality": "Sporty",
        "in_stock": True
    },
    "Plaid shirt": {
        "price": "$28",
        "colors": ["red", "blue", "black"],
        "quality": "Casual",
        "in_stock": True
    },
    "Dress shirt": {
        "price": "$50",
        "colors": ["white", "gray", "blue"],
        "quality": "Elegant",
        "in_stock": True
    },
    "Button-up shirt": {
        "price": "$30",
        "colors": ["blue", "white", "black"],
        "quality": "Smart",
        "in_stock": True
    },
    "Linen shirt": {
        "price": "$50",
        "colors": ["beige", "light blue", "white"],
        "quality": "Lightweight",
        "in_stock": True
    },
    "Muscle tank": {
        "price": "$18",
        "colors": ["black", "gray", "green"],
        "quality": "Stretchy",
        "in_stock": True
    },
    "V-neck shirt": {
        "price": "$20",
        "colors": ["white", "red", "navy blue"],
        "quality": "Casual",
        "in_stock": True
    },
    "Hoodie": {
        "price": "$40",
        "colors": ["black", "gray", "navy"],
        "quality": "Warm",
        "in_stock": False
    },
    "Fleece shirt": {
        "price": "$38",
        "colors": ["blue", "green", "gray"],
        "quality": "Cozy",
        "in_stock": True
    },
    "Work shirt": {
        "price": "$45",
        "colors": ["gray", "black", "navy"],
        "quality": "Durable",
        "in_stock": True
    },
    "Plaid shirt": {
        "price": "$30",
        "colors": ["red", "black", "yellow"],
        "quality": "Stylish",
        "in_stock": True
    },
    "Summer shirt": {
        "price": "$28",
        "colors": ["light yellow", "green", "blue"],
        "quality": "Lightweight",
        "in_stock": True
    },
    "T-shirt": {
        "price": "$12",
        "colors": ["white", "black", "blue"],
        "quality": "Basic",
        "in_stock": True
    },
    "Performance shirt": {
        "price": "$32",
        "colors": ["gray", "red", "navy"],
        "quality": "Breathable",
        "in_stock": True
    },
    "Workwear shirt": {
        "price": "$50",
        "colors": ["brown", "gray", "black"],
        "quality": "Heavy-duty",
        "in_stock": True
    },
    "Striped shirt": {
        "price": "$35",
        "colors": ["blue", "white", "black"],
        "quality": "Elegant",
        "in_stock": False
    },
    "Camo shirt": {
        "price": "$30",
        "colors": ["green", "brown", "gray"],
        "quality": "Rugged",
        "in_stock": True
    },
    "Sweater shirt": {
        "price": "$40",
        "colors": ["cream", "gray", "navy"],
        "quality": "Warm",
        "in_stock": True
    },
    "Batik shirt": {
        "price": "$45",
        "colors": ["brown", "blue", "green"],
        "quality": "Stylish",
        "in_stock": True
    },
    "Terry cloth shirt": {
        "price": "$35",
        "colors": ["light blue", "pink", "green"],
        "quality": "Soft",
        "in_stock": False
    },
    "Athletic shirt": {
        "price": "$22",
        "colors": ["black", "red", "gray"],
        "quality": "Stretchy",
        "in_stock": True
    },
    "Checked shirt": {
        "price": "$30",
        "colors": ["blue", "red", "black"],
        "quality": "Classic",
        "in_stock": True
    },
    "Cargo shirt": {
        "price": "$40",
        "colors": ["green", "gray", "brown"],
        "quality": "Durable",
        "in_stock": True
    },
    "Satin shirt": {
        "price": "$45",
        "colors": ["black", "silver", "gold"],
        "quality": "Luxurious",
        "in_stock": True
    },
    "Peasant shirt": {
        "price": "$38",
        "colors": ["white", "red", "blue"],
        "quality": "Bohemian",
        "in_stock": True
    },
    "Hooded shirt": {
        "price": "$50",
        "colors": ["black", "charcoal", "navy"],
        "quality": "Warm",
        "in_stock": False
    },
    "Rugby shirt": {
        "price": "$30",
        "colors": ["green", "blue", "yellow"],
        "quality": "Sporty",
        "in_stock": True
    },
    "Tie-dye shirt": {
        "price": "$25",
        "colors": ["pink", "purple", "yellow"],
        "quality": "Trendy",
        "in_stock": True
    },
    "Batik shirt": {
        "price": "$45",
        "colors": ["red", "yellow", "brown"],
        "quality": "Artisan",
        "in_stock": True
    },
    "Patchwork shirt": {
        "price": "$42",
        "colors": ["multicolor", "blue", "red"],
        "quality": "Creative",
        "in_stock": False
    },
    "Thermal shirt": {
        "price": "$35",
        "colors": ["black", "gray", "white"],
        "quality": "Insulating",
        "in_stock": True
    },
    "Tunic shirt": {
        "price": "$32",
        "colors": ["blue", "green", "beige"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "Puffer shirt": {
        "price": "$60",
        "colors": ["black", "white", "red"],
        "quality": "Warm",
        "in_stock": False
    },
    "Mesh shirt": {
        "price": "$28",
        "colors": ["black", "white", "neon green"],
        "quality": "Breathable",
        "in_stock": True
    },
    "Cowl neck shirt": {
        "price": "$38",
        "colors": ["gray", "black", "burgundy"],
        "quality": "Cozy",
        "in_stock": True
    },
    "Baseball shirt": {
        "price": "$20",
        "colors": ["white", "gray", "red"],
        "quality": "Sporty",
        "in_stock": True
    },
    "Sherpa shirt": {
        "price": "$55",
        "colors": ["brown", "cream", "black"],
        "quality": "Warm",
        "in_stock": True
    },
    "Asymmetrical shirt": {
        "price": "$40",
        "colors": ["black", "red", "gray"],
        "quality": "Fashionable",
        "in_stock": True
    },
    "Knit shirt": {
        "price": "$35",
        "colors": ["gray", "blue", "light pink"],
        "quality": "Soft",
        "in_stock": True
    },
    "Oversized shirt": {
        "price": "$50",
        "colors": ["navy", "gray", "olive"],
        "quality": "Relaxed",
        "in_stock": True
    },
    "Sweater shirt": {
        "price": "$60",
        "colors": ["blue", "white", "green"],
        "quality": "Warm",
        "in_stock": False
    },
      "Baseball shirt": {
        "price": "$30",
        "colors": ["white", "red", "blue"],
        "quality": "Sporty",
        "in_stock": True
    },
    "Blouse shirt": {
        "price": "$35",
        "colors": ["white", "cream", "pink"],
        "quality": "Elegant",
        "in_stock": True
    },
    "Over-sized shirt": {
        "price": "$40",
        "colors": ["gray", "black", "white"],
        "quality": "Casual",
        "in_stock": True
    },
    "Skater shirt": {
        "price": "$28",
        "colors": ["black", "red", "blue"],
        "quality": "Trendy",
        "in_stock": True
    },
    "Button-down shirt": {
        "price": "$38",
        "colors": ["blue", "white", "gray"],
        "quality": "Smart",
        "in_stock": True
    },
    "Athletic shirt": {
        "price": "$30",
        "colors": ["black", "neon green", "blue"],
        "quality": "Breathable",
        "in_stock": True
    },
    "Knit shirt": {
        "price": "$33",
        "colors": ["gray", "red", "beige"],
        "quality": "Stretchy",
        "in_stock": True
    },
    "Peacoat shirt": {
        "price": "$45",
        "colors": ["navy", "gray", "black"],
        "quality": "Warm",
        "in_stock": False
    },
    "Sweat-wicking shirt": {
        "price": "$35",
        "colors": ["blue", "black", "white"],
        "quality": "Functional",
        "in_stock": True
    },
    "Military shirt": {
        "price": "$38",
        "colors": ["green", "black", "tan"],
        "quality": "Tough",
        "in_stock": True
    },
    "Work shirt": {
        "price": "$42",
        "colors": ["brown", "black", "gray"],
        "quality": "Durable",
        "in_stock": True
    },
    "Yoga shirt": {
        "price": "$28",
        "colors": ["black", "purple", "white"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "Chino shirt": {
        "price": "$32",
        "colors": ["navy", "olive", "beige"],
        "quality": "Smart",
        "in_stock": True
    },
    "Rain jacket shirt": {
        "price": "$50",
        "colors": ["blue", "gray", "green"],
        "quality": "Waterproof",
        "in_stock": False
    },
    "Biker shirt": {
        "price": "$40",
        "colors": ["black", "gray", "red"],
        "quality": "Tough",
        "in_stock": True
    },
    "Luxe shirt": {
        "price": "$75",
        "colors": ["gold", "black", "white"],
        "quality": "Luxurious",
        "in_stock": True
    },
    "Sport tank": {
        "price": "$20",
        "colors": ["black", "gray", "red"],
        "quality": "Lightweight",
        "in_stock": True
    },
    "Denim vest shirt": {
        "price": "$48",
        "colors": ["blue", "black", "gray"],
        "quality": "Stylish",
        "in_stock": True
    },
    "Safari shirt": {
        "price": "$36",
        "colors": ["khaki", "green", "brown"],
        "quality": "Tactical",
        "in_stock": True
    },
    "Cargo short-sleeve shirt": {
        "price": "$32",
        "colors": ["black", "gray", "green"],
        "quality": "Functional",
        "in_stock": True
    },
    "Mock neck shirt": {
        "price": "$28",
        "colors": ["black", "red", "green"],
        "quality": "Warm",
        "in_stock": True
    },
    "Cropped shirt": {
        "price": "$25",
        "colors": ["black", "white", "gray"],
        "quality": "Trendy",
        "in_stock": True
    },
    "Plaid flannel shirt": {
        "price": "$34",
        "colors": ["red", "green", "blue"],
        "quality": "Soft",
        "in_stock": False
    },
    "Tie front shirt": {
        "price": "$30",
        "colors": ["blue", "white", "yellow"],
        "quality": "Stylish",
        "in_stock": True
    },
    "Belted shirt": {
        "price": "$40",
        "colors": ["gray", "black", "beige"],
        "quality": "Elegant",
        "in_stock": True
    },
    "Rain jacket shirt": {
        "price": "$50",
        "colors": ["black", "blue", "green"],
        "quality": "Water-resistant",
        "in_stock": True
    },
    "Shacket": {
        "price": "$45",
        "colors": ["gray", "navy", "burgundy"],
        "quality": "Warm",
        "in_stock": True
    },
    "Mock neck shirt": {
        "price": "$38",
        "colors": ["black", "gray", "white"],
        "quality": "Cozy",
        "in_stock": True
    },
    "Gingham shirt": {
        "price": "$32",
        "colors": ["red", "blue", "green"],
        "quality": "Preppy",
        "in_stock": True
    },
    "Henley shirt": {
        "price": "$28",
        "colors": ["black", "gray", "blue"],
        "quality": "Casual",
        "in_stock": True
    },
    "Cropped shirt": {
        "price": "$25",
        "colors": ["white", "pink", "yellow"],
        "quality": "Trendy",
        "in_stock": True
    },
    "Ski shirt": {
        "price": "$55",
        "colors": ["blue", "black", "green"],
        "quality": "Insulating",
        "in_stock": False
    },
    "Biker shirt": {
        "price": "$40",
        "colors": ["black", "gray", "red"],
        "quality": "Tough",
        "in_stock": True
    },
    "Sweater shirt": {
        "price": "$48",
        "colors": ["black", "gray", "beige"],
        "quality": "Warm",
        "in_stock": True
    },
    "Vests shirt": {
        "price": "$34",
        "colors": ["blue", "black", "red"],
        "quality": "Stylish",
        "in_stock": True
    }
}






pants_data = {
     "jeans pants": {
        "price": "$40",
        "colors": ["black", "blue"],
        "quality": "Premium",
        "in_stock": True
    },
    "dress pants": {
        "price": "$50",
        "colors": ["black", "gray", "navy"],
        "quality": "Professional",
        "in_stock": False
    },
    "cargo pants": {
        "price": "$40",
        "colors": ["olive", "black", "khaki"],
        "quality": "Durable",
        "in_stock": True
    },
    "chino pants": {
        "price": "$45",
        "colors": ["beige", "navy", "gray"],
        "quality": "Smart",
        "in_stock": True
    },
    "athletic pants": {
        "price": "$35",
        "colors": ["black", "gray", "blue"],
        "quality": "Stretchy",
        "in_stock": True
    },
    "track pants": {
        "price": "$25",
        "colors": ["black", "red", "blue"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "corduroy pants": {
        "price": "$60",
        "colors": ["brown", "gray", "blue"],
        "quality": "Warm",
        "in_stock": False
    },
    "denim pants": {
        "price": "$55",
        "colors": ["blue", "black", "gray"],
        "quality": "Durable",
        "in_stock": True
    },
    "work pants": {
        "price": "$50",
        "colors": ["brown", "black", "green"],
        "quality": "Heavy-duty",
        "in_stock": True
    },
    "flannel pants": {
        "price": "$48",
        "colors": ["red", "blue", "green"],
        "quality": "Soft",
        "in_stock": True
    },
    "sweatpants": {
        "price": "$30",
        "colors": ["gray", "black", "navy"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "leggings": {
        "price": "$25",
        "colors": ["black", "gray", "purple"],
        "quality": "Stretchy",
        "in_stock": True
    },
    "slim fit pants": {
        "price": "$55",
        "colors": ["black", "gray", "navy"],
        "quality": "Modern",
        "in_stock": True
    },
    "bootcut pants": {
        "price": "$50",
        "colors": ["blue", "black", "gray"],
        "quality": "Stylish",
        "in_stock": True
    },
    "cargo joggers": {
        "price": "$45",
        "colors": ["olive", "black", "gray"],
        "quality": "Casual",
        "in_stock": True
    },
    "skinny jeans": {
        "price": "$42",
        "colors": ["blue", "black", "gray"],
        "quality": "Slim",
        "in_stock": True
    },
    "harem pants": {
        "price": "$40",
        "colors": ["black", "beige", "gray"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "jogger pants": {
        "price": "$35",
        "colors": ["black", "blue", "gray"],
        "quality": "Sporty",
        "in_stock": True
    },
    "cargo shorts": {
        "price": "$30",
        "colors": ["khaki", "black", "green"],
        "quality": "Durable",
        "in_stock": True
    },
    "bermuda shorts": {
        "price": "$28",
        "colors": ["blue", "black", "beige"],
        "quality": "Casual",
        "in_stock": True
    },
    "palazzo pants": {
        "price": "$50",
        "colors": ["black", "blue", "red"],
        "quality": "Elegant",
        "in_stock": True
    },
    "capri pants": {
        "price": "$35",
        "colors": ["black", "navy", "white"],
        "quality": "Casual",
        "in_stock": True
    },
    "cargo capris": {
        "price": "$40",
        "colors": ["green", "black", "beige"],
        "quality": "Durable",
        "in_stock": True
    },
    "dress shorts": {
        "price": "$38",
        "colors": ["navy", "gray", "black"],
        "quality": "Smart",
        "in_stock": True
    },
    "thermal pants": {
        "price": "$45",
        "colors": ["black", "gray", "navy"],
        "quality": "Insulated",
        "in_stock": True
    },
    "twill pants": {
        "price": "$48",
        "colors": ["beige", "gray", "black"],
        "quality": "Smart",
        "in_stock": True
    },
    "jean shorts": {
        "price": "$30",
        "colors": ["blue", "black", "gray"],
        "quality": "Casual",
        "in_stock": True
    },
    "hiking pants": {
        "price": "$55",
        "colors": ["khaki", "green", "black"],
        "quality": "Durable",
        "in_stock": True
    },
    "snow pants": {
        "price": "$65",
        "colors": ["black", "blue", "red"],
        "quality": "Waterproof",
        "in_stock": False
    },
    "windbreaker pants": {
        "price": "$40",
        "colors": ["blue", "gray", "black"],
        "quality": "Lightweight",
        "in_stock": True
    },
     "wide-leg pants": {
        "price": "$40",
        "colors": ["black", "beige", "blue"],
        "quality": "Relaxed",
        "in_stock": True
    },
    "cargo shorts": {
        "price": "$30",
        "colors": ["olive", "tan", "black"],
        "quality": "Durable",
        "in_stock": True
    },
    "harem pants": {
        "price": "$38",
        "colors": ["purple", "black", "beige"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "pleated pants": {
        "price": "$45",
        "colors": ["gray", "navy", "black"],
        "quality": "Formal",
        "in_stock": True
    },
    "jogger pants": {
        "price": "$35",
        "colors": ["black", "gray", "olive"],
        "quality": "Sporty",
        "in_stock": True
    },
    "lounge pants": {
        "price": "$28",
        "colors": ["gray", "navy", "green"],
        "quality": "Relaxed",
        "in_stock": True
    },
    "palazzo pants": {
        "price": "$50",
        "colors": ["black", "navy", "brown"],
        "quality": "Flowy",
        "in_stock": False
    },
    "tactical pants": {
        "price": "$65",
        "colors": ["black", "green", "tan"],
        "quality": "Heavy-duty",
        "in_stock": True
    },
    "cycling pants": {
        "price": "$45",
        "colors": ["black", "neon green", "blue"],
        "quality": "Performance",
        "in_stock": True
    },
    "linen pants": {
        "price": "$50",
        "colors": ["white", "light blue", "beige"],
        "quality": "Lightweight",
        "in_stock": True
    },
    "wool pants": {
        "price": "$80",
        "colors": ["charcoal", "gray", "beige"],
        "quality": "Warm",
        "in_stock": False
    },
    "thermal pants": {
        "price": "$55",
        "colors": ["black", "gray", "navy"],
        "quality": "Insulating",
        "in_stock": True
    },
    "golf pants": {
        "price": "$60",
        "colors": ["khaki", "black", "gray"],
        "quality": "Sporty",
        "in_stock": True
    },
    "high-waisted pants": {
        "price": "$48",
        "colors": ["blue", "black", "gray"],
        "quality": "Trendy",
        "in_stock": True
    },
    "bootcut jeans": {
        "price": "$50",
        "colors": ["blue", "black", "light blue"],
        "quality": "Classic",
        "in_stock": True
    },
    "tuxedo pants": {
        "price": "$120",
        "colors": ["black", "navy"],
        "quality": "Formal",
        "in_stock": False
    },
    "maternity pants": {
        "price": "$40",
        "colors": ["black", "gray", "blue"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "stretch pants": {
        "price": "$30",
        "colors": ["black", "gray", "green"],
        "quality": "Flexible",
        "in_stock": True
    },
    "pleated shorts": {
        "price": "$25",
        "colors": ["gray", "blue", "black"],
        "quality": "Casual",
        "in_stock": True
    },
    "flared pants": {
        "price": "$55",
        "colors": ["red", "black", "blue"],
        "quality": "Vintage",
        "in_stock": True
    },
    "overalls pants": {
        "price": "$65",
        "colors": ["blue", "black", "green"],
        "quality": "Durable",
        "in_stock": True
    },
    "skinny jeans": {
        "price": "$50",
        "colors": ["black", "blue", "light blue"],
        "quality": "Slim",
        "in_stock": True
    },
    "retro pants": {
        "price": "$45",
        "colors": ["brown", "navy", "red"],
        "quality": "Vintage",
        "in_stock": True
    },
    "seamless pants": {
        "price": "$40",
        "colors": ["black", "gray", "navy"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "snow pants": {
        "price": "$90",
        "colors": ["black", "red", "blue"],
        "quality": "Insulating",
        "in_stock": False
    },
    "fleece-lined pants": {
        "price": "$70",
        "colors": ["gray", "blue", "black"],
        "quality": "Warm",
        "in_stock": True
    },
    "knee-length pants": {
        "price": "$35",
        "colors": ["navy", "black", "gray"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "combat pants": {
        "price": "$50",
        "colors": ["green", "black", "brown"],
        "quality": "Tough",
        "in_stock": True
    },
    "swim trunks": {
        "price": "$25",
        "colors": ["blue", "black", "green"],
        "quality": "Quick-dry",
        "in_stock": True
    },
    "tartan pants": {
        "price": "$55",
        "colors": ["red", "green", "black"],
        "quality": "Stylish",
        "in_stock": True
    },
    "business casual pants": {
        "price": "$60",
        "colors": ["beige", "navy", "black"],
        "quality": "Smart",
        "in_stock": True
    },
    "cargo joggers": {
        "price": "$50",
        "colors": ["gray", "black", "olive"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "swim shorts": {
        "price": "$20",
        "colors": ["blue", "yellow", "red"],
        "quality": "Quick-dry",
        "in_stock": True
    },
    "stretch leggings": {
        "price": "$30",
        "colors": ["black", "gray", "purple"],
        "quality": "Flexible",
        "in_stock": True
    },
    "fitted pants": {
        "price": "$40",
        "colors": ["navy", "black", "charcoal"],
        "quality": "Slim",
        "in_stock": True
    },
     "jumpsuit pants": {
        "price": "$60",
        "colors": ["black", "beige", "navy"],
        "quality": "Fashion-forward",
        "in_stock": True
    },
    "athleisure pants": {
        "price": "$40",
        "colors": ["black", "gray", "red"],
        "quality": "Comfortable",
        "in_stock": True
    },
    "stretch pants": {
        "price": "$30",
        "colors": ["black", "gray", "green"],
        "quality": "Flexible",
        "in_stock": True
    },
    "baggy pants": {
        "price": "$35",
        "colors": ["blue", "gray", "olive"],
        "quality": "Casual",
        "in_stock": True
    },
    "overalls": {
        "price": "$50",
        "colors": ["blue", "black", "green"],
        "quality": "Durable",
        "in_stock": True
    },
    "split-leg pants": {
        "price": "$45",
        "colors": ["black", "gray", "navy"],
        "quality": "Trendy",
        "in_stock": True
    },
    "suit pants": {
        "price": "$75",
        "colors": ["black", "gray", "navy"],
        "quality": "Formal",
        "in_stock": True
    },
    "waterproof pants": {
        "price": "$65",
        "colors": ["black", "gray", "olive"],
        "quality": "Water-resistant",
        "in_stock": True
    },
    "leggings with pockets": {
        "price": "$40",
        "colors": ["black", "purple", "red"],
        "quality": "Functional",
        "in_stock": True
    },
    "spandex pants": {
        "price": "$35",
        "colors": ["black", "pink", "blue"],
        "quality": "Stretchy",
        "in_stock": True
    },
    "shiny pants": {
        "price": "$50",
        "colors": ["black", "gold", "silver"],
        "quality": "Fashionable",
        "in_stock": True
    },
    "bootcut jeans": {
        "price": "$60",
        "colors": ["blue", "black", "light blue"],
        "quality": "Classic",
        "in_stock": True
    },
    "leather pants": {
        "price": "$90",
        "colors": ["black", "brown", "gray"],
        "quality": "Bold",
        "in_stock": True
    },
    "stretch chinos": {
        "price": "$50",
        "colors": ["beige", "olive", "gray"],
        "quality": "Flexible",
        "in_stock": True
    },
    "metallic pants": {
        "price": "$70",
        "colors": ["gold", "silver", "black"],
        "quality": "Eye-catching",
        "in_stock": False
    },
    "cargo leggings": {
        "price": "$40",
        "colors": ["olive", "black", "tan"],
        "quality": "Durable",
        "in_stock": True
    },
    "fleece pants": {
        "price": "$55",
        "colors": ["black", "gray", "green"],
        "quality": "Warm",
        "in_stock": True
    },
    "canvas pants": {
        "price": "$50",
        "colors": ["brown", "black", "gray"],
        "quality": "Tough",
        "in_stock": True
    },
    "track jogger pants": {
        "price": "$38",
        "colors": ["black", "red", "blue"],
        "quality": "Sporty",
        "in_stock": True
    },
    "silk pants": {
        "price": "$85",
        "colors": ["black", "cream", "gold"],
        "quality": "Luxurious",
        "in_stock": True
    },
    "dungarees": {
        "price": "$55",
        "colors": ["blue", "black", "green"],
        "quality": "Durable",
        "in_stock": True
    },
    "culotte pants": {
        "price": "$40",
        "colors": ["black", "gray", "brown"],
        "quality": "Stylish",
        "in_stock": True
    },
    "polka dot pants": {
        "price": "$45",
        "colors": ["black", "white", "blue"],
        "quality": "Fun",
        "in_stock": True
    },
    "sports pants": {
        "price": "$50",
        "colors": ["black", "gray", "navy"],
        "quality": "Activewear",
        "in_stock": True
    },
    "cargo joggers": {
        "price": "$42",
        "colors": ["black", "olive", "gray"],
        "quality": "Functional",
        "in_stock": True
    },
    "denim shorts": {
        "price": "$38",
        "colors": ["blue", "black", "gray"],
        "quality": "Casual",
        "in_stock": True
    },
    "track pants with stripes": {
        "price": "$45",
        "colors": ["black", "blue", "green"],
        "quality": "Sporty",
        "in_stock": True
    },
    "quilted pants": {
        "price": "$65",
        "colors": ["black", "gray", "navy"],
        "quality": "Warm",
        "in_stock": True
    },
    "stretch denim pants": {
        "price": "$55",
        "colors": ["blue", "black", "gray"],
        "quality": "Stretchable",
        "in_stock": True
    }
}

scarfs_data = {
    "Knitted scarf": {
        "price": "$25",
        "colors": ["gray", "black", "blue"],
        "quality": "Warm",
        "in_stock": True
    },
    "Silk scarf": {
        "price": "$40",
        "colors": ["red", "gold", "black"],
        "quality": "Elegant",
        "in_stock": False
    },
    "Wool scarf": {
        "price": "$30",
        "colors": ["white", "gray", "brown"],
        "quality": "Soft",
        "in_stock": True
    },
    "Cashmere scarf": {
        "price": "$80",
        "colors": ["beige", "black", "navy"],
        "quality": "Luxury",
        "in_stock": True
    },
    "Plaid scarf": {
        "price": "$35",
        "colors": ["red and black", "green and blue", "navy and white"],
        "quality": "Classic",
        "in_stock": True
    },
    "Infinity scarf": {
        "price": "$20",
        "colors": ["purple", "gray", "pink"],
        "quality": "Cozy",
        "in_stock": True
    },
    "Fringed scarf": {
        "price": "$28",
        "colors": ["brown", "gray", "beige"],
        "quality": "Trendy",
        "in_stock": False
    },
    "Fleece scarf": {
        "price": "$18",
        "colors": ["black", "red", "blue"],
        "quality": "Warm",
        "in_stock": True
    },
    "Houndstooth scarf": {
        "price": "$50",
        "colors": ["black and white", "brown and beige"],
        "quality": "Stylish",
        "in_stock": True
    },
    "Linen scarf": {
        "price": "$40",
        "colors": ["light blue", "ivory", "gray"],
        "quality": "Lightweight",
        "in_stock": True
    },
    "Vegan leather scarf": {
        "price": "$45",
        "colors": ["black", "brown", "burgundy"],
        "quality": "Chic",
        "in_stock": False
    },
    "Satin scarf": {
        "price": "$55",
        "colors": ["red", "navy", "gold"],
        "quality": "Luxurious",
        "in_stock": True
    },
    "Tartan scarf": {
        "price": "$30",
        "colors": ["red and green", "blue and yellow"],
        "quality": "Bold",
        "in_stock": True
    },
    "Embroidered scarf": {
        "price": "$60",
        "colors": ["white", "black", "pink"],
        "quality": "Detailed",
        "in_stock": False
    },
    "Cotton scarf": {
        "price": "$15",
        "colors": ["light blue", "cream", "yellow"],
        "quality": "Soft",
        "in_stock": True
    },
    "Graphic scarf": {
        "price": "$35",
        "colors": ["black", "gray", "red"],
        "quality": "Trendy",
        "in_stock": True
    },
    "Tweed scarf": {
        "price": "$45",
        "colors": ["brown", "gray", "green"],
        "quality": "Durable",
        "in_stock": True
    },
    "Woven scarf": {
        "price": "$38",
        "colors": ["blue", "green", "black"],
        "quality": "Textured",
        "in_stock": False
    },
    "Chunky knit scarf": {
        "price": "$50",
        "colors": ["cream", "gray", "burgundy"],
        "quality": "Thick",
        "in_stock": True
    },
    "Jacquard scarf": {
        "price": "$60",
        "colors": ["blue", "gold", "gray"],
        "quality": "Patterned",
        "in_stock": True
    },
    "Ribbed scarf": {
        "price": "$22",
        "colors": ["black", "gray", "green"],
        "quality": "Textured",
        "in_stock": True
    },
    "Boho scarf": {
        "price": "$27",
        "colors": ["brown", "orange", "beige"],
        "quality": "Bohemian",
        "in_stock": True
    },
    "Tie-dye scarf": {
        "price": "$32",
        "colors": ["purple", "yellow", "green"],
        "quality": "Fun",
        "in_stock": True
    },
    "Shawl scarf": {
        "price": "$60",
        "colors": ["red", "black", "gray"],
        "quality": "Warm",
        "in_stock": False
    },
    "Chiffon scarf": {
        "price": "$40",
        "colors": ["pink", "blue", "black"],
        "quality": "Elegant",
        "in_stock": True
    },
    "Patchwork scarf": {
        "price": "$48",
        "colors": ["red", "green", "blue"],
        "quality": "Unique",
        "in_stock": True
    },
    "Mesh scarf": {
        "price": "$27",
        "colors": ["black", "navy", "gray"],
        "quality": "Lightweight",
        "in_stock": False
    },
    "Bohemian scarf": {
        "price": "$34",
        "colors": ["brown", "black", "white"],
        "quality": "Free-spirited",
        "in_stock": True
    },
    "Reversible scarf": {
        "price": "$45",
        "colors": ["red/black", "green/blue", "purple/yellow"],
        "quality": "Dual-tone",
        "in_stock": True
    }
}


wallets_data = {
    "Slim wallet": {
        "price": "$30",
        "colors": ["black", "brown", "blue"],
        "quality": "Compact",
        "in_stock": True
    },
    "Bi-fold wallet": {
        "price": "$40",
        "colors": ["black", "brown", "navy"],
        "quality": "Classic",
        "in_stock": True
    },
    "Cardholder wallet": {
        "price": "$25",
        "colors": ["red", "gray", "black"],
        "quality": "Slim",
        "in_stock": False
    },
    "Travel wallet": {
        "price": "$50",
        "colors": ["dark brown", "black"],
        "quality": "Durable",
        "in_stock": True
    },
    "Money clip wallet": {
        "price": "$35",
        "colors": ["silver", "black"],
        "quality": "Minimalist",
        "in_stock": True
    },
    "Front pocket wallet": {
        "price": "$45",
        "colors": ["green", "brown"],
        "quality": "Comfortable",
        "in_stock": False
    },
    "Tri-fold wallet": {
        "price": "$38",
        "colors": ["black", "brown", "blue"],
        "quality": "Spacious",
        "in_stock": True
    },
    "Luxury wallet": {
        "price": "$100",
        "colors": ["black", "chocolate brown"],
        "quality": "Premium",
        "in_stock": True
    },
    "Hobo wallet": {
        "price": "$40",
        "colors": ["brown", "olive"],
        "quality": "Fashionable",
        "in_stock": True
    },
    "Clutch wallet": {
        "price": "$55",
        "colors": ["red", "black", "gold"],
        "quality": "Elegant",
        "in_stock": False
    },
    "Sport wallet": {
        "price": "$28",
        "colors": ["blue", "black", "gray"],
        "quality": "Active",
        "in_stock": True
    },
    "Purse wallet": {
        "price": "$60",
        "colors": ["pink", "white", "black"],
        "quality": "Chic",
        "in_stock": True
    },
    "Coin wallet": {
        "price": "$22",
        "colors": ["purple", "yellow", "blue"],
        "quality": "Compact",
        "in_stock": False
    },
    "Bifold leather wallet": {
        "price": "$55",
        "colors": ["black", "brown", "gray"],
        "quality": "Luxury",
        "in_stock": True
    },
    "Zipper wallet": {
        "price": "$40",
        "colors": ["red", "blue", "black"],
        "quality": "Secure",
        "in_stock": True
    },
    "Crossover wallet": {
        "price": "$48",
        "colors": ["brown", "green"],
        "quality": "Stylish",
        "in_stock": False
    },
    "Wallet clutch": {
        "price": "$50",
        "colors": ["gray", "black", "beige"],
        "quality": "Sleek",
        "in_stock": True
    },
    "Envelope wallet": {
        "price": "$30",
        "colors": ["black", "white", "brown"],
        "quality": "Elegant",
        "in_stock": True
    },
    "Tote wallet": {
        "price": "$65",
        "colors": ["blue", "green", "black"],
        "quality": "Premium",
        "in_stock": False
    },
    "Keychain wallet": {
        "price": "$15",
        "colors": ["black", "red", "green"],
        "quality": "Compact",
        "in_stock": True
    }
}


accessories_data = {
    "chain": {
        "price": "$15",
        "colors": ["gold", "silver", "black"],
        "quality": "Trendy",
        "in_stock": True  # Added availability
    },
    "rings": {
        "price": "$10",
        "colors": ["gold", "silver"],
        "quality": "Elegant",
        "in_stock": True  # Added availability
    },
}

# Conversational topics
conversation = {
    "greetings": {
        "keywords": ["hello", "hi", "hey", "good morning", "good evening", "sup"],
        "responses": ["Hello! How can I assist you?", "Hi there! Looking for something specific?", "Greetings! How may I help?"]
    },
    "farewells": {
        "keywords": ["bye", "goodbye", "see you", "take care", "farewell"],
        "responses": ["Goodbye! Have a great day!", "Thank you for visiting! Come back soon!", "See you next time!"]
    },
    "how are you": {
        "keywords": ["how are you", "how are you doing", "what's up", "how's it going"],
        "responses": ["I'm doing great, thanks for asking! How can I assist you today?", "I'm doing well, how about you?"]
    },
    "refund_policy": {
        "keywords": ["refund", "return", "money back", "return policy", "refund policy"],
        "responses": ["Our refund policy allows you to return items within 30 days for a full refund.",
                      "You can return any product within 30 days for a refund. Check our refund policy for more details."]
    },
    "track_order": {
        "keywords": ["track order", "order status", "where is my order", "order tracking", "shipping status"],
        "responses": ["To track your order, please visit the 'Track Order' section on our website and enter your order number.",
                      "You can track your order by visiting our 'Order Status' page and entering your tracking number."]
    },
    "discounts": {
        "keywords": ["discount", "sale", "promotion", "deal", "coupon", "discount code"],
        "responses": ["We are currently offering a 10% discount on all shirts! Use code 'SHIRT10' at checkout.",
                      "Check out our 'Deals' section for the latest discounts on select items."]
    },
    "deals": {
        "keywords": ["deal", "special offer", "promotion", "discount", "sale"],
        "responses": ["Today's deal: Buy one, get one free on all accessories!",
                      "Our current special offer: 20% off all pants for a limited time!"]
    },
    "product_availability": {
        "keywords": ["in stock", "availability", "available", "out of stock", "product availability"],
        "responses": ["Let me check the availability of that item for you. Could you provide the product name or number?",
                      "This product is currently in stock. Would you like to place an order?",
                      "Unfortunately, the item is out of stock at the moment, but I can notify you when it's back."]
    },
    "shipping_information": {
        "keywords": ["shipping", "delivery time", "shipping cost", "free shipping", "shipping options"],
        "responses": ["We offer free shipping on orders over $50. Standard shipping typically takes 3-5 business days.",
                      "Shipping costs vary depending on your location. You can check our shipping policy for more details.",
                      "Would you like express shipping? It can get your order delivered in 1-2 business days."]
    },
    "customer_support": {
        "keywords": ["support", "help", "customer service", "contact", "issue", "complaint"],
        "responses": ["Our customer service team is available 24/7 to assist you. You can reach us via chat, email, or phone.",
                      "If you're facing an issue with your order, please provide more details, and we'll resolve it as soon as possible."]
    },
    "payment_methods": {
        "keywords": ["payment", "pay", "payment options", "credit card", "paypal", "pay later"],
        "responses": ["We accept all major credit cards, PayPal, and Apple Pay.",
                      "You can also use our 'Buy Now, Pay Later' option with interest-free installments."]
    },
    "order_cancellation": {
        "keywords": ["cancel order", "cancel", "change order", "modify order", "order cancellation"],
        "responses": ["You can cancel your order within 2 hours of placing it. Please go to the 'My Orders' section.",
                      "Need to cancel or modify your order? Let me check the status and help you with that."]
    },
    "exchange_policy": {
        "keywords": ["exchange", "exchange policy", "swap item", "replace item"],
        "responses": ["Our exchange policy allows you to exchange items within 30 days of purchase, as long as they are in their original condition.",
                      "You can initiate an exchange request through our website. Let me know if you need any help."]
    },
    "gift_cards": {
        "keywords": ["gift card", "voucher", "store credit", "redeem gift card"],
        "responses": ["You can purchase gift cards for any amount. They are valid for a year.",
                      "To redeem a gift card, enter the card number at checkout. It will automatically apply the balance to your order."]
    },
    "order_issues": {
        "keywords": ["wrong order", "missing item", "damaged item", "order problem", "order issue"],
        "responses": ["I'm sorry to hear there’s an issue with your order. Please provide your order number, and we’ll resolve it right away.",
                      "If you received the wrong item or a damaged product, we’ll arrange a replacement or refund immediately."]
    },
    "product_recommendations": {
        "keywords": ["recommendation", "suggest", "suggestion", "best product", "best seller"],
        "responses": ["Looking for recommendations? Our best-selling products right now are X, Y, and Z.",
                      "Tell me what you're looking for, and I’ll suggest the best products to meet your needs."]
    },
    "account_management": {
        "keywords": ["account", "login", "reset password", "create account", "my account"],
        "responses": ["You can manage your account by logging in on our website. Need help resetting your password?",
                      "If you don’t have an account, you can create one easily by signing up with your email."]
    },
    "loyalty_program": {
        "keywords": ["loyalty program", "rewards", "points", "membership", "loyalty benefits"],
        "responses": ["Join our loyalty program and earn points on every purchase. Points can be redeemed for discounts!",
                      "Loyalty members also get early access to sales and exclusive deals. Sign up today!"]
    },
    "product_reviews": {
        "keywords": ["reviews", "product reviews", "customer feedback", "rate product"],
        "responses": ["You can check product reviews from other customers on each product page.",
                      "We appreciate your feedback! You can leave a review after purchasing the product."]
    },
    "small_talk": {
        "keywords": ["how's the weather", "what's the weather", "is it hot", "weather update"],
        "responses": ["I'm just a chatbot, but you can always check the weather on your phone!",
                      "Not sure about the weather, but I hope it's a sunny day for you!"]
    },
    "jokes": {
        "keywords": ["tell me a joke", "make me laugh", "joke", "funny"],
        "responses": ["Why don’t skeletons fight each other? They don’t have the guts!",
                      "I would tell you a construction joke, but I’m still working on it."]
    },
    "compliments": {
        "keywords": ["compliment", "say something nice", "praise me"],
        "responses": ["You’re doing amazing today!", "You have a great sense of style!"]
    },
    "random_facts": {
        "keywords": ["tell me a fact", "random fact", "did you know"],
        "responses": ["Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
                      "Did you know that octopuses have three hearts? Two pump blood to the gills, while one pumps it to the rest of the body!"]
    },
    "favorite_color": {
        "keywords": ["what's your favorite color", "favorite color", "do you have a favorite color"],
        "responses": ["I don’t have a favorite color, but I think blue is pretty calming, don’t you?",
                      "I like all colors equally, but how about you? What’s your favorite color?"]
    },
    "hobbies": {
        "keywords": ["do you have hobbies", "what do you do for fun", "free time", "pastime" ,"favourite hobbies"],
        "responses": ["I like helping people find the best deals and giving product recommendations! What about you?",
                      "If I could have hobbies, I’d probably enjoy reading. What do you like to do in your free time?"]
    },
    "food_suggestions": {
        "keywords": ["what should i eat", "what to eat", "give me food suggestions", "i'm hungry", "what's for dinner"],
        "responses": ["How about trying a delicious pasta dish?", "How about a salad with some grilled chicken?", "Maybe a burger or a pizza sounds good!", "Why not have some sushi or a healthy smoothie bowl?"]
    },

    "movies": {
        "keywords": ["favorite movie", "what should I watch", "good movies", "movie recommendation"],
        "responses": ["I hear that action movies are really exciting! How about watching the latest blockbuster?",
                      "If you’re in the mood for something light, maybe try a comedy!"]
    },
    "music": {
        "keywords": ["favorite music", "what should I listen to", "good songs", "music recommendation"],
        "responses": ["I don't listen to music, but I hear people love pop hits!",
                      "How about some relaxing jazz to wind down your day?"]
    },
    "who are you": {
        "keywords": ["who are you", "what are you", "who am I talking to", "tell me about yourself"],
        "responses": ["I’m your friendly e-commerce assistant! Here to help you with anything you need.",
                      "I’m a chatbot created to help with shopping, deals, and answering any questions you might have!"]
    },
    "weather": {
        "keywords": ["weather", "forecast", "is it raining", "how's the weather", "is it sunny"],
        "responses": ["I'm not sure about the current weather, but you can check your local forecast for the latest update.",
                      "It seems like a great day! Don't forget to check the weather app for the exact forecast."]
    },
     "travel": {
        "keywords": ["vacation", "holiday", "where should I go", "travel tips", "destination"],
        "responses": ["Are you looking for travel recommendations? Let me know where you're headed, and I’ll suggest some great destinations!",
                      "A beach vacation sounds amazing right now! Have you considered visiting Hawaii or the Caribbean?"]
    },
    "thank_you": {
        "keywords": ["thank you", "thanks", "appreciate it", "thank you very much"],
        "responses": ["You're welcome! Let me know if you need any further assistance.",
                      "It was my pleasure! Feel free to reach out anytime."]
    },
     "motivation": {
        "keywords": ["motivational", "inspiration", "encourage", "inspiring quote", "pep talk"],
        "responses": ["Believe in yourself! Every step you take gets you closer to your goal.",
                      "Keep going, you're doing great! Success is just around the corner."]
    },
    "self_care": {
        "keywords": ["self-care", "take care", "relaxation", "wellness", "mental health"],
        "responses": ["Self-care is so important! Take time to relax, whether it’s through a walk, reading, or just some quiet time.",
                      "Mental wellness is key! A little meditation or some mindfulness can do wonders."]
    },
    "time_management": {
        "keywords": ["time management", "schedule", "organize day", "how to manage time", "time tips"],
        "responses": ["Make a to-do list to prioritize tasks and focus on one thing at a time.",
                      "Try using time-blocking to allocate specific hours for different activities. It helps keep things organized."]
    }

}

def preprocess(text):
    """Normalize and tokenize user input."""
    return [word.lower() for word in word_tokenize(text)]

def find_best_match(query, choices, threshold=70):
    """Find the best matching choice using fuzz with a threshold."""
    best_match = None
    highest_score = 0
    for choice in choices:
        score = fuzz.partial_ratio(query, choice)
        if score > highest_score and score >= threshold:
            highest_score = score
            best_match = choice
    return best_match, highest_score

def handle_short_queries(query):
    """Handle generic short queries like 'shirt', 'pant', etc., and prompt for specifics if needed."""
    query_tokens = preprocess(query)

    # Handle conversational queries (like "how are you")
    conversation_topics = ["how are you", "how's it going", "what's up", "how r u"]
    if any(fuzz.partial_ratio(query, topic) > 85 for topic in conversation_topics):
        return handle_conversation(query)

    # Product categories and their corresponding data
    categories = {
        'shirt': shirts_data,
        'pant': pants_data,
        'wallet': wallets_data,
        'scarf': scarfs_data,
        'accessories': accessories_data
    }

    # Check for mentions of a category (e.g., 'shirt', 'pant', etc.)
    for category, data in categories.items():
        if category in query_tokens:
            # If the query is asking for availability
            availability_keywords = ["available", "availability", "in stock", "out of stock", "stock"]
            if any(keyword in query_tokens for keyword in availability_keywords):
                return get_product_info(query)  # Prioritize product info when availability is mentioned

            # Check if user is asking about types of products (e.g., "types of shirt", "different shirt")
            query_variants = ["types", "different", "diff", "category", "variety", "kinds", "list", "options"]
            if any(fuzz.partial_ratio(variant, token) > 80 for variant in query_variants for token in query_tokens):
                return get_category_info(category)  # Call get_category_info to list product types

            # If the query contains only the category (like "shirt") and doesn't specify more:
            if len(query_tokens) == 1:
                return f"Can you provide more details or be more specific about the {category}?"

            return get_product_info(query)  # Call get_product_info to handle product-specific details

    return None


def get_product_info(query):
    """Provide specific product information based on user input, including availability and color options."""
    categories = {
        'shirt': shirts_data,
        'pant': pants_data,
        'wallet': wallets_data,
        'scarf': scarfs_data,
        'accessories': accessories_data
    }

    # Detect if the user is asking about availability
    availability_keywords = ['available', 'availability', 'in stock', 'stock', 'out of stock']
    is_availability_query = any(keyword in query for keyword in availability_keywords)

    # Detect if the user is asking about color
    color_query = None
    colors = [
        "red", "blue", "green", "white", "navy blue", "gray", "pink", "black",
        "maroon", "charcoal", "olive", "cream", "light blue", "denim", "light pink",
        "beige", "sky blue", "purple", "yellow", "plaid", "black and white",
        "red and black", "blue and white", "green and white", "white with black sleeves",
        "white with blue sleeves", "gray with black sleeves", "white with maroon sleeves",
        "yellow floral", "blue floral", "green floral", "gold", "silver",
        "multicolor", "blue-white", "pink-white", "khaki", "tan", "blue floral",
        "orange", "ivory"
    ]
    for color in colors:
        if color in query:
            color_query = color
            break  # Exit the loop once the color is found

    # Check if a category is mentioned in the query
    category_query = None
    for category in categories:
        if category in query:
            category_query = category
            break

    if category_query:
        # If both color and category are mentioned, filter products by both
        if color_query:
            results = []
            data = categories[category_query]  # Get products in the specified category
            for product_name, product_info in data.items():
                if color_query in product_info["colors"]:
                    if is_availability_query:  # Filter by availability if requested
                        if product_info.get("in_stock", False):
                            results.append(f"{product_name.title()} (In Stock)")
                    else:
                        results.append(product_name.title())

            if results:
                return f"Here are the {category_query}s available in {color_query}:\n" + "\n".join(results)
            else:
                return f"Sorry, no {category_query}s available in {color_query}."

        # Check for availability of all items in the category (without color)
        if is_availability_query and "which" in query and len(query.split()) <= 5:
            available_items = [product_name.title() for product_name, product_info in categories[category_query].items() if product_info.get('in_stock', False)]
            if available_items:
                return f"The following {category_query}s are currently in stock:\n" + "\n".join(available_items)
            else:
                return f"Sorry, no {category_query}s are currently in stock."

        # Find the product match for specific product queries
        best_match, best_score = find_best_match(query, categories[category_query].keys())
        if best_match and best_score > 70:  # Only accept strong matches
            product = categories[category_query][best_match]

            if is_availability_query:  # If the query is about availability
                availability_status = "in stock" if product.get("in_stock", False) else "out of stock"
                return f"The {best_match} is currently {availability_status}."
            if "price" in query:
                return f"The price of the {best_match} is {product['price']}."
            if "color" in query or "colors" in query:
                return f"The {best_match} is available in the following colors: {', '.join(product['colors'])}."
            if "quality" in query:
                return f"The quality of the {best_match} is {product['quality']}."
            return f"{best_match.title()} - Price: {product['price']}, Colors: {', '.join(product['colors'])}, Quality: {product['quality']}."

    # Handle the case where only a color is mentioned (without category)
    if color_query:
        results = []
        for category, data in categories.items():
            for product_name, product_info in data.items():
                if color_query in product_info["colors"]:
                    if is_availability_query:  # Filter by availability if requested
                        if product_info.get("in_stock", False):
                            results.append(f"{product_name.title()} ({category}) - In Stock")
                    else:
                        results.append(f"{product_name.title()} ({category})")

        if results:
            return f"Here are the products available in {color_query}:\n" + "\n".join(results)
        else:
            return f"Sorry, no products available in {color_query}."

    # If no specific product or category is found, ask the user to be more specific
    if is_availability_query:
        return "Can you specify which product you're asking about? I can check its availability."

    return None  # Return None if no match is found







def get_category_info(query):
    """Respond to queries about categories of products and list their names."""
    categories = {
        "shirt": shirts_data,
        "pant": pants_data,
        "wallet": wallets_data,
        "scarf": scarfs_data,
        "accessories": accessories_data
    }

    query = query.lower()
    for category, data in categories.items():
        if category in query:
            product_names = list(data.keys())
            product_count = len(product_names)
            product_list = ", ".join(product_names)
            return f"We have {product_count} different types of {category}s: {product_list}."
    return None

def handle_conversation(query):
    """Respond to general conversational topics with prioritization."""
    query = query.lower()

    # Normalize informal abbreviations to standard forms
    abbreviations = {"r": "are", "u": "you", "how's": "how is", "i": "hiiiiiiii"}
    tokens = word_tokenize(query)
    normalized_query = " ".join([abbreviations.get(word, word) for word in tokens])

    # Check "how are you" first, then greetings and farewells
    for topic, info in conversation.items():
        if any(fuzz.partial_ratio(normalized_query, kw) > 85 for kw in info["keywords"]):
            return random.choice(info["responses"])

    return "I'm sorry, I couldn't understand that. Could you clarify?"

def handle_unknown_query():
    """Fallback for unknown queries."""
    return "I'm sorry, I couldn't find that information. Could you clarify or ask about something else?"

def main():
    print("E-commerce Chatbot: Welcome! Ask me about products, or any other questions. Type 'exit' to leave.")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("Chatbot: Thank you for visiting! Have a great day!")
            break

        # Check for short queries first
        short_query_response = handle_short_queries(user_input)
        if short_query_response:
            print("Chatbot:", short_query_response)
            continue


        # Check for product-related queries
        product_response = get_product_info(user_input)
        if product_response:
            print("Chatbot:", product_response)
            continue


        # Handle general conversation after product/category queries
        conversation_response = handle_conversation(user_input)
        if conversation_response:
            print("Chatbot:", conversation_response)
            continue


        # Check for category-related queries
        category_response = get_category_info(user_input)
        if category_response:
            print("Chatbot:", category_response)
            continue


        # Fallback response
        print("Chatbot:", handle_unknown_query())

        print("Chatbot: I'm sorry, I couldn't understand that. Could you clarify?")


main()