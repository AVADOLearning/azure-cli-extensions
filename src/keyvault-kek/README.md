# Key Vault Key Encryption Key commands

Provides Key Encryption Key wrap and unwrap operations, useful for mopping up Azure Disk Encryption flavoured tears.

---

## Usage

The `wrap` and `unwrap` commands are added to the existing `keyvault key` command group.

### Wrap

First, base64-encode the text you'd like to wrap:

```console
echo 'base64 encoded gibberish' | base64
YmFzZTY0IGVuY29kZWQgZ2liYmVyaXNoCg==
```

Then wrap it:

```console
$ az keyvault key wrap \
        --alg RSA-OAEP
        --value 'YmFzZTY0IGVuY29kZWQgZ2liYmVyaXNoCg==' \
        --name my-key \
        --vault-name my-vault
{
  "kid": "https://my-vault.vault.azure.net/keys/my-key/00000000000000000000000000000000",
  "result": "dm4s5dQVLdT7/EKWEu5sWUu3OEymc5T71xINOVcC5dXFOnH3bGEZGQ3Nws2++6rcpsRrH42/2yOihhOqrOQzU8++IB37HjBwFxGre5Qe1TrIh1HWdE9BwrB21xs2/uQOd9X5rhixnK68Q8PIzJGYn6c0bil2mDQHx9fHzHpL80PE8CgSrUaGof0N71q94dBLo3qIr+9QGySv/nI0WFtA8+4AYErISRWxkjxzEq5pGGUU95QSa/nlmYtz4xHnAJo/uCbEHou4ZpXs5Z9V7X+xkP/dclo0w4dWCkQvFHSRZ/5SuIZQAHIktN/uVFQPg0N5oI5e/5JlaNERZqAPyQ81ufZDetelkZSj566oZ3E2dVv24DL4ClajvSaXaBMLQU2zMCpUm3i0P52u1T9E45+BZ/MLTgjzZbgcyggSimfxQBnu62F0cGRSLBUCqMqeQ9Z4v9lp2PZGb3X1VoamzHnKlMP9EBE38UeglF388tibnp4g+AQ5dSMlX7Y7kwMMGHCfsDKBZfILDBKe7Vml/h1b70WVc2zu4OSnhy5UJ+qXTlbZLTO6G8J7JVydciRwWrIpn24a2Avz03l7D9xJePVNsLOdADUk/DnfH4lE32NEI29kvJ9tvGsnuTSHxffUSeIBQPLUjZlEQArwyWwPeyDAcFpIRLyVZtYBo4bMF+vHUAA="
}
```

The long string of garbage is the resulting secret, which can now be stored in a Key Vault.

You may optionally supply a `--version` to specify the key value, if not the latest.

### Unwrap

```console
az keyvault key unwrap \
        --alg RSA-OAEP \
        --value 'dm4s5dQVLdT7/EKWEu5sWUu3OEymc5T71xINOVcC5dXFOnH3bGEZGQ3Nws2++6rcpsRrH42/2yOihhOqrOQzU8++IB37HjBwFxGre5Qe1TrIh1HWdE9BwrB21xs2/uQOd9X5rhixnK68Q8PIzJGYn6c0bil2mDQHx9fHzHpL80PE8CgSrUaGof0N71q94dBLo3qIr+9QGySv/nI0WFtA8+4AYErISRWxkjxzEq5pGGUU95QSa/nlmYtz4xHnAJo/uCbEHou4ZpXs5Z9V7X+xkP/dclo0w4dWCkQvFHSRZ/5SuIZQAHIktN/uVFQPg0N5oI5e/5JlaNERZqAPyQ81ufZDetelkZSj566oZ3E2dVv24DL4ClajvSaXaBMLQU2zMCpUm3i0P52u1T9E45+BZ/MLTgjzZbgcyggSimfxQBnu62F0cGRSLBUCqMqeQ9Z4v9lp2PZGb3X1VoamzHnKlMP9EBE38UeglF388tibnp4g+AQ5dSMlX7Y7kwMMGHCfsDKBZfILDBKe7Vml/h1b70WVc2zu4OSnhy5UJ+qXTlbZLTO6G8J7JVydciRwWrIpn24a2Avz03l7D9xJePVNsLOdADUk/DnfH4lE32NEI29kvJ9tvGsnuTSHxffUSeIBQPLUjZlEQArwyWwPeyDAcFpIRLyVZtYBo4bMF+vHUAA=' \
        --name my-key \
        --vault-name avado-disk-encryption
{
  "kid": "https://avado-disk-encryption.vault.azure.net/keys/my-key/00000000000000000000000000000000",
  "result": "YmFzZTY0IGVuY29kZWQgZ2liYmVyaXNoCg=="
}
```

The resulting string should be valid base64, which can be decoded for the original result:

```console
echo 'YmFzZTY0IGVuY29kZWQgZ2liYmVyaXNoCg==' | base64 -d
base64 encoded gibberish
```

## Hacking

First, follow the [hacking instructions](../../README.md#hacking) in the root of this repository.

Now install the requirements:

```console
pip install -r requirements.txt
```
