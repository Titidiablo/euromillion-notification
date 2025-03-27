import requests
import datetime

# URL de l'API des r�sultats de l'Euromillion (utilisation de l'API publique)
euromillion_url = "https://api.loto-api.fr/v1/euromillion/latest"

# Fonction pour v�rifier la cagnotte et envoyer la notification si elle d�passe 100 millions
def check_euromillion():
    # Appel de l'API pour obtenir les derniers r�sultats
    response = requests.get(euromillion_url)
    data = response.json()

    # V�rifier la cagnotte (on suppose que l'API renvoie une cl� 'jackpot' en millions d'euros)
    jackpot = data['jackpot']

    # Si la cagnotte d�passe 100 millions
    if jackpot > 100:
        # Envoi de la notification via NTFY
        message = f"La cagnotte de l'Euromillion est � {jackpot} millions d'euros !"
        requests.post(f"https://ntfy.sh/euromillion", data=message.encode('utf-8'))
        print("Notification envoy�e !")
    else:
        print("Cagnotte inf�rieure � 100 millions.")

# Ex�cution
check_euromillion()
