def bandingkan_file(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        baris1 = f1.readlines()
        baris2 = f2.readlines()

        max_baris = max(len(baris1), len(baris2))
        print("Perbandingan isi file:\n")

        for i in range(max_baris):
            teks1 = baris1[i].strip() if i < len(baris1) else ''
            teks2 = baris2[i].strip() if i < len(baris2) else ''

            if teks1 != teks2:
                print(f"Baris {i+1}:")
                print(f"  File 1: {teks1}")
                print(f"  File 2: {teks2}\n")
