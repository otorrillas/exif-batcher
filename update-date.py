from exiftool import ExifToolHelper
from os import listdir

# Sample date: 2022:10:05 18:37:34+02:00

def getUpdatedDate(originalDate):
  date, hour = originalDate.split(' ')
  updatedDate = '2022:10:05 ' + hour

  return updatedDate

def updateOriginalDate(picFile):
  for d in et.get_metadata(picFile):
    for k, v in d.items():
      if (k == "EXIF:DateTimeOriginal"):
        updatedDate = getUpdatedDate(v)

        print('EXIF:DateTimeOriginal')
        print('originalDate: ', v)
        print('updatedDate: ', updatedDate)
        print('---')
        et.set_tags(
          [picFile],
          tags={"EXIF:DateTimeOriginal": updatedDate, "EXIF:ModifyDate": updatedDate, "EXIF:CreateDate": updatedDate },
          params=["-P", "-overwrite_original"]
        )
      if (k == "File:FileModifyDate"):
        updatedDate = getUpdatedDate(v)

        print('File:FileModifyDate')
        print('originalDate: ', v)
        print('updatedDate: ', updatedDate)
        print('---')
        et.set_tags(
          [picFile],
          tags={"FileModifyDate": updatedDate}
        )

with ExifToolHelper() as et:
  for file in listdir("pics"):
    if file.endswith(".JPG") or file.endswith('.RAF'):
      picFile = 'pics/' + file
      print('picFile =>', picFile)

      updateOriginalDate(picFile)
