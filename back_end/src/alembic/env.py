from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context

# Import your database setup and models from the correct paths
from db_setup import Base


from models.Alimento_model import Alimentos, Status
from models.Animal_model import Animal, ConsumoAnimal, StatusAnimal
from models.Usuario_model import Usuario
from models.Objetivo_model import Objetivos, ObjetivoCompleto


# Set up the Alembic config object
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Define the target metadata
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
