import os
import glob
from xml.etree import ElementTree
import gzip
from gzip import GzipFile
import hashlib
import time
import shutil

def test_result_generate():
    result_file = glob.glob(os.getcwd() + '/*.gz')
    result_file = result_file[0]
    gzip_file = GzipFile(result_file)
    xml_file = gzip_file.filename[:-3]
    tree = ElementTree.parse(gzip_file)
    root = tree.getroot()
    childs = root.getchildren()

    for child in childs:
        if child.tag == "hardware":
            sub_childs = child.getchildren()
            for sc in sub_childs:
                if sc.tag == "model":
                    sc.text = hashlib.md5(str(time.time())).hexdigest()

    tree.write(xml_file)
    gzip_file.close()

    with open(gzip_file.filename[:-3], 'rb') as f_in:
        with gzip.open(gzip_file.filename, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(xml_file)

if __name__ == "__main__":
    test_result_generate()
