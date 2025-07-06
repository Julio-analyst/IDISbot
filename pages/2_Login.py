
import streamlit as st
import pandas as pd
import numpy as np

class LoginUser:

    def __init__(self):
        self.menu = st.sidebar.selectbox("Menu: ", ('Login', 'Registrasi'))
        self.username = None
        
    def baca_data(self):
        try:
            data_user = pd.read_csv("User.csv")
        except FileNotFoundError:
            data_user = pd.DataFrame(columns=["Username", "Password","Nama_Lengkap","Tanggal_Lahir"])
        return data_user

    def regist_data(self,name,password,full_name,date):
        data_user = self.baca_data()
        if name.strip() == '' or password.strip() == '' or full_name.strip() == '' or date.strip() == ' ': #jika inputan kosong, harus diisi
            st.error('Masukkan data yang valid')
            return
        if name in data_user["Username"].tolist():
            st.error("Username sudah terdaftar!, silakan ganti dengan Username lain")
        else:
            new_data = pd.DataFrame({"Username": [name], "Password": [password],"Nama_Lengkap": [full_name],"Tanggal_Lahir": [date]})
            data_user = pd.concat([data_user, new_data], ignore_index=True)
            data_user.to_csv("User.csv", index=False) # Corrected line
            st.success("Registrasi berhasil ! silakan Login")

    def cek_data(self,name,password):
        data_user = self.baca_data()
        user = (data_user[(data_user["Username"] == name) & (data_user["Password"] == password )].iloc[0]
            if not data_user.empty
            else None
            ) 
        if user is not None:
            self.name = name
            st.session_state.isverif = True
            st.session_state.isloggin = True
            st.session_state.username = self.name
            st.rerun()
        

    def buat_form(self):
        if self.menu == "Registrasi":
            InputName = st.text_input("Nama Lengkap")
            Inputdate = st.text_input("Tanggal Lahir (DD/MM?YYYY)")
        InputUsername = st.text_input("Username")
        InputPassword = st.text_input("Password", type="password")

        if self.menu == "Registrasi":
            if st.button("Registrasi",key="register"):
                self.regist_data(InputUsername,InputPassword,InputName,Inputdate)
        elif self.menu == "Login":
            if st.button("Login"):
                self.cek_data(InputUsername, InputPassword)
        
    
    def user_page(self):
        if "isloggin" in st.session_state and st.session_state.isloggin:

            st.title("💸 Selamat Datang! Kami Akan Mewujudkan Tujuan Investasi Anda 💸 ")
            st.markdown("Here to help you out of your investment problem!")

            # Main menu
            
            st.sidebar.markdown("# Pililah Jenis Investasi Yang Menarik Minat Anda!💰")
            selected_option = st.sidebar.selectbox('Pilihlah satu:', ["Tabungan", "Saham", "Emas", "Obligasi", "Deposito", "Reksadana"])


            def tabungan():
                st.title("Tabungan")
                st.subheader("Apa itu....🤔")
                st.markdown(''' Investasi tabungan adalah cara menyimpan uang Anda di tempat yang memberikan imbal hasil atau bunga. Tujuannya adalah agar uang yang disimpan tumbuh seiring waktu, menghasilkan lebih banyak uang daripada sekadar disimpan di tempat biasa seperti tabungan reguler di bank. Jadi, dengan menyimpan uang Anda di tempat yang memberikan bunga atau imbal hasil, Anda berharap uang tersebut bisa bertambah dari waktu ke waktu ''')
            
                st.subheader("Kelebihan ➕")
                st.markdown('''
        \n -	Aman dan Nyaman: Tabungan adalah tempat yang aman untuk menyimpan uang. Seperti tempat tidurmu yang nyaman, tabungan membuat uangmu aman dan tetap di tempatnya.
        \n -	Mudah Dicapai: Kamu bisa mengakses uangmu kapan saja. Jika kamu butuh uang untuk mainan baru atau sesuatu yang ingin kamu beli, tinggal ambil dari tabunganmu.
        \n -	Tidak Hilang: Uang di tabungan tidak akan hilang begitu saja. Seperti mainan favoritmu yang selalu ada di tempatnya, uang di tabungan selalu ada untukmu.
        \n -	Dapat Bertambah: Meskipun tidak banyak, uang di tabungan bisa bertambah. Ini seperti menanam benih kecil yang tumbuh menjadi pohon kecil. Namanya bunga.
        ''')

                st.subheader("Kekurangan ➖")
                st.markdown('''\n -	Bunga Sedikit: Meskipun tabungan bisa bertambah, namun penambahannya tidak banyak. Seperti pohon yang tumbuh sangat pelan, begitu juga dengan uangmu di tabungan.
        \n - 	Tidak Bisa Beli Banyak Mainan: Tabungan tidak akan membuatmu kaya dengan cepat. Kamu mungkin harus menabung untuk waktu yang lama sebelum bisa membeli mainan besar atau sesuatu yang mahal.
        \n -	Tidak Ada Petualangan: Uang di tabungan tidak bisa berpetualang atau bekerja sendiri untukmu. Seperti boneka kesayanganmu yang hanya menunggu di rak, uang di tabungan hanya menunggu di bank.
        \n -	Tidak Bisa Menyesuaikan Diri: Tabungan tidak bisa berubah-ubah sesuai dengan kebutuhanmu. Ini berbeda dengan mainanmu yang bisa kamu sesuaikan sesuai moodmu. Tabungan tetap sama.
        ''')
                st.subheader("Resiko ❗❗❗")
                st.markdown(''' Bunga yang Kurang: Di bank atau celengan, bunga yang didapat bisa sekecil gosip yang berhembus sebentar.
\n - Pertumbuhan yang Pelan: Uangnya tumbuh seperti rumor yang pelan menyebar di lingkungan. Pertumbuhannya tidak selalu cepat.
\n - Celengan yang Hilang: Kadang-kadang, ada rumor bahwa celengan bisa "menghilang" atau tertinggal di belakang lemari. Risiko kecil tapi tetap bisa terjadi.
 ''')

                st.subheader("Siapa yang cocok untuk investasi.....👌")
                st.markdown(''' \n - Cari Keamanan: Mereka yang ingin menjaga uangnya tetap aman tanpa terlalu banyak risiko. Investasi tabungan di bank atau celengan sering dianggap lebih aman daripada investasi lainnya.
\n - Pendekatan Lambat: Orang-orang yang tidak terburu-buru untuk mendapatkan keuntungan besar dalam waktu singkat. Mereka lebih suka melihat uang mereka tumbuh perlahan tapi pasti.
\n - Butuh Dana Darurat: Mereka yang ingin memiliki dana darurat yang mudah diakses jika dibutuhkan. Tabungan memberikan akses cepat ke uang jika terjadi keadaan darurat.
\n - Tidak Terlalu Ambisius: Mereka yang tidak terlalu ambisius untuk mendapatkan keuntungan besar. Mereka lebih fokus pada keamanan dan kepastian.
 ''')

                st.subheader("Kira - kira berapa lama yaa hingga tujuan investasi tercapai?🕥")
                st.markdown(''' Waktu yang dibutuhkan sampai investasi tabungan menguntungkan:
\n Investasi tabungan biasanya tidak memberikan keuntungan besar dalam waktu singkat. Waktu yang dibutuhkan untuk melihat hasil yang signifikan dari investasi tabungan tergantung pada beberapa faktor, termasuk jumlah yang disimpan, tingkat bunga, dan apakah Anda menambahkan uang secara teratur.
Pertumbuhan uang dalam tabungan biasanya terjadi perlahan. Untuk melihat keuntungan yang besar, dibutuhkan waktu yang cukup lama, terutama jika bunganya tidak terlalu tinggi. Investasi tabungan lebih menekankan pada keamanan dan kepastian daripada mendapatkan keuntungan besar dalam waktu singkat.
 ''')

            def saham():
                st.title("Saham")
                st.subheader("Apa itu....🤔")
                st.markdown(''' Saham itu seperti potongan kecil dari suatu perusahaan. Ketika kamu membeli saham, kamu sebenarnya membeli sebagian kecil dari perusahaan itu. Misalnya, bayangkan kamu memiliki sebuah kue besar, dan ketika kamu membaginya menjadi potongan-potongan kecil, setiap potongan itu seperti saham. Setiap potongan mewakili bagian kecil dari kue secara keseluruhan.Contohnya, mari kita bicara tentang saham "Apple". Jika kamu membeli saham Apple, kamu membeli sebagian kecil dari perusahaan teknologi besar yang membuat iPhone, iPad, dan Mac. Jadi, dengan memiliki saham Apple, kamu memiliki sedikit bagian dari keberhasilan atau keuntungan yang diperoleh Apple sebagai perusahaan. Dan jika Apple tumbuh dan berkembang dengan baik, nilai sahamnya pun bisa naik, yang bisa membuatmu mendapatkan keuntungan jika kamu menjual saham tersebut dengan harga lebih tinggi dari harga belinya.
 ''')
            
                st.subheader("Kelebihan ➕")
                st.markdown('''\n - Seperti Bertumbuh Besar: Saham adalah cara untuk membuat uangmu "bertumbuh besar" seperti pohon yang tinggi. Jika kamu memilikinya, kamu bisa mendapatkan lebih banyak uang dari yang kamu simpan.
\n - Bisa Dapat Dividen: Kadang-kadang, saham bisa memberikan hadiah kecil yang disebut dividen. Ini seperti mendapat permen atau cokelat tambahan dari temanmu.
\n - Jadi Pemilik Sebagian: Kalau kamu punya saham, kamu jadi seperti pemilik kecil dari perusahaan. Bayangkan memiliki potongan kue dan bisa mendapatkan sebagian kecil ketika kamu tumbuh lebih tinggi dalam waktu singkat. Ini bisa membuat uangmu jadi lebih banyak.
''')

                st.subheader("Kekurangan ➖")
                st.markdown(''' \n - Bisa Turun Juga: Sayangnya, seperti balon yang bisa bocor, harga saham juga bisa turun. Ini bisa membuat sedih, tapi ingat bahwa kadang-kadang balon bisa ditiup lagi.
\n - Perlu Waktu: Saham butuh waktu untuk tumbuh. Tidak seperti bermain-mainan yang bisa langsung menyenangkan, kamu perlu menunggu untuk melihat saham tumbuh besar.
\n - Perlu Pemahaman Lebih: Saham tidak selalu mudah dimengerti. Kamu perlu belajar sedikit tentang perusahaan dan bagaimana saham bekerja. Ini seperti belajar cara merakit mainan yang baru.
\n - Bisa Bikin Cemas: Harga saham bisa berubah-ubah seperti cuaca. Ini bisa membuat hatimu berdebar-debar seperti ketika kamu tidak tahu kapan hujan akan datang.
 ''')
                st.subheader("Resiko ❗❗❗")
                st.markdown(''' \n -  Kehilangan Uang: Jika harga saham turun saat kamu jual, bisa membuatmu kehilangan uang dari investasimu.
\n - Tidak Ada Jaminan: Tidak ada jaminan bahwa nilai saham akan terus naik. Harganya bisa berubah-ubah sesuai dengan pasar.
\n - Waktu Sulit untuk Jual: Ada waktu-waktu di mana sulit untuk menemukan pembeli yang ingin membeli sahammu dengan harga yang kamu inginkan.
\n - Pengaruh Eksternal: Peristiwa seperti masalah di pasar global atau masalah dalam perusahaan bisa memengaruhi harga saham.
 ''')

                st.subheader("Siapa yang cocok untuk investasi.....👌")
                st.markdown(''' Tipikal orang yang cocok untuk melakukan investasi saham:
\n Orang yang cocok untuk melakukan investasi adalah seseorang yang ingin menyimpan uangnya dengan harapan untuk mendapatkan keuntungan di masa depan. Mereka biasanya punya ketertarikan untuk membuat uang mereka berkembang lebih dari sekadar disimpan di tempat yang sama. Orang-orang ini siap mengambil risiko yang terkendali untuk mendapatkan hasil yang lebih baik dari uang yang mereka investasikan.
 ''')

                st.subheader("Kira - kira berapa lama yaa hingga tujuan investasi tercapai?🕥")
                st.markdown(''' waktu yang dibutuhkan agar investasi saham menguntungkan:
\n Waktu yang dibutuhkan agar investasi saham menguntungkan bisa bervariasi tergantung pada beberapa faktor, seperti kondisi pasar saham, jenis saham yang dibeli, dan strategi investasi yang digunakan. Tidak ada jaminan pasti bahwa investasi saham akan menguntungkan dalam waktu tertentu.Bayangkan seperti menanam pohon. Saat menanam benih pohon, kita tidak bisa langsung melihat pohon besar. Dibutuhkan waktu agar benih tumbuh menjadi pohon besar yang memberikan buah. Begitu juga dengan investasi saham, dibutuhkan waktu untuk melihat hasilnya.
Saat membeli saham, itu seperti menaruh uang pada bisnis. Bisnis ini akan tumbuh seiring waktu. Terkadang, hasilnya bisa terlihat dalam beberapa bulan, tapi seringkali hasil terbaiknya dilihat setelah beberapa tahun.
Jadi, investasi saham butuh kesabaran. Seperti menunggu pohon tumbuh dan memberikan buah, kita perlu waktu untuk melihat investasi saham berkembang dan memberikan keuntungan.
 ''')

            def emas():
                st.title("Emas")
                st.subheader("Apa itu....🤔")
                st.markdown(''' Investasi emas adalah cara untuk menyimpan uang dalam bentuk emas, seperti koin atau batangan emas, sebagai cara untuk mendapatkan keuntungan di masa depan. Orang melakukan ini karena emas sering dianggap nilainya cenderung stabil dan bisa naik seiring waktu, membantu melindungi uang dari perubahan nilai atau ketidakstabilan ekonomi. Tujuannya adalah membeli emas sekarang dan kemudian menjualnya di masa depan dengan harga yang lebih tinggi untuk mendapatkan keuntungan
 ''')
            
                st.subheader("Kelebihan ➕")
                st.markdown('''\n -  Bersinar Seperti Bintang: Emas itu berkilau seperti bintang di langit malam. Jadi, jika kamu memiliki emas, kamu punya sesuatu yang indah dan bersinar seperti mainan favoritmu.
\n - Tahan Lama: Emas bisa tahan lama, seperti boneka atau mainan kesayanganmu. Itu artinya, emas bisa kamu simpan untuk waktu yang lama dan tetap cantik.
\n - Dapat Bertambah Nilainya: Emas bisa menjadi lebih berharga seiring berjalannya waktu. Ini seperti memiliki mainan yang menjadi lebih istimewa seiring berjalannya waktu.
\n - Aman Seperti Pelukan Mama: Emas memberikan perasaan aman, seperti ketika kamu dipeluk oleh mama atau papa. Orang sering menyimpan emas karena merasa aman dengannya.
 ''')

                st.subheader("Kekurangan ➖")
                st.markdown('''\n - Tidak Bisa Berbicara: Emas tidak bisa berbicara seperti teman mainanmu. Artinya, emas tidak memberi tahu kamu apa yang sebenarnya terjadi dengannya, apakah nilainya akan bertambah atau tidak.
\n - Perlu Tempat Aman: Emas perlu tempat yang aman, seperti tempat mainanmu yang selalu dijaga oleh mama atau papa. Jadi, kamu perlu menemukan tempat yang baik untuk menyimpan emas.
\n - Tidak Bisa Dibagi-bagi: Emas tidak bisa dibagi Ini artinya, emas tidak memberitahu kamu kapan kamu harus mengambilnya atau menjualnya.
''')
                st.subheader("Resiko ❗❗❗")
                st.markdown('''\n - Harga yang berubah-ubah: Harga emas bisa naik dan turun dengan cepat, bisa bikin nilai investasi Anda berubah-ubah juga.
\n - Biaya penyimpanan: Kalau punya emas fisik, Anda perlu tempat aman untuk simpan. Itu bisa ada biaya tambahan.
\n - Sulit dijual: Kadang emas fisik susah dijual dengan cepat atau dengan harga yang diinginkan. Proses jual beli bisa lama.
\n - Pengaruh pasar: Nilai emas dipengaruhi oleh banyak hal di pasar global. Perubahan ini bisa langsung mempengaruhi nilai investasi Anda.
\n - Kemungkinan palsu: Ada risiko mendapatkan emas palsu yang bisa turunkan nilai investasi. Ini bisa jadi masalah.
 ''')

                st.subheader("Siapa yang cocok untuk investasi.....👌")
                st.markdown('''\n - Tipikal orang yang cocok untuk melakukan investasi emas: Mencari kestabilan: Mereka yang ingin uang mereka tetap aman nilainya dari perubahan di pasar atau ekonomi.
\n - Paham tentang pasar: Orang-orang yang mau mengerti bagaimana kondisi pasar dan apa yang memengaruhi harga emas.
\n - Bisa bersabar: Mereka yang sabar dan tidak tergesa-gesa untuk mendapat untung. Investasi emas biasanya butuh waktu untuk memberikan keuntungan.
\n - Siap menyimpan dengan aman: Orang-orang yang siap untuk menjaga emas mereka dengan baik dan melindunginya dari risiko kehilangan atau pencurian.
\n - Ingin beragam investasi: Mereka yang ingin memiliki beberapa jenis investasi untuk mengurangi resiko. Investasi emas bisa menjadi bagian dari portofolio mereka.
 ''')

                st.subheader("Kira - kira berapa lama yaa hingga tujuan investasi tercapai?🕥")
                st.markdown(''' waktu yang dibutuhkan sampai investasi emas menguntungkan:
\n Emas cenderung stabil nilainya dari waktu ke waktu, tetapi nilai emas juga bisa naik atau turun tergantung pada kondisi pasar global. Maka dari itu, banyak ahli merekomendasikan untuk memegang investasi emas dalam jangka waktu yang lebih panjang agar memiliki kesempatan yang lebih baik untuk mendapatkan keuntungan. Bayangkan investasi emas seperti menanam pokok pisang. Anda tanam bibit pisang hari ini, tapi sayangnya besok Anda tidak akan dapat memetik pisang yang siap dimakan. Anda butuh waktu, air, sinar matahari, dan kesabaran sebelum bisa mendapatkan hasilnya.
Investasi emas juga begitu. Anda beli emas hari ini, tapi tidak bisa mengharapkan untuk menggali peti emas di halaman Anda besok pagi. Dibutuhkan waktu, kondisi pasar yang tepat, dan kesabaran untuk melihat investasi emas tumbuh dengan baik, seperti menunggu pisang di pohon sampai matang. Jadi, bersabarlah dan nikmati prosesnya!
 ''')

            def obligasi():
                st.title("Obligasi")
                st.subheader("Apa itu....🤔")
                st.markdown(''' Obligasi itu seperti surat janji yang membuat suatu perusahaan atau pemerintah berkomitmen untuk membayar kembali uang yang kamu pinjamkan, ditambah dengan bunga sebagai imbalan atas pinjaman tersebut. Obligasi ini dapat diartikan sebagai surat pengakuan utang yang didalamnya berisi janji dari pihak yang menerima pinjaman.

\n Contohnya = bayangkan jika kamu memberikan pinjaman kepada temanmu lalu temanmu membuat janji untuk mengembalikan uang tersebut ditambah dengan bunga sampai batas waktu tertentu. Obligasi mirip dengan itu, tapi pinjaman tersebut untuk suatu perusahaan atau pemerintahan.
 ''')
            
                st.subheader("Kelebihan ➕")
                st.markdown('''\n - Seperti Pinjam Teman: Ketika kamu memiliki obligasi, itu seperti meminjamkan uang kepada teman. Temanmu memberikan janji untuk mengembalikan uangmu beserta bonus (bunga). Ini seperti mendapat hadiah tambahan ketika kamu meminjamkan mainanmu pada temanmu.
\n - Aman dan Teratur: Obligasi itu aman dan teratur, seperti ketika kamu memiliki rutinitas harian yang membuatmu nyaman. Kamu tahu kapan kamu akan mendapatkan uang kembali dan berapa banyak.
\n - Pendapatan Tetap: Kamu mendapatkan uang tambahan secara teratur dari obligasi. Ini seperti mendapatkan jatah permen setiap hari. Kamu tahu persis berapa yang akan kamu dapatkan.
\n - Cocok untuk Jangka Waktu Pendek: Obligasi cocok untuk jangka waktu pendek. Ini seperti ketika kamu menabung uang jajanmu untuk membeli mainan baru.
 ''')

                st.subheader("Kekurangan ➖")
                st.markdown('''\n - Bunga Mungkin Kecil: Kadang-kadang, bunga yang kamu dapatkan dari obligasi mungkin tidak banyak. Ini seperti hanya mendapat sedikit permen sebagai bonus.
\n - Tidak Seperti Saham yang Bertumbuh Cepat: Obligasi tidak tumbuh seperti saham. Ini berbeda dengan tanaman yang bisa tumbuh lebih besar dalam waktu singkat.
\n - Tidak Ada Keuntungan Besar: Kamu mungkin tidak bisa mendapatkan keuntungan besar seperti yang bisa kamu dapatkan dari saham. Ini berbeda dengan hadiah besar yang mungkin kamu dapatkan dari permainan atau acara tertentu.
\n - Tidak Bisa Diubah-ubah: Setelah kamu punya obligasi, kamu tidak bisa mengubahnya. Ini seperti memiliki mainan yang tidak bisa diubah-ubah atau dimodifikasi.
Jadi
 ''')
                st.subheader("Resiko ❗❗❗")
                st.markdown('''\n - Risiko Kredit: Ada kemungkinan penerbit yaitu perusahaan atau pemerintah tidak dapat membayar utangnya
\n - Risiko Likuiditas: Hal ini mengacu pada kemudahan jual beli, obligasi mungkin kurang likuid daripada saham, yang artinya mungkin sulit untuk menjualnya dengan cepat tanpa mengalami penurunan nilai.
\n - Risiko Kondisi Pasar: Nilai obligasi dapat dipengaruhi oleh kondisi pasar secara keseluruhan. Jika ekonomi sedang bergejolak, nilai obligasi bisa saja turun.
 ''')

                st.subheader("Siapa yang cocok untuk investasi.....👌")
                st.markdown('''\n - Investor Konservatif: Obligasi cocok bagi mereka yang suka dengan investasi rendah risiko dan cenderung bermain aman dalam investasi
\n - Pensiun dan Orang yang Mendekati hari Pensiun: Investasi ini sangat cocok bagi mereka yang sudah mendekati masa pensiun. Pendapatan tetap dari bunga dapat memberi kepastian dihari tua.
\n - Investor yang ingin diverifikasi: Cocok untuk para investor yang ingin membuat portofolio investasi.
\n - Orang yang mengutamakan pendapatan tetap: Jika mencari sumber pendapatan tetap secara teratur, obligasi cukup menjanjikan untuk mendapat pendapatan tetap yang teratur dari bunganya.
 ''')

                st.subheader("Kira - kira berapa lama yaa hingga tujuan investasi tercapai?🕥")
                st.markdown(''' Keuntungan dalam obligasi tergantung pada tingkat bunga, jangka waktu investasi, serta kondisi pasar. Biasanya semakin lama kamu memegang obligasi, semakin besar potensi keuntungannya. ''')

            def deposito():
                st.title("Deposito")
                st.subheader("Apa itu....🤔")
                st.markdown('''  Deposito adalah investasi dimana seseorang menempatkan sejumlah uang dalam bank atau lembaga keuangan untuk jangka waktu tertentu dengan tingkat bunga yang tetap. Deposito ini seperti kamu menyewakan uang pada bank dalam jangka waktu yang telah disepakati dan bunga yang didapatkan berada ditingkat tetap.  ''')
            
                st.subheader("Kelebihan ➕")
                st.markdown('''\n - Seperti Menyimpan di Kotak Khusus: Deposito itu seperti menyimpan mainanmu di kotak khusus yang aman. Uangmu disimpan di tempat yang sangat aman dan tidak mudah diambil oleh orang lain.
\n - Tetap Ada Bonus: Deposito memberikan bonus tambahan, yang disebut bunga. Ini seperti mendapatkan hadiah ekstra ketika kamu menyimpan mainanmu di kotak khusus.
\n - Tidak Bisa Diambil Sebelum Waktunya: Uang di deposito tidak bisa diambil sebelum waktunya. Ini seperti ketika ibumu bilang bahwa kamu hanya bisa main di taman setelah makan. Uangnya aman di sana sampai waktu yang ditentukan.
\n - Tidak Berubah-Ubah: Deposito itu seperti mainan yang tidak berubah-ubah. Kamu tahu pasti berapa banyak yang akan kamu dapatkan. Ini memberikan kepastian seperti tahu persis kapan mainanmu akan kembali.
 ''')

                st.subheader("Kekurangan ➖")
                st.markdown('''\n - Harus Menunggu Lama: Sayangnya, kamu harus menunggu sampai waktu tertentu untuk bisa mengambil uangmu dari deposito. Ini seperti menunggu acara atau liburan yang kamu nanti-nanti.
\n - Bunga Mungkin Tidak Banyak: Meskipun ada bonus (bunga), kadang-kadang bunganya tidak terlalu banyak. Ini seperti hanya mendapatkan sedikit permen sebagai bonus.
\n - Tidak Seperti Saham yang Bisa Tumbuh Cepat: Deposito tidak tumbuh seperti saham. Ini berbeda dengan tanaman yang bisa tumbuh lebih besar dalam waktu singkat.
\n - Tidak Bisa Digunakan untuk Kebutuhan Mendesak: Uang di deposito tidak bisa diambil dengan cepat jika kamu butuh uang untuk sesuatu yang penting. Ini seperti tidak bisa langsung mendapat mainan baru jika yang lama rusak.
 ''')
                st.subheader("Resiko ❗❗❗")
                st.markdown('''\n - Likuiditas terbatas: Uangmu akan terkunci dalam deposito untuk jangka waktu tertentu. Jika kamu perlu mengakses uang sebelum waktu yang disepakati, kamu mungkin akan dikenai denda atau kehilangan sebagian bunga.
\n - Inflasi: Sayangnya tingkat bunga deposito biasanya lebih rendah dibandingkan laju inflasi. Ini berarti, meskipun uangmu tumbuh dengan bunga, daya belinya bisa berkurang seiring waktu.
\n - Pengembalian yang Rendah: Meskipun cenderung aman, pengembalian dari deposito biasanya lebih rendah dibanding jenis investasi lainnya.
\n - Pajak: Bunga atau keuntungan yang kamu terima dari deposito dapat dikenai pajak.

  ''')

                st.subheader("Siapa yang cocok untuk investasi.....👌")
                st.markdown('''\n - Investor Konservatif:  Ini sangat cocok untuk kamu yang suka menghindar risiko tinggi dan mencari investasi yang stabil dan mendapat keuntungan tetap.
\n - Orang yang mendekati pensiun dan yang membutuhkan dana darurat: Ini sangat cocok untuk kamu yang membutuhkan dana darurat serta dana untuk keamanan dimasa tua, karena deposito memberi kepastian dan keamanan dana yang stabil.
\n - Investor jangka pendek: Deposito cocok untuk kamu yang memiliki rencana keuangan jangka pendek, seperti menabung untuk liburan atau pembelian besar dalam jangka waktu beberapa tahun.
 ''')

                st.subheader("Kira - kira berapa lama yaa hingga tujuan investasi tercapai?🕥")
                st.markdown(''' Investasi deposito umumnya sudah menghasilkan keuntungan yang stabil karena tingkat bunga yang telah disepakati sejak awal. Deposit ini biasanya memiliki jangka waktu tertentu, seperti 3, 6, 12 bulan, atau lebih. Keuntungan sudah diatur sebelumnya, jadi umumnya, Anda akan melihat hasil yang sudah pasti saat jatuh tempo.
\nNamun, perlu dicatat bahwa keuntungan dari deposito tidaklah sebesar investasi yang lebih berisiko seperti saham atau reksadana. Biasanya, deposito memberikan keuntungan yang lebih kecil, tapi dalam jangka waktu yang lebih pasti dan stabil. Jadi, sementara investasi deposito cenderung aman, keuntungannya mungkin tidak sebesar investasi yang lebih berisiko, namun lebih pasti.
 ''')

            def reksadana():
                st.title("Reksadana")
                st.subheader("Apa itu....🤔")
                st.markdown(''' Investasi reksadana itu seperti bergabung dalam satu kotak besar dengan orang lain untuk membeli berbagai macam investasi, seperti saham atau obligasi. Seorang ahli akan mengelola uang di dalam kotak ini dan membeli beragam investasi untuk kita. Keuntungan atau kerugian dari investasi ini kemudian dibagi-bagi di antara kita sesuai dengan seberapa besar kita berkontribusi ke kotak besar itu. Jadi, dengan reksadana, kita bisa berinvestasi dalam berbagai jenis aset meskipun uang yang kita punya tidak terlalu banyak.
 ''')
            
                st.subheader("Kelebihan ➕")
                st.markdown('''\n - Banyak Mainan dalam Satu Kotak: Reksadana itu seperti memiliki banyak mainan dalam satu kotak besar. Kamu bisa memiliki potongan dari berbagai mainan tanpa harus membeli semuanya sendiri.
\n - Dikelola Oleh Ahli: Reksadana diurus oleh orang yang pintar tentang uang. Mereka tahu cara mengatur mainan agar tumbuh besar. Seperti memiliki kakak yang pandai mengatur mainanmu.
\n - Bertumbuh Lebih Cepat: Reksadana bisa tumbuh lebih cepat daripada hanya menyimpan uang di kotak. Ini seperti mainan yang bisa bertambah banyak dalam waktu singkat.
\n - Bisa Dapat Hadiah Rutin: Kadang-kadang, reksadana memberikan hadiah rutin yang disebut dividen. Ini seperti mendapat permen atau cokelat tambahan dari teman setiap bulan.
 ''')

                st.subheader("Kekurangan ➖")
                st.markdown('''\n - Harganya Bisa Naik Turun: Sayangnya, seperti mainan yang harganya bisa naik dan turun, nilai reksadana juga bisa berubah-ubah. Ini bisa membuat hatimu berdebar-debar seperti ketika mainanmu harganya berubah.
\n - Perlu Tahu Sedikit: Kamu perlu tahu sedikit tentang cara mainan bekerja agar bisa berinvestasi dalam reksadana. Ini seperti belajar cara merakit mainan yang baru.
\n - Tidak Selalu Ada Bonus Besar: Meskipun ada bonus (dividen), kadang-kadang bonusnya tidak terlalu besar. Ini seperti hanya mendapat sedikit permen sebagai bonus.
\n - Harus Bersabar: Reksadana butuh waktu untuk tumbuh besar. Kamu perlu sedikit kesabaran seperti saat menunggu mainan baru yang kamu impikan
 ''')
                st.subheader("Resiko ❗❗❗")
                st.markdown('''\n - Risiko Pasar: Nilai investasi dalam reksadana bisa dipengaruhi oleh kondisi pasar, seperti naiknya atau turunnya harga saham atau obligasi. Jika pasar sedang turun, nilai investasi Anda bisa terpengaruh.
\n - Risiko Manajemen: Kinerja reksadana tergantung pada kemampuan manajer investasinya. Jika manajer tidak berhasil membuat keputusan yang baik, kinerja reksadana bisa terpengaruh.
\n - Risiko Likuiditas: Tidak semua reksadana mudah dijual atau ditukar dengan uang tunai secara cepat. Beberapa jenis reksadana mungkin memerlukan waktu untuk mencairkan investasi.
\n - Risiko Diversifikasi: Meskipun reksadana sudah terdiversifikasi, artinya memiliki berbagai macam investasi, namun jika salah satu asetnya merosot nilainya, hal itu bisa memengaruhi nilai keseluruhan reksadana.
\n - Biaya dan Pajak: Beberapa reksadana bisa memiliki biaya administrasi atau manajemen. Selain itu, ada juga pajak yang mungkin dikenakan pada keuntungan investasi Anda.
 ''')

                st.subheader("Siapa yang cocok untuk investasi.....👌")
                st.markdown(''' Tipikal orang seperti apa yang cocok untuk Reksadana:
\n - Investor Pemula: Jika kamu adalah investor pemula, reksadana dapat menjadi pilihan yang baik. Mereka dapat mengakses portofolio yang telah diatur oleh manajer investasi profesional.
\n - Investor yang mencari diversifikasi: Bagi orang yang ingin mengurangi risiko dengan menyebarkan investasi mereka ke berbagai instrumen keuangan, reksadana menawarkan diversifikasi yang otomatis melalui portofolio yang beragam.
\n - Orang sibuk atau tidak aktif secara finansial: Reksadana memungkinkan investor untuk menghindari kebutuhansecara aktif mengelola portofolio mereka sendiri. Karena, manajer investasi membantu mengelola dana dan membuat keputusan investasi. Investor jangka panjang: Bagi kamu yang memiliki tujuan investasi jangka panjang, seperti pensiun atau pendidikan anak, reksadana dapat memberikan pertumbuhan kapital yang lebih berkelanjutan daripada beberapa pilihan investasi lainnya.
\n - Investor yang menilai profesionalisme: Untuk kamu yang ingin keputusan investasi diambil oleh para profesional keuangan yang berpengetahuan, reksadana dengan manajer investasi dapat memberi keyakinan


 ''')

                st.subheader("Kira - kira berapa lama yaa hingga tujuan investasi tercapai?🕥")
                st.markdown(''' Waktu yang dibutuhkan agar investasi reksadana menguntungkan bisa bervariasi tergantung pada berbagai faktor. Investasi reksadana umumnya dimaksudkan untuk jangka panjang dan hasilnya bisa bervariasi tergantung pada kondisi pasar dan jenis reksadana yang Anda pilih.Tidak ada jaminan pasti kapan investasi reksadana akan menguntungkan. Beberapa orang mungkin melihat hasil yang baik dalam jangka waktu tertentu, sementara yang lain mungkin membutuhkan waktu lebih lama.Dalam banyak kasus, investasi reksadana lebih efektif jika dipegang dalam jangka waktu yang lebih panjang, seperti 5 tahun atau lebih. Ini memberikan kesempatan bagi investasi tersebut untuk melewati fluktuasi pasar dan mungkin memberikan hasil yang lebih baik.Namun, sangat penting untuk memahami bahwa pasar keuangan bisa berubah-ubah. Jadi, keuntungan investasi reksadana bisa bervariasi dari waktu ke waktu dan tidak dapat dipastikan secara pasti dalam jangka waktu tertentu.
 ''')

            if selected_option == "Tabungan":
                tabungan()
            elif selected_option == "Saham":
                saham()
            elif selected_option == "Emas":
                emas()
            elif selected_option == "Obligasi":
                obligasi()
            elif selected_option == "Deposito":
                deposito()
            elif selected_option == "Reksadana":
                reksadana()
            if st.button("Logout"):
                st.session_state.isloggin = False
                st.session_state.isverif = False
                st.rerun()
        else:
            self.buat_form()

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
st.markdown("<h1 class='centered-title'>SmartInvest</h1>", unsafe_allow_html=True)

app = LoginUser()
app.user_page()
