# OpenLuck Try Try Again

## What's up with this script?

### TLDR
I wanted to be able to run OpenLuck with a sequence of targets

### A little bit of history
I created this script because I'm studying for TCM's [Practical Network Penetration Testing](https://certifications.tcm-sec.com/) exam.
Chapter 10 has a lesson where we use [OpenLuck](https://github.com/heltonWernik/OpenLuck) to get a bind shell on a [Kioptrix Level 1 box](https://www.vulnhub.com/entry/kioptrix-level-1-1,22/) but rather than just following the tutorial or reading through the list of options I wanted to be able to run all possible target options as if I didn't have the full manual.
Basically I'm generating every option of target based on a given starting and stopping hex value.

### Preconditions
1. You should put and run this script from the OpenLuck repo folder

### Improvements
1. Setting parameters for all values that can be modified such as target IP, port, initial hex and final hex
2. Update mechanism to identiy when there's an error and when there's a shell, right now I'm verifying error based on specific strings and I assume there's been a shell when the script stops failing

### Execution and Output

1. Navigate into the OpenLuck repo directory
2. Run: python3 007-openluck-try-try-again.py
3. Output:
```
0x66 was not successful
Attempt # 36; Target: 0x67
output: read_ssl_packet: Record length out of range (rec_len = 0)

0x67 was not successful
Attempt # 37; Target: 0x68
output: read_ssl_packet: Record length out of range (rec_len = 0)

0x68 was not successful
Attempt # 38; Target: 0x69
output: Error in read: Connection reset by peer

```