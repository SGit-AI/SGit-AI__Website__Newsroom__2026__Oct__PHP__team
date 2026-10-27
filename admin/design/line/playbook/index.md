# Prototype F: the line, the playbook

A content page under the line: the response step by step, with a line written for each role.

> Prototype F for review, built from the data of release v0.22.43. Not the live site. Every part of the page is listed here; a reader sees the parts written for their role.

The playbook 
## The response, step by step

Fixed in PHP 8.5.12, 8.4.27, 8.3.36, 8.2.35. An update only counts once the service restarts. 

### In order

1 

#### Find every system that runs PHP.

Websites, internal tools, suppliers, vendor appliances and the images you build from. 

2 

#### Patch internet-facing first.

mod_php, then FPM, then the rest. Restart every worker; rebuild every image. 

3 

#### Bound the known paths.

Each temporary setting blocks a path; none is a fix. 

4 

#### Watch the process tree.

Alert on a PHP worker spawning a shell or a downloader. 

5 

#### Decide who calls isolate or offline, and when.

Two US agencies say take it offline if it cannot be updated. 

### Fixed versions, and the settings until you are there

 Fixed in 8.5.12 · 8.4.27 · 8.3.36 · 8.2.35 
 memory_limit=-1, set where applications cannot Removes the controllable memory-limit failure; an underlying allocation failure can still reach the vulnerable 
 A low post_max_size (8M without uploads, 32M w Reduces exposure to specific attack paths; does not make an installation safe. 
 A container or cgroup memory limit as an avail Do not use RLIMIT_AS or RLIMIT_DATA: they can cause the vulnerable allocation failure. 
 session.upload_progress.enabled=0 in php.ini, Blocks the confirmed session paths only. ini_set() and .user.ini are too late.

---
site v0.22.43 · https://team.php.oct.2026.newsroom.sgit.ai/admin/design/line/playbook/index.html
