import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.markdown("<h1 style='text-align: center; color: white; font-size: 30px;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")


#Menu/tabs
tab1, tab2 = st.tabs(["PULAU BANGKA", "PULAU BELITUNG"])

#PULAU BANGKA
with tab1:
    #PURI TRI AGUNG
    st.header("Puri Tri Agung")
    Puri = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBangka\puriTriAgung.png",)
    st.image(Puri)

    # Mendefinisikan koordinat lokasi
    latitude = -1.899424228970354 
    longitude = 106.18401494232795
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-1.899424228970354},{106.18401494232795}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat 
    st.write("Pagoda Vihara Puri Tri Agung adalah pantai terkenal di Sungailiat, Bangka Belitung. Disebut juga sebagai Pantai Tikus karena lokasinya yang berdekatan dengan pantai tersebut. Pantai ini adalah pantai terpanjang di kota Sungailiat. Pagoda Vihara Puri Tri Agung dikenal sebagai Pagoda Kuil Saolin oleh sebagian masyarakat karena tidak memiliki plakat nama. Misi pembangunan pagoda ini adalah memperkenalkan budaya Bangka dengan ajaran Tri Dharma yang mencakup kongfuciusme, Buddhisme, dan Taoisme. Pembangunan pagoda ini memakan waktu lebih dari 12 tahun dan memiliki interior mewah serta arsitektur yang kokoh. Pagoda ini tidak hanya digunakan sebagai tempat ibadah, tetapi juga terbuka untuk wisatawan yang ingin mengenal keindahan wisata religi di Pulau Bangka. Harapannya, kehadiran Pagoda Vihara Puri Tri Agung dapat meningkatkan daya tarik objek wisata di Pantai Tikus.")


    st.write("-------")#sebagai garis pembatas

    #DANAU KAOLIN 
    st.header("Danau kaolin")
    kaolin = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBangka\DanauKaolin.png",)
    st.image(kaolin, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -2.5486532122958407
    longitude = 106.35298594603229
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.5486532122958407},{106.35298594603229}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat 
    st.write("Danau Kaolin, juga dikenal sebagai Kulong Biru, terletak di Desa Nibung, Kecamatan Koba, Kabupaten Bangka Tengah. Dengan jarak sekitar 60 kilometer dari Bandara Depati Amir dan 15 kilometer dari Koba, ibu kota Kabupaten Bangka Tengah, objek wisata ini dapat dicapai dalam waktu sekitar 60 menit perjalanan darat dari Kota Pangkal Pinang. Danau Kaolin menawarkan keindahan air biru yang jernih dan bukit-bukit berwarna putih yang mempesona. Tempat ini dulunya merupakan bekas tambang bijih timah yang telah ditinggalkan. Kelebihan danau ini adalah udara segar tanpa aroma belerang, karena bukanlah kawah pegunungan. Pengunjung dapat menikmati jalur pedestrian dan jembatan kayu yang terhubung dengan Danau Kaolin, memberikan sensasi yang luar biasa. Kejernihan air danau berwarna biru tosca kontras dengan gundukan pasir putih yang membentuk bukit-bukit kecil di sekitarnya. Warna air danau ini berubah-ubah sesuai dengan suhu udara dan sinar matahari. Danau Kaolin (Kulong Biru) menarik minat banyak turis domestik dan mancanegara, serta menjadi salah satu destinasi wisata utama di Kabupaten Bangka Tengah. Keunikan dan keindahannya telah membuatnya masuk dalam nominasi Destinasi Unik Terpopuler pada Anugerah Pesona Indonesia 2019.")

    st.write("-------")#sebagai garis pembatas


    #PANTAI MATRAS
    st.subheader("Pantai Matras")
    Matras = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBangka\PantaiMatras.png")
    st.image(Matras)

    # Mendefinisikan koordinat lokasi
    latitude = -1.7992147107228296
    longitude = 106.11637164139518
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-1.7992147107228296},{106.11637164139518}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Pantai Matras terletak di desa Sinar Baru, Kecamatan Sungailiat, Pulau Bangka. Pantai ini memiliki keindahan yang memukau dan memiliki pasir putih dengan tekstur halus. Pantainya memiliki panjang 3 km dan lebar 20-30 meter. Pantai Matras merupakan tujuan wisata yang populer di Bangka Belitung, dikunjungi oleh masyarakat lokal, wisatawan domestik, dan mancanegara.")
    st.write("Namun, pantai Matras mengalami abrasi yang signifikan terutama dari bulan November hingga Maret. Hal ini disebabkan oleh arah hadapnya ke Laut Cina Selatan dan peningkatan kekuatan gelombang setiap tahun. Pemandangan di pantai Matras terbagi menjadi dua bagian: bagian selatan dengan ujung tanjung berbatu granit eksotis yang khas Pulau Bangka, dan bagian utara dengan pemandangan pantai yang tak berujung dan sungai air tawar di sekitarnya.")
    

    st.write("-------")#sebagai garis pembatas


    #PANTAI PARAI
    st.subheader("Pantai Parai")
    Parai = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBangka\PantaiParai.png")
    st.image(Parai)

    # Mendefinisikan koordinat lokasi
    latitude = -1.8043226925603426
    longitude = 106.12840979955965
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-1.8043226925603426},{106.12840979955965 }"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Pantai Parai Tenggiri terletak di Kecamatan Sungai Liat, Kabupaten Bangka, Kepulauan Bangka Belitung. Pantai ini memiliki kontur tanah landai dengan ombak yang kecil. Parai Tenggiri adalah pantai utama di wilayah tersebut. Kawasan pantai ini dikenal sebagai Parai Green Resort yang mengedepankan kepedulian lingkungan. Pengunjung dapat menikmati keindahan alam pantai dan berpartisipasi dalam aktivitas rekreasi seperti memancing, naik banana boat, dan menyelam untuk melihat terumbu karang yang berbatasan dengan Laut Cina Selatan.")


    st.write("-------")#sebagai garis pembatas


    #MUSEUM TIMAH
    st.header("Museum Timah")
    timah = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBangka\MuseumTimah.png")
    st.image(timah)

    # Mendefinisikan koordinat lokasi
    latitude = -2.062280623066687
    longitude = 105.16606331166075
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.062280623066687},{105.16606331166075}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Museum Timah Indonesia - Muntok adalah museum khusus yang berfungsi sebagai pusat informasi tentang teknologi peleburan timah, dengan galeri sejarah perkembangan Melayu Bangka, informasi pengasingan Soekarno, dan sejarah Perang Dunia II. Gedung museum ini merupakan bekas Kantor Pusat Pertambangan Timah Bangka yang dibangun pada tahun 1915 dan dikelola oleh Pemerintah Belanda. Gagasan pendirian museum ini diwujudkan pada tahun 2012 melalui tahap konservasi gedung, dan peresmiannya dilakukan pada tanggal 7 November 2013. Museum Timah Indonesia - Muntok, yang memiliki kepemilikan dan pengelolaan oleh PT. Timah Tbk, menampilkan berbagai jenis koleksi seperti bebatuan, fosil makhluk hidup, benda kesukuan, peninggalan budaya dan sejarah, mata uang kuno, perlambangan, naskah, keramik, seni rupa, dan peninggalan teknologi. Terletak di Jalan Jenderal Sudirman, Muntok, Kabupaten Bangka Barat, Provinsi Kepulauan Bangka Belitung, museum ini dapat dicapai melalui Bandar Udara Depati Amir dengan jarak tempuh 143 kilometer, Pantai Tanjung Ular 6,8 kilometer, Pelabuhan Penyebrangan Muntok 6,6 kilometer, atau Terminal Muntok 1,3 kilometer.")


    st.write("-------")#sebagai garis pembatas


    #BATU BELIMBING
    st.header("Batu Belimbing")
    BatuBelimbing = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBangka\BatuBelimbing.png")
    st.image(BatuBelimbing, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -1.5777752926329607
    longitude = 105.51424966012037
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-1.5777752926329607},{105.51424966012037}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Batu Belimbing raksasa di Jebu Laut, Dusun Jebu Laut, Desa Kelabat, Kecamatan Parittiga, Kabupaten Bangka Barat, yang memiliki dinding dan permukaan berbentuk bilah-bilah batu menyerupai buah belimbing dengan tinggi sekitar 30 meter, luas dasar hampir setengah lapangan bola, dan lebar puncak mirip lapangan futsal. Di puncak Batu Belimbing ini, yang permukaannya seperti buah belimbing, terdapat pemandangan eksotis, seperti tepian Pantai Jebu Laut, laut Cina Selatan yang terlihat sejauh mata memandang, Bukit Pala, Penyabung, Pulau Timah, dan pemandangan alam lainnya yang indah tanpa cacat. Pada cuaca cerah, kita juga dapat melihat gugusan Pulau Tujuh. Di sekitar batu raksasa ini, terdapat bongkahan batu besar dengan lubang mirip goa yang dapat digunakan untuk berteduh saat hujan, serta banyak batu belimbing mini yang berdiri kokoh di sekitar batu utama.")


    st.write("-------")#sebagai garis pembatas


    #WISMA RANGGAM
    st.header("Wisma Ranggam")
    WismaRanggam = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBangka\WismaRanggam.png")
    st.image(WismaRanggam, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -2.0591306494811934
    longitude = 105.16327588465587
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.0591306494811934},{105.16327588465587}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Wisma Ranggam, sebuah pesanggrahan di Kecamatan Muntok, Kabupaten Bangka Barat, Kepulauan Bangka Belitung, Indonesia, awalnya didirikan oleh Banka Tin Winning pada tahun 1827 sebagai tempat istirahat bagi karyawan tambang timah. Namun, wisma ini memiliki sejarah yang signifikan dalam perjuangan kemerdekaan Indonesia. Pada bulan Juni 1949, Wisma Ranggam menjadi saksi serah terima Surat Kuasa Kembalinya Kepemerintahan Republik Indonesia dari Soekarno kepada Hamengkubuwana IX di Yogyakarta. Di masa lalu, tempat ini juga menjadi lokasi pertemuan dan pengasingan tokoh-tokoh pejuang kemerdekaan seperti Soekarno, Agus Salim, Ali Sastroamidjojo, dan Mohamad Roem. Sayangnya, selama beberapa waktu, wisma ini dibiarkan terbengkalai dan mengalami kerusakan. Namun, sejak sekitar tahun 2003, pemerintah setempat telah merestorasi Wisma Ranggam menjadi objek wisata sejarah yang menarik bagi pengunjung yang tertarik dengan sejarah Indonesia.")

