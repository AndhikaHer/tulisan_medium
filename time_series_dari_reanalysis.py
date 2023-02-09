import os
import xarray as xr

#
DIR = os.path.expanduser('/Users/andhika/Downloads/medium')
PATH = os.path.join(DIR,'angin_temp_jawa_2019.nc')
data1 = xr.open_dataset(PATH)

# Menampilkan global information dari file NC
# Tahap ini bermanfaat untuk mengetahui informasi terkait dataset kita,
# seperti informasi tentang:
# - berapa panjang dataset kita (bisa dicek dari "time")
# - rentang bujur dan lintang data, serta resolusi spasial data
# - nama variabel yang ada pada dataset
# - serta beberapa meta data lainnya

print(data1)

# Ekstrak data

temp = data1.t2m.data

