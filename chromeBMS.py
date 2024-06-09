import os
import json
import asyncio
import re

PYPPETEER_CHROMIUM_REVISION = "1000027"
os.environ["PYPPETEER_CHROMIUM_REVISION"] = PYPPETEER_CHROMIUM_REVISION
from pyppeteer import launch


CWD = os.getcwd()
USER = os.getlogin()
DEFAULT_PDF_FOLDER = "C:\\chromebookmark"
BOOKMARK_PATH = (
    f"C:\\Users\\{USER}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Bookmarks"
)


def sanitize_filename(filename):

    invalid_chars = r'[<>:"/\\|?*]'
    sanitized_filename = re.sub(invalid_chars, "_", filename)
    return sanitized_filename


async def download_webpage_as_pdf(site):

    folder_path = f"{DEFAULT_PDF_FOLDER}\\{site['folder']}"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    site_name_fixed = sanitize_filename(site["name"])
    pdf_path = f"{folder_path}\\{site_name_fixed}.pdf"
    try:

        browser = await launch()
        # if you get a configuration error from the launch() function you can download chromium
        # from the following address:
        # 
        # https://commondatastorage.googleapis.com/chromium-browser-snapshots/index.html?prefix=Win_x64/1000027/
        # and copy it manually into the folder indicated by executablePath,
        # in the code below:
        # 
        # --------------------------------------------------------------
        # current_directory = os.path.dirname(os.path.abspath(__file__))
        # browser = await launch(
        #     executablePath=f"{current_directory}\\chrome-win\\chrome")
        # --------------------------------------------------------------

        page = await browser.newPage()
        await page.goto(site["url"])
        await page.pdf({"path": pdf_path, "format": "A4"})
        await browser.close()

    except Exception as err:
        print(err)


async def download_webpage_list(my_sites):

    coroutine = [download_webpage_as_pdf(site) for site in my_sites]
    tasks = asyncio.gather(*coroutine)
    results = await tasks
    return results


def building_tree_DS(root):

    global levelCompletionArrayIndex
    global subLevel
    subLevel += 1
    for index, elements in enumerate(root["children"]):
        levelCompletionArrayIndex += 1
        levelCompletingRatio = (index + 1) / len(root["children"])
        levelCompletion = [(subLevel, levelCompletingRatio)]
        levelCompletionArray.append(levelCompletion)

        if elements["type"] == "folder":
            buildingFolderPath.append((elements["name"]))
            building_tree_DS(elements)

        elif elements["type"] == "url":
            mySite = {
                "folder": "/".join(buildingFolderPath) + "/",
                "name": elements["name"],
                "url": elements["url"],
            }
            my_sites.append(mySite)

        if levelCompletingRatio == 1:
            if len(buildingFolderPath) > 0:
                subLevel -= 1
                buildingFolderPath.pop()


if __name__ == "__main__":

    levelCompletion = {}
    buildingFolderPath = []
    levelCompletionArray = []
    levelCompletionArrayIndex = 0
    subLevel = -1
    parentFolderLevel = 0

    with open(BOOKMARK_PATH, encoding="utf-8") as myBM:
        data = myBM.read()
        obj = json.loads(data)
        my_sites = []
        building_tree_DS(obj["roots"]["bookmark_bar"])
        asyncio.run(download_webpage_list(my_sites))
