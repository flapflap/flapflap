import os
import sys
import subprocess
import signal

def git_fetch():
  """
  Exécute la commande `git fetch`.
  """
  return subprocess.check_output(["git", "fetch"])

def git_add():
  """
  Exécute la commande `git add` avec le message spécifié.
  """
  try:
    return subprocess.check_output(["git", "add", "*"])                   
  except subprocess.CalledProcessError as grepexc:                                                                                                   
    print("error code", grepexc.returncode, grepexc.output)

def git_commit(message):
  """
  Exécute la commande `git commit` avec le message spécifié.
  """
  try:
    return subprocess.check_output(["git", "commit", "-m", message])                   
  except subprocess.CalledProcessError as grepexc:                                                                                                   
    print("error code", grepexc.returncode, grepexc.output)

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
  app = subprocess.Popen(["/Applications/Pages.app/Contents/MacOS/Pages"], shell=True)

  # Attend que l'application se termine.
  print("Attente de la fin de l'application...")
  app.wait()

  # Exécute la commande `git add`.
  print("Exécution de la commande `git add`...")
  git_add()
  
  # Exécute la commande `git commit` avec le message `"Commit automatique"`.
  print("Exécution de la commande `git commit`...")
  git_commit("Commit automatique")

  # Exécute la commande `git push`.
  print("Exécution de la commande `git push`...")
  git_push()

if __name__ == "__main__":
  main()
