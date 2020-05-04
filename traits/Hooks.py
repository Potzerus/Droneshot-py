def alter_attribute(attr, value, component=None):
    def predicate(drone):
        if component is not None:
            drone.components[component].__setattr__(attr, value)

    return predicate


trait_hooks = {
    "mod_attr": alter_attribute
}
