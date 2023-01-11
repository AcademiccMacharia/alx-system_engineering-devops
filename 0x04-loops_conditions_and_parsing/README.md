# Loops, conditions and parsing

In this directory, I delve a little deeper into bash scripts, seeking to show the different loops in bash as well as parsing.

**Side tip:** Always use `#!/usr/bin/env bash` instead of `#!/usr/bin/bash` as it enables your scripts to be portable.

### Technologies used
1. Files have been interpreted on Ubuntu 22.04 LTS
2. All files are according to the `shellcheck` guide

The table below contains the files used in this directory as well as their descriptions.

| **Files** | **Description** |
| -------- | -------- |
| `0-RSA_public_key.pub` | Creating a RSA key pair |
| `1-for_best_school` | Bash script that displays `Best School` 10 times |
| `2-while_best_school` | Bash script that displays `Best School` 10 times |
| `3-until_best_school` | Bash script that displays `Best School` 10 times |
| `4-if_9_say_hi` | Bash script that displays `Best School` 10 times, but for the 9th iteration, displays `Best School` and then `Hi` on a new line |
| `5-4_bad_luck_8_is_your_chance` | Bash script that loops from 1 to 10 |
| `6-superstitious_numbers` | Bash script that displays numbers from 1 to 20 |
| `7-clock` | Bash script that displays the time for 12 hours and 59 minutes |
| `8-for_ls` | Bash script that displays: The content of the current directory |
| `9-to_file_or_not_to_file` | Bash script that gives you information about the `school` file |
| `10-fizzbuzz` | Bash script that displays numbers from 1 to 100 |
| `100-read_and_cut` | Bash script that displays the content of the file /`etc/passwd` |
| `101-tell_the_story_of_passwd` |  Bash script that displays the content of the file `/etc/passwd`, using the `while` loop + IFS |
| `102-lets_parse_apache_logs` | Bash script that displays the visitor IP along with the HTTP status code from the Apache log file |
| `103-dig_the-data` | Bash script that groups visitors by IP and HTTP status code, and displays this data |
