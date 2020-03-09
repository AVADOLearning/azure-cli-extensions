# AVADO's Azure CLI extensions

A great cloud needs great tools, but apparently Microsoft forgot to create either. Implements supports for the following missing operations:

* `keyvault-kek` provides Key Vault Key Encryption Key wrap and unwrap

---

## Installation

```console
az extension install --source some-wheel.whl
```

## Hacking

This extension follows the structure of Microsoft's [Azure/azure-cli-extensions repository](https://github.com/Azure/azure-cli-extensions).

Prepare an isolated virtual environment:

```console
python3 -m vewv venv
```

Activate it:

```console
. venv/bin/activate
```

Install the Azure CLI SDK, and a copy of the CLI with our extension repository enabled:

```console
pip install -r requirements.dev.txt
azdev setup -r .
```

We can then list the available extensions:

```console
$ azdev extension list
[
  {
    "install": "",
    "name": "key-vault-kek",
    "path": "/home/lukecarrier/Code/AVADO/AzureCliExtensions/src/key-vault-kek"
  }
]
```

And selectively install them:

```console
$ azdev extension add key-vault-kek
Adding extension '/home/lukecarrier/Code/AVADO/AzureCliExtensions/src/key-vault-kek'...
```
