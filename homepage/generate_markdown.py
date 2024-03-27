# -*- coding: utf-8 -*-
'''
Created on Sun Mar 24 13:23:22 2024

@author: pctab
'''

import json
import os
import sys
homedir = r'C:/Users/pctab/Dropbox/Projects/Homepage/homepage/'


def get_paragraph(string):
    res = []
    for line in string.splitlines():
        res += line.split(' ')
    return ' '.join(res)


with open(os.path.join(homedir, 'data/summary.json')) as f:
    summary = json.load(f)
summary_str = summary['summary']
# print(summary_str)


with open(os.path.join(homedir, 'data/experience.json')) as f:
    experience = json.load(f)
experience_str = ''
for e in experience:
    x = '''- ### [{}]({})\n\t**{}**\n\n\t{}\n\n\t📅 {}\n\n\t🗺 {}\n\n\t---'''.format(
        e['company'],
        e['website'],
        e['position'],
        e['description'],
        e['duration'],
        e['location'],)
    experience_str += x+'\n'
# print(experience_str)

with open(os.path.join(homedir, 'data/education.json')) as f:
    education = json.load(f)

education_str = ''

for e in education:
    x = '''- ### [{}]({})\n\n\t**[{}]({})**\n\n\t📅 {}\n\n\t---'''.format(
        e['school'],
        e['website_school'],
        e['degree'],
        e['website_degree'],
        e['duration'],)
    education_str += x+'\n'
# print(education_str)


with open(os.path.join(homedir, 'data/projects_list.json')) as f:
    projects = json.load(f)
project_str = ''

for i, e in enumerate(projects):
    x = ''
    if e['demonstration'] != '' and e['code'] != '':
        x = '''{}.\t### [{}]({})\n\n\t<p>{}</p>\n\n\t[code]({})\n\n\t___'''.format(
            i+1,
            e['title'],
            e['demonstration'],
            get_paragraph(
                e['description']),
            e['code'])
    elif e['demonstration'] != '':
        x = '''{}.\t### [{}]({})\n\n\t<p>{}</p>\n\n\t___'''.format(
            i+1,
            e['title'],
            e['demonstration'],
            get_paragraph(
                e['description']),
        )
    elif e['code'] != '':
        x = '''{}.\t### {}\n\n\t<p>{}</p>\n\n\t[code]({})\n\n\t___'''.format(
            i+1,
            e['title'],
            get_paragraph(
                e['description']),
            e['code'])
    else:
        x = '''{}.\t### {}\n\n\t<p>{}</p>\n\n\t___'''.format(
            i+1,
            e['title'],
            get_paragraph(
                e['description'])
        )
    project_str += x+'\n'
# print(project_str)

with open(os.path.join(homedir, 'data/contacts.json')) as f:
    contacts = json.load(f)
contact_str = ''

for i, e in enumerate(contacts):
    x = '''- **{}** [{}]({})'''.format(
        e['method'],
        e['disp'],
        e['url'])
    contact_str += x+'\n'
# print(contact_str)

with open(os.path.join(homedir, 'data/achievements.json')) as f:
    achievements = json.load(f)
achievement_str = ''

for i, e in enumerate(achievements):
    x = '''- **{}** [{}]({})'''.format(
        e['achievement'],
        e['description'],
        e['link'])
    achievement_str += x+'\n'
# print(achievement_str)

with open(os.path.join(homedir, 'data/skills.json')) as f:
    skills = json.load(f)
skill_str = ''

for e in skills:
    x = '''- **{}**: {}'''.format(
        e['title'],
        ', '.join(e['details']),
    )
    skill_str += x+'\n'
# print(skill_str)

with open(os.path.join(homedir, 'data/certificates.json')) as f:
    certificates = json.load(f)
certification_str = '|||||\n'
certification_str += '|:----:|:----:|:----:|:----:|\n'


c = 4
table = []
row = []
for i, e in enumerate(certificates):
    if i % 4 == 0:
        row.clear()
    src = e['src']
    # src = src.replace('static', 'homepage')
    x = '''[{}]({}) <img src="{}" width=200 height=160 >'''.format(
        e['title'],
        e['credential'],
        src)
    row.append(x)
    # print(src)

    if i % 4 == 3:
        certification_str += "|"+'|'.join(row)+"|"
        certification_str += '\n'

        row.clear()
if row:
    certification_str += "|"+'|'.join(row)+"|"
    certification_str += '\n'
# print(certification_str)


def generate_markdown():
    stdout = sys.stdout
    os.chdir('..')

    f = open('readme.md', 'w',encoding='utf8')
    sys.stdout = f

    print('# RAHUL KUMAR')
    print()
    print('## Summary')
    print()
    print(summary_str)
    print('\n---\n',)

    print('## Experience')
    print()
    print(experience_str)
    print('\n---\n',)

    print('## Education')
    print()
    print(education_str)
    print('\n---\n',)

    print('## Projects')
    print()
    print(project_str)
    print('\n---\n',)
    
    print('## Skills')
    print()
    print(skill_str)
    print('\n---\n',)

    print('## Achievements')
    print()
    print(achievement_str)
    print('\n---\n',)

    print('## Certifications')
    print()
    print(certification_str)
    print('\n---\n',)

    print('## Contact')
    print()
    print(contact_str)
    print('\n---\n',)
    
    sys.stdout=stdout
    f.close()

generate_markdown()

# =============================================================================
# skills = {
#     'Programming Languages': ['Python', 'C', 'C++', 'Java', 'Kotlin', 'JavaScript'],
#     'Data Analysis and Statistics': ['Advanced Data Structures',
#                                      'Algorithms',
#                                      'Probabilistic Modeling',
#                                      'Inference',
#                                      'Estimation',
#                                      'Hypothesis Testing,',
#                                      'Prediction',
#                                      'Data Analysis'],
#     'Artificial Intelligence': ['Search',
#                                 'Optimization',
#                                 'Reinforcement Learning',
#                                 'Bayes-Net',
#                                 'Knowledge-Based Agents'],
#     'Machine Learning': ['Regression',
#                          'Classification',
#                          'Clustering',
#                          'Recommendation',
#                          'Collaborative Filtering',
#                          'Non-Parametric Models'],
#     'Tools and Libraries': ['TensorFlow',
#                             'PyTorch',
#                             'Keras',
#                             'Scikit-Learn',
#                             'Seaborn',
#                             'Matplotlib',
#                             'OpenCV'],
#     'Computer Vision': ['Object Detection',
#                         'Image Segmentation',
#                         'Geometric Transformations',
#                         'Synthetic Dataset Geneation',
#                         'Object Tracking'],
#     'Android Development': ['Java,',
#                             'Kotlin',
#                             'ML model porting',
#                             'Services',
#                             'Fragments',
#                             'Rest APIs',
#                             'Sensor Access',
#                             'Python Script on Android'],
#     'Web Development': ['JavaScript',
#                         'Flask',
#                         'Django',
#                         'HTML',
#                         'SAAS',
#                         'CSS',
#                         'Bootstrap',
#                         'SQL',
#                         'MVC',
#                         'Git'],
#     'IOT': ['Arduino',
#             'Sensors',
#             'Wireless Control']
# }
# skills=[{'title':title,'details':details} for title,details in skills.items()]
# with open('data/skills.json','w') as f:
#     json.dump(skills, f)
#
# =============================================================================
