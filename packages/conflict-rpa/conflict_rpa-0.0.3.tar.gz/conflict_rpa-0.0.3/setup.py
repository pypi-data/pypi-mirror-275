import os
import platform
import subprocess
from shutil import copyfile

from setuptools import setup, find_packages, Command
from setuptools.command.develop import develop
from setuptools.command.install import install


def cmd_install():
    home_dir = os.path.expanduser("~")
    profile_path = os.path.join(home_dir, 'Documents', 'WindowsPowerShell', 'Microsoft.PowerShell_profile.ps1')
    script_source = os.path.join(os.path.dirname(__file__), '.', 'record_last_command.psm1')
    script_target = os.path.join(home_dir, 'record_last_command.psm1')

    # Copy the module to the home directory
    if not os.path.exists(script_target):
        copyfile(script_source, script_target)

    # Ensure the profile path exists
    os.makedirs(os.path.dirname(profile_path), exist_ok=True)

    # Update the profile to import the module
    if os.path.exists(profile_path):
        with open(profile_path, 'r') as file:
            content = file.read()
        import_module_cmd = 'Import-Module "$HOME\\record_last_command.psm1"'
        if import_module_cmd not in content:
            with open(profile_path, "a") as profile_file:
                profile_file.write('\n' + import_module_cmd + '\n')
                print(f"Added module import command to PowerShell profile")
        else:
            print(f"Module import command already exists in PowerShell profile")
    else:
        with open(profile_path, "w") as profile_file:
            profile_file.write(f'import-module "$HOME\\record_last_command.psm1"\n')
            print(f"Created PowerShell profile and added module import command")

    print('done')


def add_bashrc_content():
    shell = os.getenv('SHELL')
    if shell:
        shellrc_content = """
    crpa() {
        local last_command=$(fc -ln -1)
        rpa_main "${last_command}"  "$@"
    }
    """
        home_dir = os.path.expanduser("~")
        shell_files = ['.bashrc', '.zshrc']

        if 'bash' in shell:
            shellrc_path = os.path.join(home_dir, '.bashrc')
            shell_file = '.bashrc'
        elif 'zsh' in shell:
            shellrc_path = os.path.join(home_dir, '.zshrc')
            shell_file = '.zshrc'
        else:
            return
        if os.path.exists(shellrc_path):
            with open(shellrc_path, 'r') as file:
                content = file.read()
            if "crpa()" not in content:
                with open(shellrc_path, "a") as shellrc_file:
                    shellrc_file.write(shellrc_content)
                    print(f"Added custom command to {shell_file}")
                # Source the updated shell configuration
                source_command = f"source {shellrc_path}"
                subprocess.run(source_command, shell=True)
                print(f"Sourced {shell_file} to apply changes")
            else:
                print(f"Custom command already exists in {shell_file}")
        else:
            print(f"{shell_file} not found")
    else:
        return


def remove_bashrc_content():
    home_dir = os.path.expanduser("~")
    bashrc_path = os.path.join(home_dir, '.bashrc')

    with open(bashrc_path, "r") as bashrc_file:
        lines = bashrc_file.readlines()

    with open(bashrc_path, "w") as bashrc_file:
        skip = False
        for line in lines:
            if line.strip() == "crpa()":
                skip = True
            if not skip:
                bashrc_file.write(line)
            if skip and line.strip() == "}":
                skip = False
        print("Removed custom command from .bashrc")


class CustomInstallCommand(install):
    """Customized setuptools install command"""

    def run(self):
        shell = os.getenv('SHELL')
        if shell:
            install.run(self)
            add_bashrc_content()
        if platform.system() == 'Windows':
            comspec = os.getenv('ComSpec')
            if comspec:
                if 'cmd.exe' in comspec.lower():
                    install.run(self)
                    cmd_install()


class CustomDevelopCommand(develop):
    def run(self):
        shell = os.getenv('SHELL')
        if shell:
            develop.run(self)
            add_bashrc_content()
        if platform.system() == 'Windows':
            comspec = os.getenv('ComSpec')
            if comspec:
                if 'cmd.exe' in comspec.lower():
                    install.run(self)
                    cmd_install()


setup(
    name='conflict_rpa',
    version='0.0.3',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'openai',
        'requests'
    ],
    author='FanYangli',
    author_email='1800017759@pku.edu.cn',
    description="A tool to rpa in your shell",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    cmdclass={
        'install': CustomInstallCommand,
        'develop': CustomDevelopCommand,
    },
    entry_points='''
        [console_scripts]
        rpa_main=conflict_rpa.rpa:rpa
    ''',
    package_data={
        'crpa': ['../record_last_command.psm1'],
    }, )
