def unwrap_key(
        client, vault_base_url,
        key_name=None, key_version=None,
        value=None, algorithm=None):
    return client.unwrap_key(
        vault_base_url,
        key_name, key_version,
        algorithm, value
    )


def wrap_key(
        client, vault_base_url,
        key_name=None, key_version=None,
        algorithm=None, value=None):
    return client.wrap_key(
        vault_base_url,
        key_name, key_version,
        algorithm, value
    )
