import app.bootstrap.initialization_app

from app.api.console.users.users import register_command

if __name__ == "__main__":
    cli = register_command()
    cli()
