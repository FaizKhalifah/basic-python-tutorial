def pertambahan(angka1, angka2):
    """Fungsi untuk melakukan penjumlahan dua angka."""
    return angka1 + angka2

def pengurangan(angka1, angka2):
    """Fungsi untuk melakukan pengurangan dua angka."""
    return angka1 - angka2

def perkalian(angka1, angka2):
    """Fungsi untuk melakukan perkalian dua angka."""
    return angka1 * angka2

def pembagian(angka1, angka2):
    """Fungsi untuk melakukan pembagian dua angka."""
    if angka2 == 0:
        raise ValueError("Pembagi tidak boleh nol.")
    return angka1 / angka2