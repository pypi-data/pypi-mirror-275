from __future__ import absolute_import

from setuptools import find_packages, setup

with open('./README.md', 'r') as f:
    readme = f.read()


setup(
    name='github-project-automation',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],
    url='https://github.com/khulansot/github-project-automation',
    license='MIT',
    author='KhulnaSoft Ltd',
    author_email='info@khulnasoft.com',
    description='GitHub automatic project manager tool',
    install_requires=[
        'click',
        'requests',
        'python-dateutil',
        'gql==3.0.0a5'
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    keywords=[
        "GitHub",
        "Project",
        "Manager",
        "github-project-automation",
        "project",
        "manage",
        "manager"
    ],
    long_description=readme,
    long_description_content_type='text/markdown',
    python_requires=">=3.7",
    entry_points={
        'console_scripts': ['github-project-automation = github_project_automation.cli.main:main']
    },
    classifiers=[
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ]
)
