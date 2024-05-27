import matematikk as mt

def sannsynlighet_gunstig_fra_mu_st(
        mu          = float(),
        st          = float(),
        x           = float(),
        X           = float(),
        gunstig     = float(),
        sim         = int(),
        is_prosent  = -1,
        desimal     = -1,
        is_print    = -1,
        print_txt   = str()
    ):

    # Alias-argumenter
    _gunstig = float()
    if x        != float(): _gunstig = x
    if X        != float(): _gunstig = X
    if gunstig  != float(): _gunstig = gunstig

    # Interne variabeler
    _rand           = float()   # Generer tilfeldig verdi fra standard normalfordeling
    _gunstig_ls     = list()    # Lag liste for gunstige utfall
    _gunstig_ant    = list()    # Antall gunstige: Tell opp el i _gunstig_ls med len(_gunstig_ls)

    # ...
    for i in range(sim):

        # ...
        _rand = mt.random.normal(mu, st) # Alternativ: np.random.normal(mu, st) med import numpy as np

        # ...
        if _rand > _gunstig:
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
sannsynlighet_x_fra_mu_st       = sannsynlighet_gunstig_fra_mu_st
sannsynlighet_X_fra_mu_st       = sannsynlighet_gunstig_fra_mu_st

# Alias > 2 > ...
