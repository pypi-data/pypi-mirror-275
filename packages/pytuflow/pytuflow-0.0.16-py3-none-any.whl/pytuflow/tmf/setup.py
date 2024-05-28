import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tuflow-model-files",
    version="0.0.25",
    author="Ellis Symons",
    author_email="support@tuflow.com",
    description="Package tuflow-model-files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["tmf",
              "tmf.data",
              "tmf.tuflow_model_files",
              "tmf.tuflow_model_files.abc",
              "tmf.tuflow_model_files.cf",
              "tmf.tuflow_model_files.dataclasses",
              "tmf.tuflow_model_files.db",
              "tmf.tuflow_model_files.inp",
              "tmf.tuflow_model_files.utils",
              "tmf.tuflow_model_files.db.drivers",
              "tmf.convert_tuflow_model_gis_format.conv_tf_gis_format",
              "tmf.convert_tuflow_model_gis_format.conv_tf_gis_format.helpers",
              "tmf.convert_tuflow_model_gis_format.conv_tf_gis_format.helpers.stubs",
              "tmf.convert_tuflow_model_gis_format.conv_tf_gis_format.data"],
    package_data={
        'tmf.data': ['*.json'],
        'tmf.convert_tuflow_model_gis_format.conv_tf_gis_format.data': ['*.json'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)