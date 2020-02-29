set -e

# locate the py package directory
SOURCE_DIR=$(pwd)/../swiptapi-py

# reset working directory to that of the py package
pushd ${SOURCE_DIR}

	# install the py package in the current directory
    python3 setup.py develop
popd