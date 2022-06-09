import re
import zipfile
import time


def main():
    unzipped_file = zipfile.ZipFile("apache_logs.zip", "r")
    log_file = unzipped_file.read("apache_logs.txt")
    pattern = re.findall(
        "\[(\d{2}\/\w{3}\/\d{4}\:\d{2}\:\d{2}:\d{2}\s?\+\d{4})\]\s\"GET\s[\/\w\-?]+\.(png|jpg|jpeg|gif)\sHTTP"
        "\/\d{1}\.\d{1}.\s200\s(\d+)", str(log_file))
    total_size_in_bytes = 0
    min_date = time.strptime("08/Mar/2004:21:10:44", "%d/%b/%Y:%H:%M:%S")
    max_date = time.strptime("12/Mar/2004:15:21:28", "%d/%b/%Y:%H:%M:%S")
    for i in pattern:
        dt = time.strptime(i[0], "%d/%b/%Y:%H:%M:%S %z")
        if min_date < dt < max_date:
            total_size_in_bytes += int(i[2])

    print(f"Summary size of the all images are {total_size_in_bytes} bytes")


if __name__ == '__main__':
    main()
