import rpyc

connection = rpyc.connect('localhost', 18861)

remote_service = connection.root

# we can now access the exposed service's function:
print(remote_service.get_answer())
print(remote_service.attribute)
try:
    print(remote_service.some_other_function())
except:
    print('could not access some_other_function() on remote_service')
