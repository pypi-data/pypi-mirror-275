import matematikk as mt

def sannsynlighet_x_fra_mu_st(
        mu                      = float(),
        st                      = float(),
        x                       = float(),
        x_ulikhetstegn          = ">",
        X                       = float(),
        X_ulikhetstegn          = ">",
        k                       = float(),
        k_ulikhetstegn          = ">",
        gunstig                 = float(),
        gunstig_ulikhetstegn    = ">",
        sim                     = int(),
        is_prosent              = -1,
        desimal                 = -1,
        is_print                = -1,
        print_txt               = str()
    ):

    # Alias-argumenter > Gunstig
    _gunstig = float()
    if x        != float(): _gunstig = x
    if X        != float(): _gunstig = X
    if k        != float(): _gunstig = k
    if gunstig  != float(): _gunstig = gunstig

    # Alias-argumenter > Gunstig
    _x_ulikhetstegn = ">"
    if x_ulikhetstegn       != ">": _x_ulikhetstegn = x_ulikhetstegn
    if X_ulikhetstegn       != ">": _x_ulikhetstegn = X_ulikhetstegn
    if k_ulikhetstegn       != ">": _x_ulikhetstegn = k_ulikhetstegn
    if gunstig_ulikhetstegn != ">": _x_ulikhetstegn = gunstig_ulikhetstegn

    # Interne variabeler
    _rand           = float()   # Generer tilfeldig verdi fra standard normalfordeling
    _gunstig_ls     = list()    # Lag liste for gunstige utfall
    _gunstig_ant    = list()    # Antall gunstige: Tell opp el i _gunstig_ls med len(_gunstig_ls)

    # ...
    for i in range(sim):

        # ...
        _rand = mt.random.normal(mu, st) # Alternativ: np.random.normal(mu, st) med import numpy as np

        # ...
        if _x_ulikhetstegn == ">":
            if _rand > _gunstig:
                _gunstig_ls.append(_rand)
        if _x_ulikhetstegn == "<":
            if _rand < _gunstig:
                _gunstig_ls.append(_rand)

    # Antall gunstige el i listen
    _gunstig_ant = len(_gunstig_ls)

    # Sannsynlighet er definert som P = g / m
    sannsyn = (_gunstig_ant / sim)

    # Hvis svaret skal konverteres til prosent
    if is_prosent   != -1: sannsyn *= 100

    # Hvis svaret skal avrundes
    if desimal      != -1: sannsyn = round(sannsyn, desimal)

    # Hvis svaret skal avrundes
    if is_print     != -1: print(f"{print_txt}{sannsyn} %")

    return sannsyn
 

# Alias > 1
sannsynlighet_X_fra_mu_st       = sannsynlighet_x_fra_mu_st
sannsynlighet_k_fra_mu_st       = sannsynlighet_x_fra_mu_st
sannsynlighet_gunstig_fra_mu_st = sannsynlighet_x_fra_mu_st

# Alias > 2 > ...
