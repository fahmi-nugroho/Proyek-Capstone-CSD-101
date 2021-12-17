import numpy as np

def reshape(umur, jenisKelamin, polyuria, polydipsia, penurunanBB, lemas, nafsuMakan, infeksiKelamin, pandangan, gatal, mood, penyembuhan, gerakanBadan, otot, rambut, obesitas):
    test_data = [
        umur,
        jenisKelamin,
        polyuria,
        polydipsia,
        penurunanBB,
        lemas,
        nafsuMakan,
        infeksiKelamin,
        pandangan,
        gatal,
        mood,
        penyembuhan,
        gerakanBadan,
        otot,
        rambut,
        obesitas
    ]

    test_data = np.array(test_data)
    test_data = test_data.reshape(1, -1)

    return test_data