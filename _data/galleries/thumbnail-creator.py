import glob
from PIL import Image, ExifTags
from os.path import join, basename, splitext

# configuration
image_path = "images"
extensions= ['jpg', 'png']
path = join("../../assets/photography/", "images")

for extension in extensions:
    search = join(path, "*."+extension)
    infiles = [infile for infile in glob.glob(search) if (not "thumbnail" in splitext(basename(infile))[0])]
    # infiles = [infile for infile in glob.glob(search) if (not "thumbnail" in splitext(basename(infile))[0] and not "x" in splitext(basename(infile))[0])]
    for infile in infiles:
        image = Image.open(infile)

        if "jpg" in extension and hasattr(image, '_getexif'): # only present in JPEGs
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation]=='Orientation':
                    break

            e = image._getexif()       # returns None if no EXIF data
            if e is not None:
                exif=dict(e.items())
                try:
                    if exif[orientation] == 3:   image = image.transpose(Image.ROTATE_180)
                    elif exif[orientation] == 6: image = image.transpose(Image.ROTATE_270)
                    elif exif[orientation] == 8: image = image.transpose(Image.ROTATE_90)
                except Exception as e:
                    print("Error in EXIF orientation for " + infile)
        elif "jpg" in extension:
            print("No EXIF for " + infile)

        # convert to thumbnail image
        image.thumbnail((512, 512), Image.ANTIALIAS)
        format = 'JPEG' if extension == 'jpg' else extension
        image.save(splitext(infile)[0]+"-thumbnail."+extension, format)
