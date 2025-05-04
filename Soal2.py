def tampilkan_soal(file1):
    print(f"nama file1: {file1}")

    with open(file1, 'r') as f:
        for baris in f:
            if '||' in baris:
                soal, jawaban_benar = baris.strip().split('||')
                soal = soal.strip()
                jawaban_benar = jawaban_benar.strip().lower()

                print(f"{soal}")
                jawaban_user = input("Jawab: ").strip().lower()

                if jawaban_user == jawaban_benar:
                    print("Jawaban benar!\n")
                else:
                    print("Jawaban salah!\n")
 
