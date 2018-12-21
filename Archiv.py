import os
import zipfile
 
fantasy_zip = zipfile.ZipFile('Pic/Experiment.zip', 'w')
 
for folder, subfolders, files in os.walk('Pic/'):
 
    for file in files:
        if file.endswith('.jpg'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'Pic/'), compress_type = zipfile.ZIP_DEFLATED)
 
fantasy_zip.close()
