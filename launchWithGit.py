import os
import sys
import subprocess
import signal

def git_fetch():
  """
  Exécute la commande `git fetch`.
  """
  return subprocess.check_output(["git", "fetch"])

def git_commit(message):
  """
  Exécute la commande `git commit` avec le message spécifié.
  """
  return subprocess.check_output(["git", "commit", "-m", message])

def git_push():
  """
  Exécute la commande `git push`.
  """
  return subprocess.check_output(["git", "push"])

def main():
  """
  Exécution principale du script.
  """
  # Exécute la commande `git fetch`.
  print("Exécution de la commande `git fetch`...")
  git_fetch()

  # Lance l'application.
  print("Lancement de l'application...")
  app = subprocess.Popen(["/App/TextEdit"], shell=True)

  # Attend que l'application se termine.
  print("Attente de la fin de l'application...")
  app.wait()

  # Exécute la commande `git commit` avec le message `"Commit automatique"`.
  print("Exécution de la commande `git commit`...")
  git_commit("Commit automatique")

  # Exécute la commande `git push`.
  print("Exécution de la commande `git push`...")
  git_push()

if __name__ == "__main__":
  main()
