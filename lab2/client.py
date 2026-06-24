import Pyro4

greeting = Pyro4.Proxy("PYRONAME:example.greeting")

print(greeting.say_hello())