### 📌 **README.md**  

# Türkiye Güncel Deprem Verisi

Bu Python betiği, Boğaziçi Üniversitesi Kandilli Rasathanesi ve Deprem Araştırma Enstitüsü'nden en güncel deprem verilerini çekerek yapılandırılmış bir formata dönüştürür. 🚀

## 📂 Klasör ve Dosya Yapısı

Deprem verileri **yıl ve ay bazında** saklanır. Klasör ve dosya organizasyonu aşağıdaki gibidir:


📂 2025\
   ├── 📄 01.csv  (Ocak 2025 verileri)\
   ├── 📄 02.csv  (Şubat 2025 verileri)\
   ├── 📄 03.csv  (Mart 2025 verileri)\
   └── ...\
📂 2026
   ├── 📄 01.csv  (Ocak 2026 verileri)
   ├── 📄 02.csv  (Şubat 2026 verileri)
   └── ...


- **Her yıl için bir klasör** oluşturulur (örn: `2025`, `2026`).
- **Her ay için bir CSV dosyası** oluşturulur (`01.csv`, `02.csv`, ...).
- **Yeni veriler eklenirken, aynı tarih-saat-koordinatlı ölçümler güncellenir**, böylece yinelenen kayıtlar engellenir.
- **Farklı aylara ait veriler doğru dosyaya eklenir.** Örneğin, Şubat ayında çalıştırıldığında ancak Ocak ayına ait depremler varsa, Ocak ayının (`01.csv`) içine eklenir.

# Türkiye Real-Time Earthquake Data

This Python script scrapes the latest earthquake data from Boğaziçi University Kandilli Observatory and Earthquake Research Institute and processes it into a structured format. 🚀

## 📂 Folder and File Structure

Earthquake data is stored **yearly and monthly**. The folder and file organization is as follows:

📂 2025\
   ├── 📄 01.csv  (January 2025 data)\
   ├── 📄 02.csv  (February 2025 data)\
   ├── 📄 03.csv  (March 2025 data)\
   └── ...\

📂 2026\
   ├── 📄 01.csv  (January 2026 data)\
   ├── 📄 02.csv  (February 2026 data)\
   └── ...\

- **A separate folder is created for each year** (e.g., `2025`, `2026`).
- **A CSV file is created for each month** (`01.csv`, `02.csv`, ...).
- **New data is added while avoiding duplicates.** If an earthquake has the same date, time, latitude, and longitude, it is updated instead of being duplicated.
- **Records from different months are placed correctly.** For example, if the script runs in February but contains earthquakes from January, those records are added to January’s (`01.csv`) file.


📊 **Updated data is automatically saved and structured, ensuring easy access and analysis.**  
💡 Feel free to contribute and enhance this repository! 🚀