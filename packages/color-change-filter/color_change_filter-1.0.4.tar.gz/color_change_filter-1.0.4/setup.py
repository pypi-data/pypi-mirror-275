import setuptools

with open("README.md", "r",encoding="UTF-8") as fh:
    long_description = fh.read()
setuptools.setup(
  name="color_change_filter",
  version="1.0.4",
  author="Chihiro senbonmatsu",
  author_email="s2222020@stu.musahino-u.ac.jp",
  description="Change color of image",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/senbonmatsu/color_changer",
  project_urls={
    "Bug Tracker": "https://github.com/senbonmatsu/color_changer",
  },
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  package_dir={"": "src"},
  py_modules=["program6"],
  packages=setuptools.find_packages(where="src"),
  Python_requires=">=3.6",
  entry_points={
    "console_scripts": [
      "color_change_filter = program6:main",
    ],
  },
)
