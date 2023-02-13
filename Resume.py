#resume_config = []
res_confg={}
about = {'name':'Roman Korobkov', 'profession': 'design engineer'}
education = {'nameinst': 'National Aerospace University «Kharkiv Aviation Institute»', 'time': '2015-2020', 'facult': 'Robotic systems and complexes', 
    'quote': 'National Aerospace University «Kharkiv Aviation Institute» (KhAI) is a higher education institution of the highest level of accreditation in Ukraine. It is one of the oldest technology universities in Ukraine.Beginning its history on June 1, 1930, NAU "KHAI" has graduated more than 100,000 highly qualified specialists.'}
about_me={'my_interests': ['3d modeling', 'animals, also dog and cat', 'cars'], 'I_like': ['trips', 'descents by kayak', 'delicious food']}
skills={'3d design':['SolidWorks', 'Inventor', 'Kompas', 'AutoCAD'], 'drawing design': ['SolidWorks','Kompas', 'AutoCAD'], 'tests': ['creating and writing a test program', 'test support']}
#resume_config.append(about)
#resume_config.append(education)
#resume_config.append(about_me)
#resume_config.append(skills)
res_confg.update(about)
res_confg.update(education)
res_confg.update(about_me)
res_confg.update(skills)
print(res_confg)
resumetxt= open('resumetxt.txt', 'w')
for key, value in res_confg.items():
    resumetxt.write(f'{key}, {value}\n')
resumetxt.close()