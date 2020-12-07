"""
This module uses Python to query different endpoints using the 
NiFi REST API.
"""
import requests
import pprint

# System Diagnostics
r = requests.get('http://localhost:9300/nifi-api/system-diagnostics')
data = r.json()

print('Aggregte Snapshot:\n'
      '==================')
print('Max Heap: {0}'.format(
    data['systemDiagnostics']['aggregateSnapshot']['maxHeap']))
print('Total Threads: {0}'.format(
    data['systemDiagnostics']['aggregateSnapshot']['totalThreads']))
print('Heap Utilization: {0}'.format(
    data['systemDiagnostics']['aggregateSnapshot']['heapUtilization']))
print('')

# Processor Groups
pg = requests.get('http://localhost:9300/nifi-api/process-groups/01761002-6e6d-1e28-3038-c32c45328032')
pgdata = pg.json()

print('Processor Group:\n'
      '================')
print('Component Name: {0}'.format(pgdata['component']['name']))
print('Status:')
pprint.pprint(pgdata['status'])
print('')

# Single Processor
p = requests.get('http://localhost:9300/nifi-api/processors/215ab91d-90c7-3e63-219e-80a21faee5c8')
pdata = p.json()

print('Single Processor:\n'
      '=================')
print('Component name: {0}'.format(pdata['component']['name']))
print('Status:')
pprint.pprint(pdata['status'])
print('')

# Make a listing request to queue
q = requests.post(
        'http://localhost:9300/nifi-api/flowfile-queues/dcec54be-3777-36a0-1d06-be5fc54a25c3/listing-requests')
qdata = q.json()

print('Queue List:\n'
      '===========')
print('List id: {0}'.format(qdata['listingRequest']['id']))
print('')

url = "http://localhost:9300/nifi-api/flowfile-queues/" + \
      "dcec54be-3777-36a0-1d06-be5fc54a25c3/listing-requests/" + \
      qdata['listingRequest']['id']

ff = requests.get(url)
ffdata = ff.json()

print('Request uuid:\n'
      '=============')
print('Id: {0}'.format(ffdata['listingRequest']['flowFileSummaries'][0]['uuid']))
print('')

ffurl = "http://localhost:9300/nifi-api/flowfile-queues/" + \
      "dcec54be-3777-36a0-1d06-be5fc54a25c3/flowfiles/" + \
      ffdata['listingRequest']['flowFileSummaries'][0]['uuid'] + \
      "/content"

print('Request Content:\n'
      '================')
print('Content:')
download = requests.get(ffurl)
pprint.pprint(download.json())
print('')

# Empty queue
e = requests.post('http://localhost:9300/nifi-api/flowfile-queues/' + \
        'dcec54be-3777-36a0-1d06-be5fc54a25c3/drop-requests')
edata = e.json()

# Read Bulletin
b = requests.get('http://localhost:9300/nifi-api/flow/bulletin-board')
bdata = b.json()
print('Bulletin:\n'
      '=========')
print('Content:')
pprint.pprint(bdata)
print('')

# Read Counters
c = requests.get('http://localhost:9300/nifi-api/counters')
cdata = c.json()
print('Counters:\n'
      '=========')
pprint.pprint(cdata)
