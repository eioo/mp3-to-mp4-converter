import subprocess
from mimetypes import MimeTypes
from os import devnull, getcwd, listdir, makedirs, walk
from os.path import basename, dirname, exists, isfile, join, splitext
from pprint import pprint
from urllib.request import pathname2url

ALLOWED_AUDIO_MIMETYPES = ['audio/mpeg']
ALLOWED_IMAGE_MIMETYPES = ['image/jpeg', 'image/png']

CWD = getcwd()
MP3_DIR = join(CWD, 'mp3')

# Setup necessary variables
mime = MimeTypes()

def get_mp3_dirs():
  dirs = next(walk(MP3_DIR))[1]
  return map(lambda d: join(MP3_DIR, d), dirs)

def get_mp3_files(dir_path):
  files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
  full_paths = map(lambda f: join(dir_path, f), files)
  mp3_files = filter(lambda f: (get_mime_type(f) in ALLOWED_AUDIO_MIMETYPES), full_paths)
  return mp3_files

def get_image_file(dir_path):
  files = [f for f in listdir(dir_path) if isfile(join(dir_path, f))]
  full_paths = map(lambda f: join(dir_path, f), files)

  for file_path in full_paths:
    if get_mime_type(file_path) in ALLOWED_IMAGE_MIMETYPES:
      return file_path
  
  return False

def get_mime_type(file_path):
  url = pathname2url(file_path)
  mime_type = mime.guess_type(url)
  return mime_type[0]

def convert_to_mp4(file_path, image_path):
  dir_name =  basename(dirname(file_path))
  file_name = splitext(basename(file_path))[0]
  target_dir = join(CWD, 'mp4', dir_name)
  target_path = join(target_dir, file_name) + '.mp4'

  if not exists(target_dir):
    print(f'Directory doesn\'t exist. Creating "{target_dir}"')
    makedirs(target_dir)

  print(f'Converting "{file_name}"')
  
  args = ['ffmpeg', '-loglevel', 'panic', '-y',
          '-loop', '1', '-r', '1',
          '-i', image_path,
          '-i', file_path,
          '-c:a', 'copy', '-vf', 'scale=720:-2',
          '-shortest', target_path]

  subprocess.call(args)

def main():
  dirs = get_mp3_dirs()

  for d in dirs:
    image_file = get_image_file(d)

    if not image_file:
      print(f'Could not find image file for "{d}". Continuing...')
      continue

    mp3_files = get_mp3_files(d)

    for mp3_file in mp3_files:
      convert_to_mp4(mp3_file, image_file)

  print('Absolutely DONE.')

if __name__ == '__main__':
  main()
