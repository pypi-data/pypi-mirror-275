import matematikk as mt

def sannsynlighet_x_fra_mu_sd(
    oppg                    = str(),
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
    print_txt               = str(),
    is_innhuk               = int()):

    # Print oppg
    if oppg != str():
        print("")
        print(oppg)

    # Interne variabeler
    _rand               = float()   # Generer tilfeldig verdi fra standard normalfordeling
    _gunstig            = float()   # Gunstig, x, X, k
    _gunstig_ls         = list()    # Lag liste for gunstige utfall
    _gunstig_ant        = list()    # Antall gunstige: Tell opp el i _gunstig_ls med len(_gunstig_ls)
    _prosent_sym        = ""        # Blir % hvis avrunding
    _x_ulikhetstegn     = ">"       # Default
    _innhuk             = ""        # Itererer frem et str-innhuk

    # Alias-argumenter > Gunstig
    if x        != float(): _gunstig = x
    if X        != float(): _gunstig = X
    if k        != float(): _gunstig = k
    if gunstig  != float(): _gunstig = gunstig

    # Alias-argumenter > Gunstig
    if x_ulikhetstegn       != ">": _x_ulikhetstegn = x_ulikhetstegn
    if X_ulikhetstegn       != ">": _x_ulikhetstegn = X_ulikhetstegn
    if k_ulikhetstegn       != ">": _x_ulikhetstegn = k_ulikhetstegn
    if gunstig_ulikhetstegn != ">": _x_ulikhetstegn = gunstig_ulikhetstegn

    # Simulering
    for i in range(sim):

        # Trekk en tilfeldig verdi i fra normal-fordelingen
        _rand = mt.random.normal(mu, sd) # Alternativ: np.random.normal(mu, sd) med import numpy as np

        # Gunstig > Større eller mindre
        if _x_ulikhetstegn == ">":
            if _rand > _gunstig:    _gunstig_ls.append(_rand)
        if _x_ulikhetstegn == "<":
            if _rand < _gunstig:    _gunstig_ls.append(_rand)

    # Antall gunstige el i listen
    _gunstig_ant = len(_gunstig_ls)

    # Sannsynlighet er definert som P = g / m
    sannsyn = (_gunstig_ant / sim)

    # Hvis prosent-konvertering
    if is_prosent   != -1:
        _prosent_sym = " %"
        sannsyn *= 100

    # Hvis avrunding
    if desimal      != -1: sannsyn = round(sannsyn, desimal)

    # Hvis innhuk
    if is_innhuk    != -1:
        for _ in range(is_innhuk):
            _innhuk += " "
        _innhuk + " "

    # Hvis printing
    if is_print     != -1:

        print(f"")
        if print_txt != str():
            print(f"{_innhuk}{print_txt}{sannsyn}{_prosent_sym}")

        if print_txt == str():
            print(f"{_innhuk}Sannsynligheten for x {_x_ulikhetstegn} {_gunstig} er: {sannsyn}{_prosent_sym}")

    return sannsyn



def sannsynlighet_x_mindre_enn_fra_mu_sd(
        oppg                    = str(),
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
        is_debug_farge          = -1,
        debug_farge             = "grønn",
        is_print                = -1,
        print_x_txt             = "",
        is_print_tolkning       = 1,
        print_tolkning_txt      = "Praktisk tolkning:",
        is_innhuk               = -1):

    # Print oppg
    if oppg != str():
        print("")
        print(oppg)

    # Bestem k slikat P(X <= k) = sannsyn_grense.
    # Gi en praktisk tolkning av svaret.

    # Interne variabler
    _sannsyn            = 0         # Sannsynligheten starter på 0 i while-løkken
    _k                  = k_start   # Starter på 0 og øker med k_ink
    _k_ink              = 1         # Steglengde som vi øker bremselengden med
    _innhuk             = ""        # Itererer frem et str-innhuk

    # Kjør så lenge sannsynligheten er mindre en grensen
    while _sannsyn < sannsyn_grense:

        # Debug
        if is_debug != -1:

            # Ny linje
            if debug_txt_new_line == 1: print("")

            # Txt
            _debug_txt_1 = f"{debug_txt_k}{_k}"
            _debug_txt_2 = f"{debug_txt_sannsyn}{_sannsyn}"

            # Farge
            # - Alternativ
            # - $ pip install colorama
            # - import colorama
            # - min_farge_txt = f"{colorama.Fore.GREEN}min_txt{colorama.Style.RESET_ALL}"
            # - print(min_farge_txt)

            if is_debug_farge != -1: _debug_txt_1 = mt.farge_txt(_debug_txt_1, debug_farge)
            if is_debug_farge != -1: _debug_txt_2 = mt.farge_txt(_debug_txt_2, debug_farge)

            print(_debug_txt_1)
            print(_debug_txt_2)

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

    # Hvis avrunding
    if sannsyn_grense_desimal != -1: _sannsyn = round(_sannsyn, sannsyn_grense_desimal)

    # Hvis innhuk
    if is_innhuk != -1:
        for _ in range(is_innhuk): _innhuk += " "
        _innhuk + " "

    # Tolkning
    if is_print_tolkning == 1:

        print("")
        if print_tolkning_txt != -1:

            if print_tolkning_txt == "Praktisk tolkning:":

                print(f"{_innhuk}- {print_tolkning_txt}")

            print(f"{_innhuk}- {_sannsyn} sannsynlighet for at {k_txt} er {k_ulikhetstegn} {_k} m")

    return _k



