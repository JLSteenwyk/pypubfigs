friendly_pals = {
    "bright_seven": ["#4477AA", "#228833", "#AA3377", "#BBBBBB", "#66CCEE", "#CCBB44", "#EE6677"],
    "contrast_three": ["#004488", "#BB5566", "#DDAA33"],
    "vibrant_seven": ["#0077BB", "#EE7733", "#33BBEE", "#CC3311", "#009988", "#EE3377", "#BBBBBB"],
    "muted_nine": ["#332288", "#117733", "#CC6677", "#88CCEE", "#999933", "#882255", "#44AA99", "#DDCC77", "#AA4499"],
    "nickel_five": ["#648FFF", "#FE6100", "#785EF0", "#FFB000", "#DC267F"],
    "ito_seven": ["#0072B2", "#D55E00", "#009E73", "#CC79A7", "#56B4E9", "#E69F00", "#F0E442"],
    "ibm_five": ["#648FFF", "#785EF0", "#DC267F", "#FE6100", "#FFB000"],
    "wong_eight": ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"],
    "tol_eight": ["#332288", "#117733", "#44AA99", "#88CCEE", "#DDCC77", "#CC6677", "#AA4499", "#882255"],
    "zesty_four": ["#F5793A", "#A95AA1", "#85C0F9", "#0F2080"],
    "retro_four": ["#601A4A", "#EE442F", "#63ACBE", "#F9F4EC"]
}

def friendly_pal(name, n=None, type='discrete'):
    pal = friendly_pals.get(name)
    if pal is None:
        raise ValueError(f"Palette '{name}' not found.")
    if n is None:
        n = len(pal)
    if type == 'discrete':
        if n > len(pal):
            raise ValueError("Requested more colors than palette provides.")
        return pal[:n]
    elif type == 'continuous':
        from matplotlib.colors import LinearSegmentedColormap
        cmap = LinearSegmentedColormap.from_list(name, pal)
        return [cmap(i / (n - 1)) for i in range(n)]
    else:
        raise ValueError("Type must be 'discrete' or 'continuous'.")