#---------------------------------------------------------------------------------------------------------------------------------------
#PULAU BELITUNG
with tab2:
    st.header("Pulau Lengkuas")
    WismaRanggam = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBelitung\PulauLengkuas.png")
    st.image(WismaRanggam, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -2.5370390962091625
    longitude = 107.62044246441803
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.5370390962091625},{107.62044246441803}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Pulau Lengkuas, sebuah pulau di Provinsi Kepulauan Bangka Belitung, terletak di sebelah utara Pantai Tanjung Kelayang, Kabupaten Belitung. Pulau ini menawarkan daya tarik utama berupa mercusuar tua yang dibangun pada tahun 1882 dan masih berfungsi sebagai penuntun kapal. Selain itu, pulau ini memiliki batu granit, pasir putih, dan air laut yang jernih. Pulau kecil ini dapat dikelilingi dalam waktu 20 menit dan menjadi tujuan populer untuk selam permukaan, menyelam, serta menjaga keberlanjutan lingkungan dengan membawa pulang sampah yang dihasilkan. Penjaga mercusuar juga melindungi Penyu Hijau di pulau ini.")


    st.write("-------")#sebagai garis pembatas


    st.header("Pulau Pasir")
    WismaRanggam = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBelitung\PulauPasir.png")
    st.image(WismaRanggam, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -2.5535121765125797 
    longitude = 107.65506379566236
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.5535121765125797 },{107.65506379566236}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Pulau Pasir adalah sebenarnya sebuah gosong pasir yang hanya muncul saat air surut. Pulau ini terletak di antara beberapa pulau di sekitarnya dan memiliki pemandangan yang indah. Pulau ini tidak memiliki objek lain selain tumpukan pasir putih halus yang khas Belitung. Selama air surut, wisatawan dapat mengunjungi pulau ini dengan menyewa perahu nelayan dan menikmati keindahan sekitarnya. Pengalaman yang tak terlupakan adalah menemukan bintang laut merah besar di pulau ini dan berfoto sambil memegangnya. Selain itu, ada juga beragam biota laut yang dapat ditemukan di sekitar pulau ini, menambah keseruan kunjungan wisatawan.")


    st.write("-------")#sebagai garis pembatas
    

    st.header("Pulau leebong")
    WismaRanggam = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBelitung\PulauLeebong.png")
    st.image(WismaRanggam, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -2.961167267845937 
    longitude = 107.5340394153441
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.961167267845937},{107.5340394153441}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Pulau Leebong (Lelebong) adalah sebuah pulau kecil yang menjadi destinasi wisata petualangan di pantai Barat Belitung. Terletak sekitar 70 km di selatan Pulau Lengkuas, pulau ini menawarkan pemandangan hutan mangrove di sekitar pelabuhan dan pusat kegiatan pantai yang terdiri dari rumah-rumah kayu beratap daun. Dengan pantai pasir putih yang memukau, wisatawan dapat menikmati berbagai aktivitas air seperti kayak, kano, standing pedal kayak, dan water bicycle. Pulau Leebong juga memiliki fasilitas restoran dan toilet yang bersih untuk kenyamanan pengunjung.")


    st.write("-------")#sebagai garis pembatas
    

    st.header("Replika Rumah laskar Pelangi")
    WismaRanggam = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBelitung\Sekolahlaskarpelangi.png")
    st.image(WismaRanggam, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -2.9638436144845883  
    longitude = 108.15246879999997
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.9638436144845883},{108.15246879999997}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("SD Muhammadiyah Gantong, yang terletak di Desa Lenggang, Kecamatan Gantung, Kabupaten Belitung Timur, Provinsi Kepulauan Bangka Belitung, adalah replika sekolah ikonik dari novel dan film -Laskar Pelangi-. Bangunan sekolah ini, yang melambangkan dedikasi para tokoh dalam cerita, dibangun kembali pada tahun 2010 dan memiliki dua pohon yang khas yang menopang dindingnya untuk tujuan pariwisata. Meskipun merupakan replika, SD Muhammadiyah Gantong tetap mengesankan pengunjung dengan nilai-nilai edukasinya di era pariwisata yang berkembang pesat. Ruang kelasnya, yang mengingatkan pada tempat di mana Ikal, Arai, Mahar, Lintang, dan teman-temannya belajar, memiliki tampilan yang sederhana dengan lantai tanah, meja dan bangku yang sudah lusuh, sebuah lemari, papan tulis, dan gambar Hamengkubuwono dan Cut Nyak Dien di dinding kayu. Tempat ini juga menyediakan fasilitas seperti masjid, area parkir yang luas, kamar mandi, sebuah kafe, galeri lukisan bertema Laskar Pelangi, dan toko oleh-oleh, yang menjamin kenyamanan pengunjung dan memungkinkan mereka benar-benar terjun ke dalam dunia -Laskar Pelangi-. Sebelum pergi, saya mengabadikan momen berharga bersama siswa dalam bentuk foto dan video, mengenang kenangan yang tercipta. Terdapat sebuah tanda yang tergantung di gedung yang bertuliskan, -Bermimpilah tentang apa yang kamu impikan-. Dibuat pada tanggal 27 November 2010, Linggang Gantung, Belitung Timur.")


    st.write("-------")#sebagai garis pembatas
    

    st.header("Pantai Tanjung Tinggi")
    WismaRanggam = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBelitung\PantaiTjTinggi.png")
    st.image(WismaRanggam, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -2.551841959271942  
    longitude = 107.71376172116473
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.551841959271942},{107.71376172116473}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat
    st.write("Tanjung Tinggi adalah pantai yang terletak di pulau Belitung, diapit oleh dua semenanjung, yaitu Tanjung Kelayang dan Tanjung Pendam. Pantai ini terkenal dengan batu granit besar yang tersebar di sekitarnya dan memiliki pasir putih yang luas. Letaknya dekat dengan Pantai Tanjung Kelayang dan menjadi salah satu tempat wisata populer di pulau Belitung. Pantai ini juga dikenal dengan nama Pelabuhan Bilik dan telah menjadi lokasi syuting film --Laskar Pelangi-- dan --Sang Pemimpi--. Selain keindahan alamnya, pantai ini juga menawarkan fasilitas yang memadai, termasuk hotel di sekitarnya. Keistimewaan pantai ini terletak pada beragamnya ukuran batu granit yang ada dan pesona kecantikan saat matahari terbenam. Pantai Tanjung Tinggi telah dikenal oleh wisatawan dari dalam dan luar negeri.")


    st.write("-------")#sebagai garis pembatas
    

    st.header("Museum Kata Andrea Hirata")
    WismaRanggam = Image.open("D:\coding\streamlit\WEB_DEV\photo\Destinasi Wisata\PulauBelitung\MuseumAndreHirata.png")
    st.image(WismaRanggam, width=300)

    # Mendefinisikan koordinat lokasi
    latitude = -2.9669929855502937  
    longitude = 108.16410183558119
    # Membuat URL Google Maps menggunakan koordinat lokasi
    google_maps_url = f"https://www.google.com/maps/place/{-2.9669929855502937},{108.16410183558119}"
    # Membuat hyperlink yang menautkan ke Google Maps
    st.markdown(f"Klik [di sini]({google_maps_url}) untuk membuka lokasi di Google Maps.")

    #penjelasan singkat 
    st.write("Museum Kata Andrea Hirata adalah museum khusus yang koleksinya berkaitan dengan sastra dunia dan sastra Indonesia. Pendirinya adalah Andrea Hirata. Museum ini diresmikan pada bulan November 2012. Kegiatan utama di dalam museum ialah pengenalan tentang sastra, perkembangan sastra di Indonesia, dan pentingnya dunia sastra bagi kehidupan manusia. Di dalam museum juga tersedia informasi mengenai proses panjang penerbitan novel berjudul Laskar Pelangi hingga pembuatannya menjadi film. Pembangunan Museum Kata Andrea Hirata adalah memberikan inspirasi kepada pemuda Indonesia agar berjuang meraih cita-cita seperti yang dikisahkan di dalam novel Laskar Pelangi.")

