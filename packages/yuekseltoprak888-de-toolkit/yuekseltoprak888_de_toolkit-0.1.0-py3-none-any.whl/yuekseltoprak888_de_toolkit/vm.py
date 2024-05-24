import click
import subprocess

@click.command()
def start():
    """Start your VM"""
    # Replace with the actual command to start the VM
    subprocess.run(["echo", "Starting VM..."])

@click.command()
def stop():
    """Stop your VM"""
    # Replace with the actual command to stop the VM
    subprocess.run(["echo", "Stopping VM..."])

@click.command()
def connect():
    """Connect to your VM in VS Code inside your ~/code/yuekseltoprak888/folder"""
    # Replace with the actual command to connect to the VM
    subprocess.run(["echo", "Connecting to VM..."])
