from openai import OpenAI

# 1. Connexion à ton Ollama local
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

# 2. Le "System Prompt" : on donne son identité
identite_agent = "Tu es un agent IA spécialisé dans programmation Python."

# 3. La question (l'entrée)
observation = "Bonjour, tu peux me donner un code en python stp pour une architecture de reseau de neuron avec keras pour entrainer un modéle sur la base de données mnist ?"

print("Envoi de l'information à l'agent en cours...\n")

# 4. Exécution de l'agent (sans try/except)
reponse = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": identite_agent},
        {"role": "user", "content": observation}
    ],
    temperature=0.3 # On remet une température basse pour des réponses sérieuses
)

# 5. Affichage de la réponse
print("🤖 Diagnostic de l'Agent :")
print(reponse.choices[0].message.content)