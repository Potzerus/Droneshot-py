import traits


# TODO: Implement Component Functionality here

class Component:
    # Dont make these directly use subclasses to access this
    def __init__(self, drone):
        # drone this is attached to
        self.drone = drone
        # What this component will do on the next tick
        self.plan = None
        # arguments for the planned function
        self.plan_args = []


class Brain(Component):
    base_stats = {
        # convert sensor input into data
        'analysis': 1,
        # convert data into projects
        'computation': 1,
        # how many other drones this can pilot
        'control': 0,
        # convert data into plans for fabricator
        'design': 1,
        # what impact it has on the energy grid while active
        'energy': -3
    }

    def __init__(self, drone):
        super().__init__(drone)


class Chassis(Component):
    base_stats = {
        # standard hp
        'health': 10,
        # for propulsion calculation
        'weight': 10,
    }

    def __init__(self, drone):
        super().__init__(drone)


class Fabricator(Component):
    base_stats = {
        # Tier of Components/Traits that can be made
        'tier': 0,
        # how much energy it consumes while active
        'energy': -1,
    }

    def __init__(self, drone):
        super().__init__(drone)


class Propulsion(Component):
    base_stats = {
        # maximum force (use for planet escape calc?)
        'thrust': 0,
        # How much fuel is consumed per tick while active
        'consumption': 0,
    }

    def __init__(self, drone, fuel=None):
        super().__init__(drone)
        self.fuel = fuel


class Generator(Component):
    base_stats = {
        # How much energy one unit of fuel is converted into
        "efficiency": 0,
        # up to how many units can be consumed in one tick
        "max capacity": 0,
    }

    def __init__(self, drone, fuel=None):
        super().__init__(drone)
        self.fuel = fuel


class Sensor(Component):
    base_stats = {
        # How good at picking up each type of stimulus the sensor is
        "visual": 0,
        "auditory": 0,
        "electromagnetic": 0,
        "chemical": 0,
    }

