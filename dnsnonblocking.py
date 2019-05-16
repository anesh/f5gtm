from sys import argv
from itertools import cycle
from pprint import pprint
import bigsuds

from twisted.names import client
from twisted.internet.task import react
from twisted.internet.defer import gatherResults, inlineCallbacks

def query(reactor, server, name):
    resolver = client.getHostByName(name)
    return resolver

@inlineCallbacks
def main(reactor, *names):
    # Here's some random DNS servers to which to issue requests.
    servers = ["4.2.2.1", "8.8.8.8"]

    # Handy trick to cycle through those servers forever
    next_server = cycle(servers).next

    # Issue queries for all the names given, alternating between servers.
    results = []
    for n in names:
        results.append(query(reactor, next_server(), n))
    # Wait for all the results
    results = yield gatherResults(results)
    # And report them
    pprint(zip(names, results))

if __name__ == '__main__':

    device=raw_input('Enter Device :')
    b = bigsuds.BIGIP(hostname = device,username = 'admin', password = 'born2run',)
    wideips=b.GlobalLB.WideIP.get_list()
    wideipname=[]
    for wideip in wideips:
        wideipname.append(wideip.replace("/Common/",""))

    react(main, wideipname)
