import components
import traits
from components.Components import *
import traits.Hooks


class Drone:

    def __init__(self, owner, data, projects, plans, traits, info):
        self.owner = owner
        # Resource for creating projects and plans
        self.data = data
        # Executable Actions
        self.projects = projects
        # Blueprints for drones/traits
        self.plans = plans
        self.traits = traits
        self.info = info
        self.components = {
            "brain": Brain(self),
            "chassis": Chassis(self),
            "sensor": Sensor(self),
            "fabricator": Fabricator(self),
            "propulsion": Propulsion(self),
            "generator": Generator(self),
        }
