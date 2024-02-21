import openai

# Set up your OpenAI API key
openai.api_key = 'your_api_key'


def generate_product_description(product_name, features, target_audience):
    try:
        prompt = f"Nom du produit: {product_name}\n Fonctionnalités du produit: {features}\n Public cible: {target_audience}\nProduct Description:"

        # Use the GPT-3 API to generate a product description
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",
            prompt=prompt,
            temperature=0.7,
            max_tokens=100
        )

        # Retrieve and print the generated description
        product_description = response.choices[0].text.strip()
        print("Description du produit générée :")
        print(product_description)
    except Exception as e:
        print("Erreur d'appel API:" + str(e))
    return None


generate_product_description(
    product_name="Smart Lamp",
    features="Remote control, color change, automatic brightness adjustment",
    target_audience="Smart home enthusiasts and those looking to create a personalized ambiance in their space."
)