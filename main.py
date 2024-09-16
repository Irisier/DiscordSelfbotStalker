import discord
import http.client, urllib
from playsound import playsound


# Benutzer-ID des zu überwachenden Benutzers
USER_ID = 1234567890  # Ersetze dies durch die tatsächliche Benutzer-ID

# Erstellt eine Instanz des Clients
client = discord.Client()  # Keine Intents verwendet, geht eh nicht mit der selfbot fork

@client.event
async def on_ready():
    print(f'Welcome {client.user}')

@client.event
async def on_presence_update(before, after):
    # Überprüfen, ob die Benutzer-ID mit der gewünschten übereinstimmt
    if before.id == USER_ID:
        # Überprüfen, ob der Status sich geändert hat
        if before.status != after.status:
            print(f'{before.name} hat den Status von {before.status} zu {after.status} geändert.')
            message = f"{before.name} hat den Status von {before.status} zu {after.status} geändert."
            playsound("C:/Users/User/Desktop/discordpy/gw.mp3")  # Pfad zu deiner Sounddatei
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
             urllib.parse.urlencode({
                "token": "DEIN TOKEN VON PUSHOVER",
                "user": "DEIN-USER VON PUSHOVER",
                "message": message
             }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()

        # Überprüfen, ob das Spiel sich geändert hat (Aktivität)
        if before.activity != after.activity:
            print(f'{before.name} hat die Aktivität von {before.activity} zu {after.activity} geändert.')
            message = f"{before.name} hat die Aktivität von {before.activity} zu {after.activity} geändert."
            playsound("C:/Users/User/Desktop/discordpy/gw.mp3")  # Pfad zu deiner Sounddatei
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
             urllib.parse.urlencode({
                "token": "DEIN TOKEN VON PUSHOVER",
                "user": "DEIN-USER VON PUSHOVER",
                "message": message
             }), { "Content-type": "application/x-www-form-urlencoded" })
            conn.getresponse()

# Client starten
client.run('DEIN-DC-TOKEN')
