import subprocess
import re


def get_apparmor_logs():

    logs = []

    try:

        result = subprocess.run(
            [
                "sudo",
                "journalctl",
                "-k",
                "-n",
                "20",
                "--no-pager"
            ],
            capture_output=True,
            text=True
        )


        for ligne in result.stdout.splitlines():


            if "apparmor=" in ligne.lower():


                # Extraction du statut DENIED
                statut = "DENIED" if "DENIED" in ligne else "ALLOWED"


                # Extraction du profil
                profil = re.search(
                    r'profile="([^"]+)"',
                    ligne
                )


                # Extraction de l'application
                application = re.search(
                    r'comm="([^"]+)"',
                    ligne
                )


                # Extraction de la ressource
                ressource = re.search(
                    r'name="([^"]+)"',
                    ligne
                )


                # Extraction de l'action
                action = re.search(
                    r'operation="([^"]+)"',
                    ligne
                )


                logs.append({

                    "application":
                    application.group(1)
                    if application else "Inconnue",


                    "profil":
                    profil.group(1)
                    if profil else "Inconnu",


                    "action":
                    action.group(1)
                    if action else "Inconnue",


                    "ressource":
                    ressource.group(1)
                    if ressource else "Inconnue",


                    "statut":
                    statut

                })


        return logs


    except Exception as e:

        return []
