import streamlit as st


st.set_page_config(
    page_title="SmartInvest",
    # page_icon="💵"
)
menu = st.sidebar.selectbox("Menu",("Home","About Us","How To Invest","How To Use"))
st.markdown(
    """
    <style>
        .centered-title {
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Menampilkan title di tengah
st.markdown("<h1 class='centered-title'> 📈 SmartInvest  📈</h1>  ", unsafe_allow_html=True)
if menu == "Home":
    def home_page ():
        st.header("Kenapa ada SmartInvest ?")
        st.write("Alasan utama SmartInvest ini untuk memberikan saran dan bimbingan kepada individu atau entitas yang ingin mengelola dan mengoptimalkan investasi")
        st.header("Apa saja yang dapat dilakukan SmartInvest pada Web ini ?")
        st.write("""1. Penilaian Tujuan Keuangan:
Menganalisis tujuan keuangan klien, seperti pensiun, pendidikan anak, atau pembelian properti, untuk merancang strategi investasi yang sesuai.
2. Pemantauan Pasar:
Memantau kondisi pasar dan tren investasi, serta memberikan pembaruan kepada klien tentang perubahan yang mungkin mempengaruhi portofolio mereka. 
3. Rekomendasi Investasi: 
Memberikan saran tentang instrumen investasi spesifik yang sesuai dengan tujuan klien, termasuk saham, obligasi, reksa dana, dan asetlainnya.        
4. Edukasi Investasi: 
Memberikan edukasi kepada klien tentang berbagai instrumen investasi, konsep keuangan, dan strategi manajemen risiko.
5. Konseling Keuangan Umum: 
Kadang-kadang memberikan saran lebih luas tentang aspek keuangan, termasuk pengelolaan hutang, perencanaan warisan, dan lainnya. 
\nNote : Konseling Keuangan ini bisa melalui idis bot yang terdapat pada menu IDIS BOT.                     
        """)
        st.write(""" """)
        st.header("WARNING ❗❗❗")
        st.write("Investasi adalah hal yang beresiko  ")
    home_page()
if menu == "About Us":
    def about_page():
        st.header("Tentang Kami")
        st.markdown("Kami dari Kelompok 10 : ")
        st.text("""1. Meira Listyaningrum_122450011
2. Farrel Julio Akbar_122450110
3. Tria Yunani_122450062
4. Renta Siahaan_122450070
5. M.Deriansyah Okutra_122450101""")
        st.write('Web ini sebagai tugas besar kami dan untuk nilai ALPRO kami.')
    about_page()
if menu == "How To Invest" :
    def how_to_invest():
        st.header("Cara Menggunakan Investasi")
        st.markdown('''Menggunakan investasi melibatkan beberapa langkah penting. Berikut adalah panduan umum tentang cara menggunakan investasi:

                \n - Tentukan Tujuan Investasi:
                \nIdentifikasi tujuan finansial Anda. Apakah itu untuk dana pensiun, pendidikan anak, atau pertumbuhan kekayaan jangka panjang? Mengetahui tujuan akan membantu Anda menentukan strategi investasi yang sesuai.
                \n - Kenali Profil Risiko dan Toleransi Risiko:
                \nTentukan seberapa besar risiko yang bersedia Anda ambil. Profil risiko dan toleransi risiko Anda akan memengaruhi jenis investasi yang paling sesuai untuk Anda, apakah itu saham, obligasi, atau instrumen investasi lainnya.
                \n - Pahami Jenis Investasi:
                \nPelajari berbagai jenis investasi seperti saham, obligasi, reksa dana, properti, dan lainnya. Pahami karakteristik masing-masing jenis investasi, termasuk potensi keuntungan dan risiko.
                \n - Buat Portofolio Investasi yang Diversifikasi:
                \nDiversifikasi dapat membantu mengurangi risiko. Sebaiknya jangan meletakkan semua dana investasi Anda pada satu jenis aset atau satu sektor. Sebaliknya, alokasikan dana Anda di berbagai jenis investasi.
                \n - Riset dan Analisis:
                \nLakukan riset tentang perusahaan atau instrumen investasi yang Anda pertimbangkan. Pelajari kinerja historis, prospek masa depan, dan faktor-faktor yang dapat memengaruhi investasi tersebut.
                \n - Buat Rencana Keuangan:
                \nSusun rencana keuangan yang mencakup strategi investasi Anda. Tetapkan target keuangan, tenggat waktu, dan rencana darurat.
                \n - Pilih Pialang atau Platform Investasi:
                \nJika Anda tidak memiliki pengalaman langsung dalam investasi, pertimbangkan untuk menggunakan jasa pialang atau platform investasi. Pilih pialang atau platform yang dapat memberikan akses ke berbagai instrumen investasi dan menyediakan alat analisis yang berguna.
                \n - Monitor dan Evaluasi:
                \nPantau secara teratur kinerja portofolio investasi Anda. Sesuaikan portofolio jika ada perubahan dalam tujuan keuangan, profil risiko, atau kondisi pasar.
                \n - Reinvestasi Keuntungan:
                \nPertimbangkan untuk reinvestasi keuntungan yang Anda peroleh. Reinvestasi dapat meningkatkan potensi pertumbuhan portofolio Anda.
                \n - Tetap Disiplin dan Sabar:
                \nInvestasi memerlukan disiplin dan kesabaran. Jangan tergoda untuk melakukan keputusan investasi berdasarkan emosi atau perubahan pasar yang jangka pendek.
                    
                \nIngatlah bahwa investasi selalu melibatkan risiko, dan hasil masa lalu tidak menjamin hasil di masa depan. Oleh karena itu, penting untuk terus memperbarui pengetahuan Anda tentang pasar keuangan dan tetap beradaptasi dengan perubahan kondisi ekonomi. Jika Anda merasa kesulitan atau tidak yakin, pertimbangkan untuk berkonsultasi dengan seorang penasihat keuangan profesional.''')
    how_to_invest()

if menu == "How To Use" :
    def how_to_use():
        st.header("Penjelasan Penggunaan Web APK ini ")
        st.markdown('\n - Menu Home, Terdapat beberapa selected yaitu :')
        st.write("""1. Home : Terdapat penjelasan SmartInvest dari web kami ini
2. About Us : Berisi tentang kami
3. How To Use : Penjelasan penggunaan Web 
                 """)
        st.markdown('\n - Menu Login : ')
        st.write('''1. sebelum melakukan login user harus registrasi terlebih dahulu dengan memasukkan, Nama lengkap, Tanggal lahir, Username, Password.
2. stelah registrasi baru user bisa login dengan memasukkan username, dan password yang telah ter-registrasi
3. stelah login berhasil, user langsung masuk ke penjelasan investasi dari Tabungan, Saham, Emas, Obligasi, Deposito, dan Reksadana
4. dan terdapat Logout jika user mau Logout''')
        st.write('Noted : Ada beberapa menu yang tidak terbuka jika user belum login, seperti menu IDIS BOT, dan Stocks Realtime ')
        st.markdown('\n - Menu IDIS BOT : ')
        st.write('''Nah pada menu ini user dapat menanyakan apa saja tentang investasi kepada IDIS BOT, contoh pertanyaan-nya: 
1. Apa itu investasi ?
2. Jika saya mempunyai uang ..... bagusnya saya investasi kemana ?
3. Bedanya Tabungan dengan Investasi ?
4. Apa saja keuntungan investasi ?
5. Apa saja resiko dari investasi ?
6. dan lain-lainnya tentang investasi !''')
        st.write('Semua kebingung pengguna tentang keuangan ataupun investasi bisa ditanyakan pada BOT IDIS ini dan tentunya akan dijawab langsung oleh BOT IDIS ini.')
        st.markdown('\n - Menu Stocks Realtime : ')
        st.write('''Pada menu ini terdapat Real-time stock analiytics yang berupa info grafis dan ada 2 grafik yang berbeda yg ditampilkan pada menu ini  : ''')
        st.write('sebelum ke grafik kita bisa memilih saham apa yang ingin kita lihat grafiknya pada fitur (Enter Stock Symbol).contoh symbolnya seperti AAPL, BBSI, ASII, dan lain-lain.')
        st.write('setelah itu user juga bisa memilih jangka waktu yang di inginkan pada fitur (Select Time Frame) jangka waktunya dari 0-100, semakin kecil waktu yang dipilih maka grafik semakin jelas,semakin besar time yang di pilih juga kita bisa melihat grafik tersebut dari tahun lampau sampai sekarang apakah grafiknya terus naik, naik turun, dan anjlok menurun.')
        st.write('''\n ~ Grafik Stock with Bollinger Bands, disini terdapat beberapa garis yang berbeda warnanya : ''')
        st.write('''1. Warna biru(Stock Prrice) : garis ini menandakan harga saham dari suatu perusahaan, harga saham ini biasanya dapat dipengaruhi oleh berbagai faktor,
termasuk kinerja keuangan perusahaan, kondisi pasar secara keseluruhan, berita industri, dan keputusan manajemen perusahaan. Pada dasarnya,
harga saham mencerminkan seberapa banyak investor bersedia membayar untuk memiliki bagian kecil dari perusahaan tersebut.
2. Warna biru muda(Upper Bollinger Band) : Garis ini menunjukkan harga tertinggi yang dianggap wajar berdasarkan deviasi standar dari harga  rata-rata. Upper Bollinger Band dihitung dengan menambahkan deviasi standar dari harga rata-rata ke middle band. 
Ini membentuk suatu "pita" di atas harga rata-rata. Upper Bollinger Band berguna untuk Mengidentifikasikan kondisi overbought, Volatilitas, dan Tren dan Momentum.
3. Warna merah (Midlle Bollinger Band) : Garis ini menunjukkan Harga rata-rata pada saham. pada harga rata-rata ini biasanya menjadi siynal bagi investmen untuk perubahan tren dan arah /penaikan dan penurunan harga saham.
4. Warna merah mudah (Lower Bollinger Band) : Garis ini menunjukkan harga terendah yang dianggap wajar berdasarkan deviasi standar dari harga rata-rata. Biasanya investor dan trader biasanya akan mempertimbangkan potensial untuk membeli pada saat harga saham tersebut mendekati atau menembus Lower Bolling Band,
karena ada kemungkinan volatilitas dan potensi perubahan tren di pasar keuangan.''')
        st.write('''\n ~ Relative Strength Index(RSI) :
\n Relative Strength Index (RSI) adalah indikator momentum yang digunakan dalam analisis teknikal untuk mengukur kecepatan dan perubahan harga. RSI sering digunakan untuk mengidentifikasi apakah suatu saham dianggap overbought atau oversold, memberikan petunjuk potensial pembalikan harga.
Poin-poin yang dapat mempengaruhi RSI ini adalah sinyal pembalikan, divergensi, konfirmasi tren, dan periode pengamatan.''')
        st.write("Grafik ini sangat membantu investor ataupun treder untuk menentukan langkah selanjutnya dalam menginvestasikan keuangannya pada saham yang dipilih.")
    
    how_to_use()