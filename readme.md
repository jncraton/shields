Shields
=======

A simulated spacecraft

Learning Outcomes
-----------------

After completing this lab, students will be able to:
    
1. Use `@property` to create getters in Python
2. Protect data using private attributes
3. Use `@x.setter` to create setters in Python

Tasks
-----

1. Complete the `Subsystem` class
    1. Create getter for `power` using `@property`
    2. Create a setter for `power` using `@power.setter`
        - Be sure to raise a value error if a user attempts to set a negative power
2. Complete the `Ship` class
    1. Complete the `shutdown` method to take all systems offline and consume no power
    2. Complete the `raise_shields_to_maximum` method that diverts all power to shields and shuts down all other systems
    3. Complete the `apply_damage` method to apply hull damage to the ship
    4. Complete the `get_available_energy` method to determine how much free energy is available
    5. Create getters and setters for `shields`, `weapons`, and `engines`. Raise a ValueError if there is not enough energy to satisfy a request or negative values are provided
