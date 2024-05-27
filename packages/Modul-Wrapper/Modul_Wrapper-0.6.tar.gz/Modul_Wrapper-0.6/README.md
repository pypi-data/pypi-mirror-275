# Modul-Wrapper

Modul Wrapper Adalah Modul Untuk Menyimpan Semua Library Yang Akan Digunakan Dalam Bentuk Dictionary Guna Menghindari Crash Karena Penamaan Class atau Function Yang Sama Antar Library. 

## Example

Tanpa Menggunakan Deklarasi Khusus
```python
from Modul_Wrapper import Wrap

modul = Wrap(modul_path="modul.json")
datetime = modul['datetime'].datetime.now().strftime("%H:%M")
print(datetime)
```

Menggunakan Deklarasi Khusus
```python
from Modul_Wrapper import Wrap

modul = Wrap(modul_path="modul.json")
datetime = modul['modul_jam'].datetime.now().strftime("%H:%M")
print(datetime)
```

## Konfigurasi Modul

Download Format Konfigurasi Modul Di : https://github.com/staykimin/Modul-Wrapper