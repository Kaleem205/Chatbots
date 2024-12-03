# !pip install pandas
#!pip uninstall -y nltk
# !pip install --upgrade nltk
# !pip install rapidfuzz

import pandas as pd
import random
from nltk.tokenize import word_tokenize
from rapidfuzz import fuzz
import nltk

# Preload NLTK resources

nltk.download('punkt_tab')
nltk.download('punkt')

# Load product data from CSV
products_df = pd.read_csv('products.csv')
categories = products_df['Category'].unique()
products_by_category = {category: {} for category in categories}

for _, row in products_df.iterrows():
    products_by_category[row['Category']][row['Name']] = {
    "price": row['Price'],
    "colors": row['Colors'].split(', '),
    "quality": row['Quality'],
    "in_stock": str(row['In Stock']).strip().lower() in ['true', '1', 'yes']
    }


# Map category data for compatibility with original code
shirts_data = products_by_category.get("shirt", {})
pants_data = products_by_category.get("pant", {})
wallets_data = products_by_category.get("wallet", {})
scarfs_data = products_by_category.get("scarf", {})
accessories_data = products_by_category.get("accessories", {})

# Load conversation data from CSV
conversation_df = pd.read_csv('conversation.csv')
conversation = {
    row['Topic']: {
        "keywords": row['Keywords'].split(', '),
        "responses": row['Responses'].split('|')
    }
    for _, row in conversation_df.iterrows()
}

# Functions preserved from original code
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