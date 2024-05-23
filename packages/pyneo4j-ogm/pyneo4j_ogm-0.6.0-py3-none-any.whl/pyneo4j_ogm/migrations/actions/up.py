"""
Applies the defined number of migrations in correct order.
"""

from copy import deepcopy
from typing import Optional

from pyneo4j_ogm.logger import logger
from pyneo4j_ogm.migrations.utils.client import MigrationClient
from pyneo4j_ogm.migrations.utils.migration import (
    RunMigrationCount,
    check_initialized,
    get_migration_config,
    get_migration_files,
)
from pyneo4j_ogm.migrations.utils.models import AppliedMigration


async def up(up_count: RunMigrationCount = "all", config_path: Optional[str] = None) -> None:
    """
    Applies the defined number of migrations in correct order.

    Args:
        up_count(int, optional): Number of migrations to apply. Can be "all" to apply all migrations.
            Defaults to "all".
        config_path(str, optional): Path to the migration config file. Defaults to None.
    """
    check_initialized(config_path=config_path)
    config = get_migration_config(config_path)

    logger.info("Applying next %s migrations", up_count)
    async with MigrationClient(config) as migration_client:
        migration_files = get_migration_files(config.migration_dir)
        migration_node = await migration_client.get_migration_node()

        logger.debug("Filtering migration files for unapplied migrations")
        for applied_migration in migration_node.get_applied_migration_identifiers:
            migration_files.pop(applied_migration, None)

        for count, _ in enumerate(deepcopy(migration_files).values()):
            if up_count != "all" and count >= up_count:
                break

            # Since the migration files are sorted by identifier, we can get the current migration
            # by getting the min identifier, which is a UNIX timestamp meaning the lowest value is the oldest migration
            current_migration_identifier = min(migration_files.keys())
            current_migration = migration_files[current_migration_identifier]

            logger.debug("Applying migration %s", current_migration["name"])
            await current_migration["up"](migration_client.client)
            migration_files.pop(current_migration_identifier)
            migration_node.applied_migrations.append(AppliedMigration(name=current_migration["name"]))

        migration_node.updated_at = migration_node.applied_migrations[-1].applied_at
        await migration_node.update()
