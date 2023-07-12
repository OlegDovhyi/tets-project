from pathlib import Path
import shutil
import os



def move_files(path):

   imeges = ['jpeg', 'png', 'jpg', 'svg']
   documents = ['doc', 'docx', 'txt', 'pdf', 'xlsx', 'pptx']
   audio = ['mp3', 'ogg', 'wav', 'amr']
   video = ['avi', 'mp4', 'mov', 'mkv']
   archives = ['zip', 'gz', 'tar']
   Spisok_papok = ('imeges','documents','audio','video','archives')
   
   # створюєм папки
   for folder in Spisok_papok:
      if not os.path.exists(f'{path}\\{folder}'):
         os.mkdir(f'{path}\\{folder}')


   Spisok = os.listdir(path)  
   for file in Spisok :
      #  if os.path.isfile(file):
         extension = file.split(".")
            #збираю всі розширення
     # razresh += extension[1]   
       
         if  len(extension) > 1 and extension[-1].lower() in imeges :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'imeges',file)
            shutil.move(old_path,new_path)  
         elif  len(extension) > 1 and extension[-1].lower() in documents :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'documents',file)
            shutil.move(old_path,new_path)
         elif  len(extension) > 1 and extension[-1].lower() in audio :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'audio',file)
            shutil.move(old_path,new_path)  
         elif  len(extension) > 1 and extension[-1].lower() in video :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'video',file)
            shutil.move(old_path,new_path)  
         elif  len(extension) > 1 and extension[-1].lower() in archives :
            old_path = os.path.join(path, file)
            new_path = os.path.join(path,'archives',file)
            shutil.move(old_path,new_path)
    

   pattern_parsinga = path.iterdir()
   for i in pattern_parsinga:

            if  i.is_dir():                
                if i.name in Spisok_papok:
                    print(f'Не видаляти папку  {i.name} ')
                else:
                    print(f'Цю папку {i.name} потрібно видалити')   
                    try:
                        os.rmdir(i)
                    except: OSError
                    else:
                        print(f' Папка {i} видалена')
                    finally:
                        print('Зробленно  -----')

  # list_vse_razresh = set(razresh) 
# # залишаю лише унікальні розширення
   list_music =  os.listdir(os.path.join(path,'audio')) 
   list_video = os.listdir(os.path.join(path,'video')) 
   list_foto = os.listdir(os.path.join(path,'imeges'))
   list_doc  = os.listdir(os.path.join(path,'documents'))
   list_archiv =os.listdir(os.path.join(path,'archives'))
   # list_neizvestnie = path.glob('*.*')

   print ({  
              'list_music':  list_music,
              'list_video': list_video,
              'list_foto': list_foto,
              'list_doc': list_doc,
              'list_archiv': list_archiv,
            # 'list_vse_razresh': list_vse_razresh,
            # 'list_neizvestnie': list_neizvestnie,
            })
     
# Список файлів в кожній категорії (музика, відео, фото та ін.)
# Перелік усіх відомих скрипту розширень, які зустрічаються в цільовій папці.
# Перелік всіх розширень, які скрипту невідомі.

if __name__ == '__main__': 
      path = Path(input('Введіть путь папки де потрібно зробити сортування файлів: '))
      move_files (path)