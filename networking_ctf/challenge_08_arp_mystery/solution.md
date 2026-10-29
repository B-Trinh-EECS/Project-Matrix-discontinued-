# ARP Mystery — Solution & Walkthrough

**Goal:** Find the flag in the ARP dump.

**Step-by-step:**
1. Open the ARP dump:
   ```
   cat arp/arp_dump.txt
   ```
2. Look for vendor/comment text after MAC addresses. You'll find:
   ```
   note: "falcon{@rp_sp00f1ng}"
   ```
**Flag:** `falcon{@rp_sp00f1ng}`
