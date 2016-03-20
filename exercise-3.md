# Exercise 3 - following relations


## Part 1 - getting an instance (row) and following its relations


With and ORM, not only do you have access to that row's attributes, but the ORM will follow relations by treating them as attributes or methods. 

    log = Log.objects.last()
    log.user

Say you have the ship the USS Ares

    ship = Ship.objects.get(name='USS Ares')
    ship.logs.count()

    print(ship.logs.all().query)


Considering that in the example `ship.logs.filter` is similar to `Log.objects.filter`, how many ship logs are captain's logs?
