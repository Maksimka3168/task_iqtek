from app.api.console.users.users import register_command
from app.factories.config_factory import ConfigFactoryStorage, YmlConfigFactory
from app.factories.repository_factory import StorageRepositoryFactory, MemoryRepositoryFactory, \
    PostgresRepositoryFactory
from app.repository.base import BaseUserRepository
from app.utils.ioc import ioc


if __name__ == "__main__":
    config_factory_storage = ConfigFactoryStorage()
    config_factory_storage.register_factory(YmlConfigFactory())
    config = config_factory_storage.get_instance("../config.yml")

    repository_factory_storage = StorageRepositoryFactory()
    repository_factory_storage.register_factory(MemoryRepositoryFactory())
    repository_factory_storage.register_factory(PostgresRepositoryFactory())
    repository = repository_factory_storage.get_instance(config.type, settings=config.settings)
    ioc.set(BaseUserRepository, repository)

    cli = register_command()
    cli()
