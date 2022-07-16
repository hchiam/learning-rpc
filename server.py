import rpyc
from rpyc.utils.server import ThreadedServer


class MyService(rpyc.Service):
    def on_connect(self, connection):  # specially-named listener method
        print(connection)

    def on_disconnect(self, connection):  # specially-named listener method
        print(connection)

    # the "exposed_" prefix tells rpyc to expose it to the client:
    def exposed_get_answer(self):
        return 'get_answer() is exposed to client'

    # the "exposed_" prefix tells rpyc to expose it to the client:
    exposed_attribute = 'attribute is exposed to client'

    # this method ISN'T exposed to client because it's missing the "exposed_" prefix:
    def some_other_function(self):
        return "some_other_function shouldn't be exposed to the client"


thread = ThreadedServer(MyService, port=18861, protocol_config={})
thread.start()
