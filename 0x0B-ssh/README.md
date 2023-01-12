# SSH

Your mission, should you chose to accept it, is to go through the files below to gain an understanding of various functionalities of the `secure shell` ie ssh. This directory aims to create SSH/RSA key pairs as well as connecting ssh client to a server.

The table below contains the files used in this directory as well as their descriptions.

| **Files** | **Descriptions** |
| --------- | ---------- |
| `0-use_a_private_key` | Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu` |
| `1-create_ssh_key_pair`| Bash script that creates an RSA key pair |
| `2-ssh_config` |  SSH client configuration to use the private key |
| `100-puppet_ssh_config.pp` | Set up client SSH configuration file so that you can connect to a server without typing a password |
