# Configuration Management

------------------

### Technologies
1. All files have been interpreted on Ubuntu 22.04 LTS
2. Puppet files follow the **puppet_lint** style guide


Configuration management is the process of handling changes to a system that it maintains intergrity over time. There are several tools that helps us automate processes such as `puppet`, `Ansible`, `Chef`. In this directory, I use Puppet.

Directory meme 😂

![directory meme](https://imgs.search.brave.com/x-AYHPKDRn5xgIdMPf398KLn1jH5t5HB5qer416UzHg/rs:fit:625:336:1/g:ce/aHR0cHM6Ly91cGxv/YWRzLnRvcHRhbC5p/by9ibG9nL2ltYWdl/LzEyNzQ2My90b3B0/YWwtYmxvZy1pbWFn/ZS0xNTQwODk0MzE4/OTMyLTViZjFjMDM4/ZmVkODRlNjYxM2Jh/YmYzNzMzNmNiYTJj/LmpwZw)

The table below contains the files used in this directory as well as their descriptions.

| **Files** | **Descriptions** |
| -------- | -------- |
| `0-create_a_file.pp` | create a file in /tmp |
| `1-install_a_package.pp` | install flask from pip3 |
| `2-execute_a_command.pp` | create a manifest that kills a process named `killmenow` |

