from PIL import Image
from os import path


async def generate_profile(name:str):
    if path.exists(f'Media/cache/{name}.jpg'):
        with Image.open(f'Media/cache/{name}.jpg') as orginal_photo:
            with Image.open('Media/template2.png') as template:
                if orginal_photo.size  == (512, 512):
                    orginal_photo.paste(template, mask=template)
                    orginal_photo.save(f'Media/generate/{name}.jpg')
                else:
                    resize_orginal_photo = orginal_photo.resize((512, 512))
                    resize_orginal_photo.paste(template, mask=template)
                    resize_orginal_photo.save(f'Media/generate/{name}.jpg')

    

 # type: ignore


def testtt():
    s = Image.open('new.png')
    print(s.size)
    ss = s.resize((512, 512))
    print(ss.size)
    ss.save('news.png')
    
