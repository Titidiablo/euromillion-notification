import requests
import datetime

# URL de l'API des résultats de l'Euromillion (utilisation de l'API publique)
euromillion_url = "https://api.loto-api.fr/v1/euromillion/latest"

# Fonction pour vérifier la cagnotte et envoyer la notification si elle dépasse 100 millions
def check_euromillion():
    # Appel de l'API pour obtenir les derniers résultats
    response = requests.get(euromillion_url)
    data = response.json()

    # Vérifier la cagnotte (on suppose que l'API renvoie une clé 'jackpot' en millions d'euros)
    jackpot = data['jackpot']

    # Si la cagnotte dépasse 100 millions
    if jackpot > 100:
        # Envoi de la notification via NTFY
        message = f"La cagnotte de l'Euromillion est à {jackpot} millions d'euros !"
        requests.post(f"https://ntfy.sh/euromillion", data=message.encode('utf-8'))
        print("Notification envoyée !")
    else:
        print("Cagnotte inférieure à 100 millions.")

# Exécution
check_euromillion()
