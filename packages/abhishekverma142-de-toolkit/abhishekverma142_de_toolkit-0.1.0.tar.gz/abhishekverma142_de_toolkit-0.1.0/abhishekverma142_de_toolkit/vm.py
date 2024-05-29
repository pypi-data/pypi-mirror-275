import click
import subprocess

@click.command()
def start():
    """Start your vm"""
    subprocess.run("gcloud compute instances start --zone=europe-west1-b lewagon-data-eng-vm-abhishekverma142", shell=True, check=True)

@click.command()
def stop():
    """Stop your vm"""
    subprocess.run("gcloud compute instances stop --zone=europe-west1-b lewagon-data-eng-vm-abhishekverma142", shell=True, check=True)

@click.command()
def connect():
    """Connect to your vm in vscode inside your ~/code/abhishekverma142/folder """
    subprocess.run("code --folder-uri vscode-remote://ssh-remote+ankita@34.76.185.84/~/code/abhishekverma142/", shell=True, check=True)
