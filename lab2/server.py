import Pyro4

@Pyro4.expose
class Greeting:
    def say_hello(self):
        return "Welcome to Distributed Systems Laboratory"

daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(Greeting)
ns.register("example.greeting", uri)

print("Server is ready...")
daemon.requestLoop()