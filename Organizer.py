import os
import shutil

current_dir = os.getcwd()

for f in os.listdir(current_dir):
    filename, file_ext = os.path.splitext(f)

    try:
        if not file_ext:
            pass
        elif file_ext in ('.py'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Python-files', f'{filename}{file_ext}'))

        elif file_ext in ('.jpg', '.png', '.gif'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'image-files', f'{filename}{file_ext}'))    

        elif file_ext in ('.txt'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'txt-files', f'{filename}{file_ext}'))

        elif file_ext in ('.lnk', '.url'):
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'Exe-files', f'{filename}{file_ext}'))

        else:
            shutil.move(
                os.path.join(current_dir, f'{filename}{file_ext}'),
                os.path.join(current_dir, 'others', f'{filename}{file_ext}'))           

    except (FileNotFoundError, PermissionError):
        pass