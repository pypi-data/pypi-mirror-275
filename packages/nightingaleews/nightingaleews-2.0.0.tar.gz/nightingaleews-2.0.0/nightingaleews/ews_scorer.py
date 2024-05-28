def calculate_shock_index(hr, sbp):
    return hr/sbp


def calculate_gews_hr_points(hr):
    if hr>=130 or hr<=20:
        hr_points = 3
    elif (hr>=111 and hr <130) or (hr<40 and hr>20):
        hr_points = 2
    elif (hr>=101 and hr<111) or (hr<50 and hr>=40):
        hr_points = 1
    else:
        hr_points = 0
    return hr_points


def calculate_gews_rr_points(rr):
    if rr>=30:
        rr_points = 3
    elif (rr>=21 and rr<30) or (rr<9):
        rr_points = 2
    elif (rr>=15 and rr<21):
        rr_points = 1
    else:
        rr_points = 0
    return rr_points


def calculate_gews_sbp_points(sbp):
    if sbp<=70:
        sbp_points = 3
    elif (sbp>70 and sbp<=80) or (sbp>=200):
        sbp_points = 2
    elif (sbp>80 and sbp<=100):
        sbp_points = 1
    else:
        sbp_points = 0
    return sbp_points


def calculate_gews_dbp_points(dbp):
    if dbp<=40:
        dbp_points = 3
    elif (dbp>40 and dbp<=50) or (dbp>=120):
        dbp_points = 2
    elif (dbp>50 and dbp<=60):
        dbp_points = 1
    else:
        dbp_points = 0
    return dbp_points


def calculate_gews_spo2_points(spo2):
    if spo2<=90:
        spo2_points = 3
    elif (spo2>90 and spo2<=95):
        spo2_points = 2
    elif (spo2>95 and spo2<=98):
        spo2_points = 1
    else:
        spo2_points = 0
    return spo2_points


def calculate_gews(hr, rr, sbp, dbp, spo2):
    hr_points = 0 if hr == -1 else calculate_gews_hr_points(hr)
    rr_points = 0 if rr == -1 else calculate_gews_rr_points(rr)
    sbp_points = 0 if sbp == -1 else calculate_gews_sbp_points(sbp)
    dbp_points = 0 if dbp == -1 else calculate_gews_dbp_points(dbp)
    spo2_points = 0 if spo2 == -1 else calculate_gews_spo2_points(spo2)
    gews = hr_points + rr_points + sbp_points + dbp_points + spo2_points
    return gews, hr_points, rr_points, sbp_points, dbp_points, spo2_points