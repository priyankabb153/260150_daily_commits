"""pip help
pip help operation
pip help install

pip list
pip show package_name
pip show pip
pip search anystring
pip search pip
pip install pygame
pip install --user pygame
pip install -U package_name
pip install pygame==1.9.2
pip uninstall package_name

List of main pip activities looks as follows:

pip help operation - shows brief pip's description;
pip list - shows list of currently installed packages;
pip show package_name - shows package_name info including package's dependencies;
pip search anystring - searches through PyPI directories in order to find packages which name contains anystring;
pip install name - installs name system-wide (expect problems when you don't have administrative rights);
pip install --user name - install name for you only; no other your platform's user will be able to use it;
pip install -U name - updates previously installed package;
pip uninstall name - uninstalls previously installed package;
"""