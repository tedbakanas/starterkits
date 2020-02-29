set -e

# locate the R package directory
SOURCE_DIR=$(pwd)/../swiptapi-r

# reset working directory to that of the R package
pushd ${SOURCE_DIR}
	
	# install the dependancies of the R package in the current directory
	Rscript -e 'devtools::install_deps(".")'
    # install the R package in the current directory
    R CMD INSTALL \
        --no-docs \
        .

popd