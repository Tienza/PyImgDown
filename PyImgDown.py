import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup

debug = False

def PyImgDown(url, folder_name):
    # Spoof User Agents, helps get past 403 Error
    request_headers = {
        "Accept-Language": "en-US,en;q=0.5",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Referer": url,
        "Connection": "keep-alive"
    }

    # Create Folder To Store Download Pictures
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # URLLIB2 Method
    try:
        page = urllib2.Request(url, headers=request_headers)
        page = urllib2.urlopen(page).read()
        page = BeautifulSoup(page)

        tags = page.findAll('img')

        images = list(set(tag['src'] for tag in tags))

        str_img = []

        for image in images:
            str_img.append(str(image))

        if debug:
            print(str_img)

        print("Images Found: " + str(len(str_img)))
    except:
        print("Improper URL Provided or Could Not Access URL")
        return -1

    correct_input = False

    while not correct_input:
        want_num = raw_input("How many images do you want? (Leave blank to download all): ")
        try:
            if not want_num:
                if debug:
                    print("Nothing was entered...")
                want_num = len(images)
                if debug:
                    print("Assigned want_num: " + str(want_num))
                correct_input = True
            else:
                want_num = int(want_num)
                correct_input = True
            if debug:
                print("Number of Images wanted: "+ str(want_num))
        except ValueError:
            pass  # it was a string, not an int.

    for i in range(want_num):
        try:
            link_check = str_img[i][:5]
            if link_check != "http:":
                down_link = "http:" + str_img[i]
            else:
                down_link = str_img[i]

            extension = str_img[i][-4:]
            if extension == ".jpg":
                file = urllib2.urlopen(down_link)
                data = file.read()
                with open(folder_name + "/" + "img" + str(i) + ".jpg", 'wb') as img:
                    img.write(data)
                print("Successfully Downloaded: http:" + str_img[i] )
            elif extension == ".png":
                file = urllib2.urlopen(down_link)
                data = file.read()
                with open(folder_name + "/" + "img" + str(i) + ".png", 'wb') as img:
                    img.write(data)
                print("Successfully Downloaded: " + str_img[i])
        except:
            extension = str_img[i][-4:]
            if extension == ".jpg":
                print("Failed To Download Image Link: " + "http:" + str_img[i])
            elif extension == ".png":
                print("Failed To Download Image Link: " + str_img[i])


PyImgDown(raw_input("Pleas Enter URL To Download Images: "), raw_input("Please Name Folder To Store Images: "))