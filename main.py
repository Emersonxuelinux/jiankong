#!/usr/bin/env python3
# _*_ codding = utf-8 _*_
# author : k3vi
from woospider import main as wooyun
from butian import main as butian
from loudonghezi import main as loudonghezi
import threading


def main():
    """
    threads = []
    t1 = threading.Thread(target=wooyun())
    threads.append(t1)
    t2 = threading.Thread(target=butian())
    threads.append(t2)
    t3 = threading.Thread(target=loudonghezi())
    threads.append(t3)
    for t in threads:
        t.setDaemon(True)
        t.start()
    """
    wooyun()
    butian()
    loudonghezi()


if __name__ == "__main__":
    print("start")
    main()
