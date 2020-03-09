from base64 import urlsafe_b64decode

from knack.arguments import CLIArgumentType

from azure.cli.core.commands.parameters import get_resource_name_completion_list

from azure.cli.command_modules.keyvault._completers import (
        get_keyvault_name_completion_list, get_keyvault_version_completion_list)
from azure.cli.command_modules.keyvault._validators import get_vault_base_url_type


def load_arguments(self, _):
    def base64(value):
        value = bytes(value, 'utf-8')

        # Pad the invalid base64 strings because Azure is stupid
        while len(value) % 4 != 0:
            value += "="

        return urlsafe_b64decode(value)

    vault_name_type = CLIArgumentType(
        help='Name of the key vault.',
        options_list=['--vault-name'],
        metavar='NAME',
        id_part=None,
        completer=get_resource_name_completion_list('Microsoft.KeyVault/vaults')
    )

    for scope in ['wrap', 'unwrap']:
        with self.argument_context('keyvault key {}'.format(scope)) as c:
            c.argument(
                'vault_base_url',
                vault_name_type,
                type=get_vault_base_url_type(self.cli_ctx),
                id_part=None
            )

            c.argument(
                'key_name',
                options_list=['--name', '-n'],
                help='Name of the key.',
                id_part='child_name_1',
                required=True,
                completer=get_keyvault_name_completion_list('key')
            )
            c.argument(
                'key_version',
                options_list=['--version'],
                help='The key version. If omitted, uses the latest version.',
                default='',
                required=False,
                completer=get_keyvault_version_completion_list('key')
            )

            c.argument(
                'value',
                options_list=['--value', '-v'],
                help='Wrapped secret value.',
                type=base64,
                required=True
            )
            c.argument(
                'algorithm',
                options_list=['--alg', '-a'],
                help='The algorithm for wrapping.',
                required=True
            )
