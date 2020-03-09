def load_command_table(self, _):
    with self.command_group('keyvault key') as g:
        g.keyvault_command('wrap', 'wrap_key', command_type=self.module_kwargs['custom_command_type'])
        g.keyvault_command('unwrap', 'unwrap_key', command_type=self.module_kwargs['custom_command_type'])
