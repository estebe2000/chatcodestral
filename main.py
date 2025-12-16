import os
import requests
import json
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

API_KEY = os.getenv("MISTRAL_API_KEY")

# Note: For some keys (especially Codestral beta/test), use https://codestral.mistral.ai/
# For standard Mistral keys, use https://api.mistral.ai/
CHAT_ENDPOINT = "https://codestral.mistral.ai/v1/chat/completions"
FIM_ENDPOINT = "https://codestral.mistral.ai/v1/fim/completions"

def chat_request(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "codestral-latest",
        "messages": messages
    }
    try:
        response = requests.post(CHAT_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Erreur: {e}"

def fim_request(prompt, suffix=""):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "codestral-latest",
        "prompt": prompt,
        "suffix": suffix,
        "temperature": 0
    }
    try:
        response = requests.post(FIM_ENDPOINT, headers=headers, json=data)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        return f"Erreur: {e}"

def main():
    if not API_KEY:
        print("Erreur: Clé API manquante. Veuillez configurer le fichier .env.")
        return

    print("Bienvenue sur Codestral Chatbot !")
    print("Commandes:")
    print(" - /chat : Mode discussion")
    print(" - /fim  : Mode complétion de code (FIM)")
    print(" - /exit : Quitter")

    mode = "chat"
    messages = []

    while True:
        user_input = input(f"\n[{mode.upper()}] > ").strip()

        if user_input == "/exit":
            print("Au revoir !")
            break
        elif user_input == "/chat":
            mode = "chat"
            print("Mode Chat activé.")
            continue
        elif user_input == "/fim":
            mode = "fim"
            print("Mode FIM activé. Entrez votre code (prompt). Pour ajouter un suffixe, utilisez '|||' comme séparateur.")
            continue

        if mode == "chat":
            messages.append({"role": "user", "content": user_input})
            print("Codestral réfléchit...")
            response = chat_request(messages)
            print(f"Codestral: {response}")
            messages.append({"role": "assistant", "content": response})

        elif mode == "fim":
            parts = user_input.split("|||")
            prompt = parts[0]
            suffix = parts[1] if len(parts) > 1 else ""

            print("Codestral complète...")
            completion = fim_request(prompt, suffix)
            print(f"Complétion: {completion}")

            # Reconstruct full code for display
            full_code = prompt + completion + suffix
            print("\n--- Code Complet ---")
            print(full_code)
            print("--------------------")

if __name__ == "__main__":
    main()
