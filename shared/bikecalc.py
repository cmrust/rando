# Shared library for calculating bicycle specific measurements


def calculate_gear_ratios(min_chainring: int, max_chainring: int, min_cog: int, max_cog: int):
    """Returns a dictionary of gear ratios mapping cogs to chainrings."""
    gear_ratios = {}

    # '+ 1' on the top end of the range to include max value as well
    for cog in range(min_cog, max_cog + 1):
        gear_ratios[cog] = {}
        for chainring in range(min_chainring, max_chainring + 1):
            # round gear ratio to 2 decimal places
            gear_ratio = round(chainring / cog, 2)
            gear_ratios[cog][chainring] = gear_ratio

    # Note: It would probably make more sense, for legibility, to store them as gear_ratios[chainring][cog],
    # given that calculating the value is 'chaingring / cog', but storing it this way makes it easier to draw a table
    # row by row with chainrings along the top.

    return gear_ratios


def calculate_gear_ratios_rotated(min_chainring: int, max_chainring: int, min_cog: int, max_cog: int):
    """Returns a dictionary of gear ratios mapping cogs to chainrings."""
    gear_ratios = {}

    # '+ 1' on the top end of the range to include max value as well
    for chainring in range(min_chainring, max_chainring + 1):
        gear_ratios[chainring] = {}
        for cog in range(min_cog, max_cog + 1):
            # round gear ratio to 2 decimal places
            gear_ratio = round(chainring / cog, 2)
            gear_ratios[chainring][cog] = gear_ratio

    return gear_ratios
