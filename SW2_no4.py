def eight():
    banana_cue_pcs = int(input("how many banana cue were sold? "))
    turon_pcs = int(input("how many turon were sold? "))
    maruya_pcs = int(input("how many maruya were sold? "))

    total_pcs = banana_cue_pcs + turon_pcs + maruya_pcs

    banana_cue_percent = 100.0 * banana_cue_pcs / total_pcs
    turon_percent = 100.0 * turon_pcs / total_pcs
    maruya_percent = 100.0 * maruya_pcs / total_pcs

    print("Banana Cue accounts for approximately %.1f%% of the sales" % banana_cue_percent)
    print("Turon accounts for approximately %.1f%% of the sales" % turon_percent)
    print("Maruya accounts for approximately %.1f%% of the sales" % maruya_percent)

eight()