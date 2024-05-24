["Santa Is Watching" (aka Santa_IW)](https://gitlab.com/SRG_gitlab/santa-is-watching) is a network monitoring tool with 
an emphasis on ZFS and network attached storage in a homelab environment. Santa_IW can automatically discover hardware 
on your intranet and build up a list of appropriate tests which will run periodically to monitor your network.
Santa_IW runs on a single Linux computer which needs ssh keys to run diagnostic commands on other computers in your system. 

If Santa_IW can make an ssh connection to the node, it schedules tests, which include:
* monitor status and free space on zfs pools
* monitor age of most recent snapshot on zfs volumes
  * detects failures in periodic snapshot or send/receive pipelines
* monitor NFS and SMB volume shares
* monitor drive health as reported by smartctl
* monitor drives listed in /etc/fstab for disk free space
* monitor temperature and other data reported by lm-sensors
* monitor for failed services reported by systemctl --failed

Santa_IW is written entirely in Python (3.11 or later) and its configuration files are all editable json. It ships with 21 built in test types
and can load additional user written tests or plugins from user directories. An example plugin is provided to use a
Philips Hue color changing light bulb to provide a GREEN/YELLOW/RED system status light.

A web based interface lets the user navigate up and down the hierarchy of node groups, nodes and tests to see various
levels of detail. Tests can record numeric data where appropriate. Running averages are displayed and values over time
can be graphed in the GUI or extracted for offline processing. 

----

Santa_IW is hosted on [GitLab](https://gitlab.com/SRG_gitlab/santa-is-watching/-/wikis/home) and has been developed and tested on a Linux platform. It has been installed and run on RHEL, Fedora, Ubuntu
and Debian platforms (including Raspberry Pi 3). It is written in pure Python, but calls out to many Linux/Posix
command line utilities. It is plausible that it might someday work on other Posix compliant platforms (macOS or BSD),
but that is out of scope for the current effort. [For windows support...](https://en.wikipedia.org/wiki/Somebody_else%27s_problem)

Santa_IW is intended for homelab use on an internal network. It does not yet have any robust authentication system and
should not be exposed on the open internet.

A Reddit group has been setup for beta test participants at https://www.reddit.com/r/Santa_IW/

Santa_IW (Code and Documentation) is published under an MIT License, Copyright (c) 2024 Steven Goncalo
