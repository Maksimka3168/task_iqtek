from app.console.users.users import register_command
from app.bootstrap.initialization_app import initialize_app


if __name__ == "__main__":
    initialize_app(config_path="../../config.yml")
    cli = register_command()
    cli()
