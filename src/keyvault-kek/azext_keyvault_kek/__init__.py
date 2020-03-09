from azure.cli.core import AzCommandsLoader
from azure.cli.core.profiles import ResourceType


class KeyVaultKekCommandsLoader(AzCommandsLoader):
    def __init__(self, cli_ctx=None):
        from azure.cli.core.commands import CliCommandType
        from azure.cli.command_modules.keyvault._client_factory import keyvault_client_factory
        from azure.cli.command_modules.keyvault._command_type import KeyVaultArgumentContext, KeyVaultCommandGroup

        kek_custom = CliCommandType(
            operations_tmpl='azext_keyvault_kek.custom#{}',
            client_factory=keyvault_client_factory
        )

        super(KeyVaultKekCommandsLoader, self).__init__(
            cli_ctx=cli_ctx,
            resource_type=ResourceType.MGMT_KEYVAULT,
            custom_command_type=kek_custom,
            command_group_cls=KeyVaultCommandGroup,
            argument_context_cls=KeyVaultArgumentContext
        )

    def load_command_table(self, args):
        from .commands import load_command_table
        load_command_table(self, args)
        return self.command_table

    def load_arguments(self, command):
        from ._params import load_arguments
        load_arguments(self, command)


COMMAND_LOADER_CLS = KeyVaultKekCommandsLoader
