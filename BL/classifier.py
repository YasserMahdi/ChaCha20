

text = ['textFiles', 'doc', 'docx', 'docm', 'odt', 'pdf', 'txt', 'rtf', 'pages', 'pfb', 'mobi', 'chm', 'tex', 'bib',
        'dvi', 'abw', 'text', 'epub', 'nfo', 'log', 'log1', 'log2', 'wks', 'wps', 'wpd', 'emlx', 'utf8', 'ichat', 'asc',
        'ott', 'fra', 'opf']
image = ['imageFiles', 'img', 'jpg', 'jpeg', 'png', 'png0', 'ai', 'cr2', 'ico', 'icon', 'jfif', 'tiff', 'tif', 'gif',
         'bmp', 'odg', 'djvu', 'odg', 'ai', 'fla', 'pic', 'ps', 'psb', 'svg', 'dds', 'hdr', 'ithmb', 'rds', 'heic',
         'aae', 'apalbum', 'apfolder', 'xmp', 'dng', 'px', 'catalog', 'ita', 'photoscachefile', 'visual', 'shape',
         'appicon', 'icns']

allcats = [text, image]


# main function, for generating the values based on data read, assumes lowercase extension without dot
def classify(extension):
    for category in allcats:
        if extension in category:
            entry = category[category.index(extension)]
            if ((entry in extension) and (extension in entry)):
                # blank comment
                if (category[0] == 'textFiles'):
                    return 'textFiles'
                else:
                    return 'imageFiles'

    else:
        return 'unclassifiable'
