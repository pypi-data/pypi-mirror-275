import matematikk as mt

def sannsynlighet_x_fra_mu_sd(
        mu                      = float(),
        sd                      = float(),
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
        _rand = mt.random.normal(mu, sd) # Alternativ: np.random.normal(mu, sd) med import numpy as np

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



def sannsynlighet_x_mindre_enn_fra_mu_sd(
        mu                      = float(),
        sd                      = float(),
        k_start                 = 0,
        k_ulikhetstegn          = ">",
        k_txt                   = "k",
        sim                     = int(),
        sannsyn_grense          = float(),
        sannsyn_grense_desimal  = -1,
        is_prosent              = -1,
        desimal                 = -1,
        is_debug                = -1,
        debug_txt_new_line      = 1,
        debug_txt_k             = "k              :: ",
        debug_txt_sannsyn       = "Sannsynlighhet :: ",
        is_print                = -1,
        print_x_txt             = "",
        is_print_tolkning       = 1,
        print_tolkning_txt      = "Praktisk tolkning:",
    ):

    # Bestem k slikat P(X <= k) = sannsyn_grense.
    # Gi en praktisk tolkning av svaret.

    # Oppg b)
    _sannsyn            = 0         # Sannsynligheten starter på 0 i while-løkken
    _k                  = k_start   # Starter på 0 og øker med k_ink
    _k_ink              = 1         # Steglengde som vi øker bremselengden med

    while _sannsyn < sannsyn_grense:

        # Debug
        if is_debug != -1:
            if debug_txt_new_line == 1: print("")
            print(f"{debug_txt_k}{_k}")
            print(f"{debug_txt_sannsyn}{_sannsyn}")

        _sannsyn = mt.sannsynlighet_x_fra_mu_sd( # sannsynlighet_x_fra_mu_sd_EX
            mu              = mu,
            sd              = sd,
            k               = _k,
            k_ulikhetstegn  = k_ulikhetstegn,
            sim             = sim,
            is_prosent      = is_prosent,
            desimal         = desimal,
            is_print        = is_print,
            print_txt       = print_x_txt,
        )

        _k += _k_ink

    # Avrunding
    if sannsyn_grense_desimal != -1: _sannsyn = round(_sannsyn, sannsyn_grense_desimal)

    # Tolkning
    if is_print_tolkning == 1:

        print("")
        if print_tolkning_txt == "Praktisk tolkning:": print(print_tolkning_txt)

        print(f"{_sannsyn} sannsynlighet for at {k_txt} er {k_ulikhetstegn} {_k} m")

    return _k


def sannsynlighet_gjennomsnitt_x_fra_mu_sd(
    mu                  = float(),
    sd                  = float(),
    x                   = float(),
    x_enhet             = str(),
    x_ulikhet           = ">",
    x_gjennomsnitt_ant  = int(),
    x_desimal           = -1,
    sim                 = int(),
    is_print            = -1
):

    # Nullstilling
    _x_enhet        = x_enhet
    _rand_ls        = list()
    _g_ls           = list()
    _rand_snitt     = float()
    _snitt_sannsyn  = float()

    # Mellomrom
    if _x_enhet != "": _x_enhet = " " + _x_enhet # Ikke def: _x_enhet =+ " "

    # Simulering f.eks. 100 000 ganger
    for _ in range(sim):

        # Husk å resette listen med tilfeldige verdier
        _rand_ls = []

        for _ in range(x_gjennomsnitt_ant):
            _rand = mt.random.normal(mu, sd) # np.random.normal(mu, sd) kan også brukes med import numpy as np
            _rand_ls.append(_rand)

        # Tag snittet av de 15 målingene
        _rand_snitt = mt.mean(_rand_ls)

        # Hvis snittet er mindre enn 84 telles denne som en gunstig
        if x_ulikhet == "<":
            if _rand_snitt < x: _g_ls.append(1)
        if x_ulikhet == ">":
            if _rand_snitt > x: _g_ls.append(1)

    # Sannsynlighet er definert som P = g / m
    _snitt_sannsyn = len(_g_ls) / sim

    # Hvis avrunding
    if x_desimal != -1: _snitt_sannsyn = round(_snitt_sannsyn, x_desimal)

    # Print
    if is_print == -1:
        print(f"Sannsynligheten for at gjennomsnittet av {x_gjennomsnitt_ant} ", )
        print(f"målinger er større en {x}{_x_enhet} er: {_snitt_sannsyn}")

    return _snitt_sannsyn



##########################################
# sannsynlighet_x_fra_mu_sd()
##########################################

# Alias > 1 > sannsynlighet_x_fra_mu_sd
sannsynlighet_X_fra_mu_sd       = sannsynlighet_x_fra_mu_sd
sannsynlighet_k_fra_mu_sd       = sannsynlighet_x_fra_mu_sd
sannsynlighet_gunstig_fra_mu_sd = sannsynlighet_x_fra_mu_sd

# Alias > 2 > sannsynlighet_x_fra_mu_sd > ...


##########################################
# sannsynlighet_x_mindre_enn_fra_mu_sd()
##########################################

# Alias > 1 > sannsynlighet_x_mindre_enn_fra_mu_sd > ...
sannsynlighet_x_storre_enn_fra_mu_sd = sannsynlighet_x_mindre_enn_fra_mu_sd

# Alias > 2 > sannsynlighet_x_mindre_enn_fra_mu_sd > ...


##########################################
# sannsynlighet_gjennomsnitt_x_fra_mu_sd()
##########################################

# Alias > 1 > sannsynlighet_x_mindre_enn_fra_mu_sd > ...
sannsynlighet_gjennomsnitt_x_mindre_fra_mu_sd = sannsynlighet_gjennomsnitt_x_fra_mu_sd

# Alias > 2 > sannsynlighet_x_mindre_enn_fra_mu_sd > ...

