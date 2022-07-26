import os 
import sys
import shutil

# Check if we have arguments to be retrieved
if len(sys.argv) > 1:
    # path to the XCAsset directory
    path_to_directory = sys.argv[1]
    # string argument that if it contains 'skip' we'll be skipping image thumbnail generation
    skip_image_generation = sys.argv[2] == 'skip' if True else False
else:
    path_to_directory = '/Users/me/Downloads'
    skip_image_generation = False

# get all imageset assets in the XCAsset folder
def get_all_xcassets_imageset_items(path_to_directory):
    directory_contents=os.listdir(path_to_directory)
    item_paths = []

    for item in directory_contents:
        item_path = path_to_directory + "/" + item
        if os.path.isdir(item_path):
            if item.endswith('.imageset'):
                item_paths.append(item_path)
            else:
                item_paths.extend(get_all_xcassets_imageset_items(item_path))

    return item_paths

# get path to individual assets
def get_path_to_images(all_image_asset_items):
    individual_assets=[]
    for path_to_imageasset in all_image_asset_items:
        directory_contents=os.listdir(path_to_imageasset)
        for item in directory_contents:
            path_individual_asset = path_to_imageasset + "/" + item
            if item.endswith('.svg') or item.endswith('.pdf'):
                individual_assets.append(path_individual_asset)
                break
            elif item.endswith('.png') or item.endswith('.jpg') or item.endswith('.jpeg'):
                if '@' in item:
                    item_name = item.split('@')[0]
                    item_extension = item.split('.')[1]
                    x3_item = item_name + "@3x." + item_extension
                    x2_item = item_name + "@2x." + item_extension
                    set_directory_contents = set(directory_contents)
                    if x3_item in set_directory_contents:
                        path = path_to_imageasset + "/" + x3_item
                        individual_assets.append(path)
                        break
                    elif x2_item in set_directory_contents:
                        path = path_to_imageasset + "/" + x2_item
                        individual_assets.append(path)
                        break
                    else:
                        individual_assets.append(path_individual_asset)
                        break
                else:
                    individual_assets.append(path_individual_asset)
                    break
    return individual_assets

# create directories where code and assets will be added
def create_directory_structure():
    parent_directory = '.'
    base_directory = 'html'
    image_directory = 'img'

    base_directory_path = os.path.join(parent_directory, base_directory)

    if os.path.isdir(base_directory_path):
        shutil.rmtree(base_directory_path, ignore_errors=True)
    
    os.mkdir(base_directory_path)

    image_directory_path = os.path.join(base_directory_path, image_directory)
    os.mkdir(image_directory_path)

    html_file_path = base_directory_path + "/index.html"
    with open(html_file_path, 'w') as html_file:
        html_file.write('')
        html_file.close()

    return base_directory_path,image_directory_path,html_file_path

# top most portion of the html file
def get_top_html():
    content = """"
        <html>
        <head>
        <style>
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        th, td {
        background-color: #96D4D4;
        }
        </style>
        </head>
        <body>
        <table>
        <tr>
        <th>Name</th>
        <th>Extension</th>
        <th>File</th>
        <th>Image</th>
        </tr>
    """
    return content

# bottom most part of the html file
def get_bottom_html():
    content = """
    </table>
    </body>
    </html>
    """
    return content

# returns the html for an image row
def get_image_row_html(image_name):
    extension = image_name.split('.')[1].upper()
    content = """
    <tr>
    <td>{}</td>
    <td>{}</td>
    <td></td>
    <td><img src=\"img/{}\" alt=\"{}\" height=\"100\" width=\"100\"></td>
    </tr>
    """.format(image_name,extension,image_name,image_name)
    return content

# returns the html for a pdf row
def get_pdf_row_html(pdf_name, image_name):
    extension = pdf_name.split('.')[1].upper()
    content = """
    <tr>
    <td>{}</td>
    <td>{}</td>
    <td><a href=\"img/{}\" target=\"_blank\">Link</a></td>
    <td><img src=\"img/{}\" alt=\"{}\" height=\"100\" width=\"100\"></td>
    </tr>
    """.format(pdf_name,extension,pdf_name,image_name,pdf_name)
    return content

structure = create_directory_structure()
assets_from_directory = get_all_xcassets_imageset_items(path_to_directory)
images_from_assets = get_path_to_images(assets_from_directory)

with open(structure[2], 'w') as html_file:
    html_file.write(get_top_html())
    for image_path in images_from_assets:
        image_name = os.path.basename(image_path)
        image_extension = image_name.split('.')[1]
        new_image_path = structure[1] + "/" + image_name

        shutil.copyfile(image_path, new_image_path)

        row = ''
        if image_extension != 'pdf':
            row = get_image_row_html(image_name)
        else:
            converted_pdf_to_png_name = image_name + ".png"
            converted_pdf_to_png_name = converted_pdf_to_png_name

            if skip_image_generation == False:
                converted_pdf_to_png_name_path = structure[1] + "/" + converted_pdf_to_png_name
                converted_pdf_to_png_name_path_escaped = converted_pdf_to_png_name_path
                new_image_path_escaped = new_image_path.replace(" ", "\ ")
                convert_command = 'sips -s format png \"' + new_image_path_escaped + '\" --out \"' + converted_pdf_to_png_name_path_escaped + '\"'
                print(convert_command)
                os.system(convert_command)
            row = get_pdf_row_html(image_name,converted_pdf_to_png_name)
        html_file.write(row)

    html_file.write(get_bottom_html())
    html_file.close()
