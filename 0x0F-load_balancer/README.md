# Load Balancer

-----------

![load balancing diagram](https://imgs.search.brave.com/gyexaY93GkF4s9AhxkiNZztRJ6xve-Lad2VZyZkwX8w/rs:fit:891:225:1/g:ce/aHR0cHM6Ly90c2Uz/Lm1tLmJpbmcubmV0/L3RoP2lkPU9JUC5j/a2NRSWZJQ0RlZmxy/MlNXU29BU1R3SGFE/OCZwaWQ9QXBp)

In this directory, I delve into load balancing which is distributing the work-load of your system to multiple individual systems, or group of systems to reduce the amount of load on an individual system.

There are 3 types of Load Balancing:
		1. No Load Balancing
		2. Layer 4 load balancing
		3. Layer 7 load balancing

There are various load balancing software but I use HAProxy in the tasks carried out in this directory.

The table below contains the files used in this directory as well as their descriptions.

| **Files** | **Description** |
| -------- | ---------- |
| `0-custom_http_response_header` | Configures a new server |
| `1-install_load_balancer` | Install and configure HAproxy on your lb-01 server |
| `2-puppet_custom_http_response_header.pp` | Manifest to automate the task of creating a custon HTTP header response |
