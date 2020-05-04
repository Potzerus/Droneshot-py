import json
from traits.Modifier import Modifier


class Trait:
    def __init__(self, modifiers, hooks = None):
        # subtraits are dicts with affected component as key and dict with modifiers as values
        self.modifiers = {}
        for component in modifiers:
            self.modifiers[component] = {}
        for component, stat in modifiers.items:
            for k, v in stat.items():
                self.modifiers[component][stat] = Modifier(**v)


    @classmethod
    def get_trait(cls, trait_name):
        traits = json.loads(open("Traits.json").read())
        if trait_name in traits:
            trait = traits[trait_name]
            return Trait(trait)
