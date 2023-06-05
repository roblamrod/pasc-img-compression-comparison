from PIL import Image
import time
import os
import matplotlib.pyplot as plt

compress_rates={"png":[], "tiff":[], "jpeg":[]}
compress_times={"png":[], "tiff":[], "jpeg":[]}
input_sizes=[]

for i in range(10):
    img="input/%d.bmp"%i
    file_stat = os.stat(img)
    input_img_size = file_stat.st_size
    input_sizes.append(input_img_size)

    out_name="output/out%d"%i
    print("="*20)
    print("Image: %s"%img)

    start_time = time.time()
    Image.open(img).save(os.path.join(out_name+'.png'))
    elapsed_time = time.time() - start_time
    print("PNG: %0.10f seconds." % elapsed_time)
    file_stat = os.stat(out_name+'.png')
    output_img_size = file_stat.st_size
    compress_rates["png"].append(input_img_size/output_img_size)
    compress_times["png"].append(elapsed_time)

    start_time = time.time()
    Image.open(img).save(os.path.join(out_name+'.tiff'))
    elapsed_time = time.time() - start_time
    print("TIFF: %0.10f seconds." % elapsed_time)
    file_stat = os.stat(out_name+'.tiff')
    output_img_size = file_stat.st_size
    compress_rates["tiff"].append(input_img_size/output_img_size)
    compress_times["tiff"].append(elapsed_time)

    start_time = time.time()
    Image.open(img).save(os.path.join(out_name+'.jpeg'))
    elapsed_time = time.time() - start_time
    print("JPEG: %0.10f seconds." % elapsed_time)
    file_stat = os.stat(out_name+'.jpeg')
    output_img_size = file_stat.st_size
    compress_rates["jpeg"].append(input_img_size/output_img_size)
    compress_times["jpeg"].append(elapsed_time)

fig, ax = plt.subplots()
for i in compress_rates.keys():
    plt.plot(input_sizes, compress_rates[i], label=i)
plt.legend()
plt.grid()
m2km = lambda x, _: f'{x/1000:g}'
ax.xaxis.set_major_formatter(m2km)
ax.yaxis.set_major_formatter(m2km)
plt.xlabel("Input image size (KB)")
plt.ylabel("Compression rate (KB)")

fig, ax = plt.subplots()
for i in compress_times.keys():
    plt.plot(input_sizes, compress_times[i], label=i)
plt.legend()
plt.grid()
m2km = lambda x, _: f'{x/1000:g}'
ax.xaxis.set_major_formatter(m2km)
ax.yaxis.set_major_formatter(m2km)
plt.xlabel("Input image size (KB)")
plt.ylabel("Compression time (ms)")

plt.show()