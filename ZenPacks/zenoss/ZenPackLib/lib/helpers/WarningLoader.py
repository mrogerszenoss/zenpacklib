from .Loader import Loader

class WarningLoader(Loader):
    """
        These subclasses exist so that each copy of zenpacklib installed on a
        zenoss system provide their own loader (for add_constructor and yaml.load)
        and its own dumper (for add_representer) so that the proper methods will
        be used for this specific zenpacklib.
    """
    warnings = True
    yaml_errored = False