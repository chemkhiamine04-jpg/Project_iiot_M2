# Projet IIoT - Apprentissage Fédéré et Agents IA

Ce dépôt contient mon travail pour le projet de Master 2 sur l'IoT. Le but du projet est de comprendre l'apprentissage fédéré (Federated Learning) et les agents IA (LLM) en local.

## Structure du projet

J'ai organisé mon espace de travail en 3 dossiers :

* **Apprentissage_fédéré :** Contient mes codes et tests avec le framework Flower sur la base de données MNIST.
* **LLM_Agent_IA :** Contient mes scripts Python pour les agents IA qui tournent en local avec Ollama.
* **Rapport :** Contient les explications théoriques et les réponses détaillées aux questions posées pendant les réunions.

---

## Journal des réunions

### Meeting 1 : 13 Octobre (11h00 - 11h30)

**Superviseure :** Mme Nancy Awad

**Ce que j'ai présenté :**

1. Mon travail avec Flower : apprentissage profond sur la base de données MNIST, puis apprentissage fédéré sur 3 rounds pour voir le résultat et comprendre la différence entre les deux.
2. Mon travail sur les agents IA : un script pour un agent IA simple, et un autre script où deux agents IA communiquent entre eux.

**Ce que Mme Nancy a demandé pour le prochain meeting :**

*(Toutes les réponses détaillées à ces questions sont rédigées dans le dossier `Rapport` et appliquées dans les codes des autres dossiers).*

**Questions sur l'Apprentissage Fédéré :**
* Quand est-ce que on choisit qu'un client participe dans un round ou pas ?
* La relation entre la distribution de données entre clients et leur participation au round ou leur contribution à l'algorithme de l'agrégation.
* Comment le serveur sait ou décide de la contribution de chaque client.
* C'est quoi les facteurs qui décident le nombre des manches ou rounds.
* Les autres stratégies d'agrégation au niveau d'un serveur autre que FedAvg.
* Est-ce que logiquement on peut faire le test sur le même test set.

**Questions sur les Agents IA :**
* Quelles sont les parties formantes sur les agents (LLM / tools / history / loop) : expliquer ça sur mon code.
* Expliquer les concepts suivants : agent specialization, communication protocols, task delegation, et validation.

**Organisation :**
* Créer un GitHub avec un dossier pour le code, un dossier pour les discussions (ce README) avec les dates, et un dossier qui contient les rapports sur tout ce que j'ai compris.