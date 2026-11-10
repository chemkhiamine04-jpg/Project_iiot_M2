from openai import OpenAI

# 1. Connexion au moteur local Ollama
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama" 
)

# ==========================================
# PHASE 1 : L'Agent 1 (Expert) génère son explication
# ==========================================
print("⏳ L'Agent 1 (Expert) réfléchit à la question...\n")

system_agent_1 = "Tu es un expert en IA et IIoT. Explique les concepts de manière simple et courte (3 phrases max)."
question_initiale = "Qu'est-ce que l'apprentissage fédéré (federated learning) ?"

reponse_1 = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": system_agent_1},
        {"role": "user", "content": question_initiale}
    ],
    temperature=0.3
)

# On extrait le texte généré et on le sauvegarde dans une variable
texte_agent_1 = reponse_1.choices[0].message.content

print("🤖 Agent 1 (Expert) :")
print(texte_agent_1)
print("\n" + "-"*50 + "\n")


# ==========================================
# PHASE 2 : L'Agent 2 (Ingénieur) lit et critique
# ==========================================
print("⏳ L'Agent 2 (Ingénieur) lit l'explication et prépare sa question...\n")

system_agent_2 = "Tu es un ingénieur réseau très pointilleux. Tu lis les explications qu'on te donne et tu poses toujours UNE seule question technique sur les problèmes de sécurité."

# LE PONT ENTRE LES DEUX AGENTS : On injecte 'texte_agent_1' dans le message du 2ème !
message_pour_agent_2 = f"Voici l'explication de l'expert : '{texte_agent_1}'. Pose-lui ta question technique."

reponse_2 = client.chat.completions.create(
    model="llama3.2",
    messages=[
        {"role": "system", "content": system_agent_2},
        {"role": "user", "content": message_pour_agent_2} # L'agent 2 "lit" la réponse de l'agent 1
    ],
    temperature=0.3
)

texte_agent_2 = reponse_2.choices[0].message.content

print("🕵️ Agent 2 (Ingénieur) :")
print(texte_agent_2)