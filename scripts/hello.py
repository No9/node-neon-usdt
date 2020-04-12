#!/usr/bin/python3
#
# This is a Hello World example that formats output as fields.

from __future__ import print_function
from bcc import BPF, USDT
from bcc.utils import printb
import sys

if len(sys.argv) < 2:
    print("USAGE: probe.py PID")
    exit()
pid = sys.argv[1]

# define BPF program
bpf_text = """
int hello(void *ctx) {
    bpf_trace_printk("Hello, World!\\n");
    return 0;
}
"""
u = USDT(pid=int(pid))
u.enable_probe(probe="helloprobe", fn_name="hello")

# load BPF program
b = BPF(text=bpf_text, usdt_contexts=[u])

# header
print("%-18s %-16s %-6s %s" % ("TIME(s)", "COMM", "PID", "MESSAGE"))

# format output
while 1:
    try:
        (task, pid, cpu, flags, ts, msg) = b.trace_fields()
    except ValueError:
        continue
    except KeyboardInterrupt:
        exit()
    printb(b"%-18.9f %-16s %-6d %s" % (ts, task, pid, msg))
