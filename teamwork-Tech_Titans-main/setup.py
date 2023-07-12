from setuptools import setup, find_namespace_packages
setup(
    name="personal_assistant_Tech_Titans",
    version= "0.1",
    description= " Proekt rabotae s phon book , notebook, clean papki po formats ",
    url='https://github.com/Topsya/teamwork-Tech_Titans',
    author= "Anton Mescheryakov, Denis Mashtak, Elizaveta Kolesnyk, Oleg Dovhyi",
    author_email= "topsya1986@gmail.com,  ned.warov@gmail.com,  kolesnyk.elyzaveta24.1201@gmail.com,  oleg.dovgyy@gmail.com",
    data_files=[('personal_assistant_Tech_Titans/mygame',['personal_assistant_Tech_Titans/mygame/background.png',
                                                          'personal_assistant_Tech_Titans/mygame/bonus.png',
                                                          'personal_assistant_Tech_Titans/mygame/enemy.png',
                                                           'personal_assistant_Tech_Titans/mygame/player.png',
                                                           'personal_assistant_Tech_Titans/mygame/goose/1-1.png',
                                                           'personal_assistant_Tech_Titans/mygame/goose/1-2.png',
                                                           'personal_assistant_Tech_Titans/mygame/goose/1-3.png',
                                                           'personal_assistant_Tech_Titans/mygame/goose/1-4.png',
                                                           'personal_assistant_Tech_Titans/mygame/goose/1-5.png'])],
    packages= find_namespace_packages(),
    include_package_data=True,
    install_requires=['pyowm'],
    entry_points={
          'console_scripts': ['assistant=personal_assistant_Tech_Titans.Menu_project:menu']
          }
)