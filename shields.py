class Subsystem:
    """
    Class to store and manage individual ship subsystems
    """

    def __init__(self, power):
        """Constructor to set initial power consumed"""
        self._power = power


sys = Subsystem(1)
assert sys.power == 1
sys.power = 3
assert sys.power == 3
try:
    sys.power = -1
except ValueError:
    pass
assert sys.power == 3
assert sys.online == True
sys.power = 0
assert sys.power == 0
assert sys.online == False


class Ship:
    """
    Class to represent on spacecraft
    """

    def __init__(self):
        self._hull = 100
        self._shields = Subsystem(1)
        self._weapons = Subsystem(1)
        self._engines = Subsystem(1)
        self._reactor_output = 5
        self._subsystems = [self._shields, self._weapons, self._engines]

    def shutdown(self):
        """Shutdown all systems"""

    def raise_shields_to_maximum(self):
        """Move all power to the shields"""

    def apply_damage(self, damage):
        """Applies hull damage less current shield level"""

    def get_available_energy(self):
        """
        Return the available ship energy

        This is the reactor output minor energy used by
        subsystems
        """


# Tests

s = Ship()
assert s._shields.power == 1
assert s._engines.power == 1
assert s._weapons.power == 1
s.shutdown()
assert s._shields.power == 0
assert s._engines.power == 0
assert s._weapons.power == 0

s = Ship()
assert s._shields.power == 1
s.raise_shields_to_maximum()
assert s._shields.power == 5
assert s._engines.power == 0
assert s._weapons.power == 0

s = Ship()
assert s._hull == 100
s.apply_damage(6)
assert s._hull == 95
s.raise_shields_to_maximum()
s.apply_damage(3)
assert s._hull == 95
s.shutdown()
s.apply_damage(4)
assert s._hull == 91

s = Ship()
assert s.get_available_energy() == 2
s.shutdown()
assert s.get_available_energy() == 5
s.raise_shields_to_maximum()
assert s.get_available_energy() == 0
s.shutdown()

s = Ship()
assert s.shields == 1
s.shields = 2
assert s.shields == 2
s.shields = 3
assert s.shields == 3
try:
    s.shields = 4
except ValueError:
    pass
assert s.shields == 3
try:
    s.shields = -2
except ValueError:
    pass
assert s.shields == 3

s = Ship()
assert s.weapons == 1
s.weapons = 2
assert s.weapons == 2
s.weapons = 3
assert s.weapons == 3
try:
    s.weapons = 4
except ValueError:
    pass
assert s.weapons == 3
try:
    s.weapons = -2
except ValueError:
    pass
assert s.weapons == 3

s = Ship()
assert s.engines == 1
s.engines = 2
assert s.engines == 2
s.engines = 3
assert s.engines == 3
try:
    s.engines = 4
except ValueError:
    pass
assert s.engines == 3
try:
    s.engines = -2
except ValueError:
    pass
assert s.engines == 3
