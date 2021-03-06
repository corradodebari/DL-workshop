#--------------------------------
# Convert Pascal VOC to CSV file
#--------------------------------
import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        print(xml_file)
        for member in root.findall('object'):
            xmin=member.find('bndbox')[0].text
            ymin=member.find('bndbox')[1].text
            xmax=member.find('bndbox')[2].text
            ymax=member.find('bndbox')[3].text
            value = (root.find('filename').text,
                     int(root.find('size')[0].text),
                     int(root.find('size')[1].text),
                     member[0].text,
                     int(xmin),
                     int(ymin),
                     int(xmax),
                     int(ymax)
                     )
            print(value)
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main():
    for directory in ['training','test']:
        image_path = os.path.join('/', 'images/{}'.format(directory))
        print(image_path)
        xml_df = xml_to_csv(image_path)
        xml_df.to_csv('/images/{}_labels.csv'.format(directory), index=None)
        print('Successfully converted xml to csv.')

main()