def sannsynlighet_gjennomsnitt_x_fra_mu_sd(
    oppg                = str(),
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

    # Print oppg
    if oppg != str():
        print("")
        print(oppg)

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
    if is_print != -1:
        print(f"")
        print(f"Sannsynligheten for at gjennomsnittet av {x_gjennomsnitt_ant} ", )
        print(f"målinger er større en {x}{_x_enhet} er: {_snitt_sannsyn}")

    return _snitt_sannsyn

def sannsynlighet_hypotese_test_fra_mu_sd(
    oppg                        = str(),
    mu                          = float(),
    sd                          = float(),
    x_liste                     = list(),
    x_liste_kontroll_faktor     = None,
    x_ulikhetstegn              = ">",
    sim                         = int(),
    signifikans                 = float(),
    sannsyn_desimal             = -1,
    is_prosent                  = -1,
    is_print                    = -1,
    print_hypotese_0_txt        = str(),
    print_hypotese_1_txt        = str(),
    is_farge                    = -1,
    farge_hypotese_0            = str(),
    farge_hypotese_1            = str()):

    # Print oppg
    if oppg != str(): print(""); print(oppg)

    # H_0:  Bremselengden er 83 m eller kortere (nullhypotese)
    # H_1:  Bremselengden er lengre enn 83 m (alternativ hypotese)

    # Variabler
    _prosent_sym = ""

    # Kontroll
    if x_liste_kontroll_faktor != None:

        # Ganger med en faktor som gjør at målingene faller utenfor signifikans-nivået
        for i in range(len(x_liste)):
            x_liste[i] *= x_liste_kontroll_faktor

    # Snittet av testmålingene
    _x_snitt_mu = mt.mean(x_liste) # Alternativ: numpy.mean(x_liste)

    # σ_snitt = σ / √n
    _snitt_sd = sd / mt.sqrt(len(x_liste)) # Alternativ: numpy.sqrt(brems_snitt_ant)

    # Regner ut sannsynligheten med st fra normalfordelingen
    _test_sannsyn = mt.sannsynlighet_x_fra_mu_sd(
        mu              = mu,
        sd              = _snitt_sd,
        x               = _x_snitt_mu,
        x_ulikhetstegn  = x_ulikhetstegn,
        sim             = sim,
        is_prosent      = -1,
        desimal         = -1,
        is_print        = -1,
        print_txt       = str())

    # Prosent
    if is_prosent != -1:

        _test_sannsyn   *= 100
        signifikans     *= 100
        _prosent_sym    = " %"

    # Avrunding
    if sannsyn_desimal != -1:

        _test_sannsyn   = round(_test_sannsyn,  sannsyn_desimal)
        signifikans     = round(signifikans,   sannsyn_desimal)

    # Print svar
    if is_print != -1:
        _txt_0_1 = f"- Hypotese-testen gir at {_test_sannsyn}{_prosent_sym} > {signifikans}{_prosent_sym} (signifikans-nivået)"
        _txt_0_2 = f"- Det er mer enn {signifikans}{_prosent_sym} sannsynlighet for at H_0 er riktig"
        _txt_0_3 = f"- {print_hypotese_0_txt} kan IKKE forkaste nullhypotesen"
        _txt_0_4 = f"- {print_hypotese_1_txt} har sannsynligvis rett"

        _txt_1_1 = f"- Hypotese-testen gir at {_test_sannsyn}{_prosent_sym} < {signifikans}{_prosent_sym} (signifikans-nivået)"
        _txt_1_2 = f"- Det er mer enn {signifikans}{_prosent_sym} sannsynlighet for at H_1 er riktig"
        _txt_1_3 = f"- {print_hypotese_0_txt} kan forkaste nullhypotesen"
        _txt_1_4 = f"- {print_hypotese_1_txt} tar sannsynligvis feil"

        # Farge
        # - Alternativ
        # - $ pip install colorama
        # - import colorama
        # - min_farge_txt = f"{colorama.Fore.GREEN}min_txt{colorama.Style.RESET_ALL}"
        # - print(min_farge_txt)
        if is_farge != -1:
            _txt_0_1 = mt.farge_txt(_txt_0_1, farge_hypotese_0)
            _txt_0_2 = mt.farge_txt(_txt_0_2, farge_hypotese_0)
            _txt_0_3 = mt.farge_txt(_txt_0_3, farge_hypotese_0)
            _txt_0_4 = mt.farge_txt(_txt_0_4, farge_hypotese_0)
        if is_farge != -1:
            _txt_1_1 = mt.farge_txt(_txt_1_1, farge_hypotese_1)
            _txt_1_2 = mt.farge_txt(_txt_1_2, farge_hypotese_1)
            _txt_1_3 = mt.farge_txt(_txt_1_3, farge_hypotese_1)
            _txt_1_4 = mt.farge_txt(_txt_1_4, farge_hypotese_1)

        # Mer enn 5 % sannsynlighet for at H_0 er riktig
        if _test_sannsyn > signifikans:
            print("")
            print(_txt_0_1)
            print(_txt_0_2)
            print(_txt_0_3)
            print(_txt_0_4)

        # Mindre enn 5 % sannsynlighet for at H_0 er riktig
        if _test_sannsyn < signifikans:
            print("")
            print(_txt_1_1)
            print(_txt_1_2)
            print(_txt_1_3)
            print(_txt_1_4)

    return _test_sannsyn



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


##########################################
# sannsynlighet_hypotese_test_fra_mu_sd()
##########################################

# Alias > 1 > sannsynlighet_hypotese_test_fra_mu_sd > ...

# Alias > 2 > sannsynlighet_hypotese_test_fra_mu_sd > ...

