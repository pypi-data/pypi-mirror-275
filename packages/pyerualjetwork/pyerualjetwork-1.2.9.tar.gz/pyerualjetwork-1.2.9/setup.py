from setuptools import setup, find_packages

# Setting Up

setup(
      
      name = "pyerualjetwork",
      version = "1.2.9",
      author = "Hasan Can Beydili",
      author_email = "tchasancan@gmail.com",
      description= "Advanced python deep learning library. New Visualize parameter added ('y' or 'n') for TrainPlan and TestPLAN funcs. (Documentation in desc. Examples in GİTHUB: https://github.com/HCB06/PyerualJetwork)",
      packages = find_packages(),
      keywords = ["model evaluation", "classifcation", 'pruning learning artficial neural networks'],
      install_requires=[
          'numpy',
          'scipy',
            'time',
            'math',
            'colorama',
            'typing'
            ],
      
       extras_require={
          'visualization': ['matplotlib','seaborn']
      }
      
      )