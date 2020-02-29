# locate the R package directory
SOURCE_DIR=$(pwd)/../swiptapi-r

# reset working directory to that of the R package
pushd ${SOURCE_DIR}
    
    # build the R package in the current directory
    Rscript -e "roxygen2::roxygenize('.')"

popd