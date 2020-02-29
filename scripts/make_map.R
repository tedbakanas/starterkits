
# parse the command line inputs
opts <- optparse::parse_args(
    optparse::OptionParser(
        option_list = list(
            optparse::make_option(
                opt_str = "--output_dir"
                , help = "The path to the directory in which to store the plot"
                )
            )
    )
)

# make a filename and a path
filename <- "super_cool_map_R.html"
filepath <- file.path(opts$output_dir,filename)

logging::loginfo(paste("Creating a map at:",filepath))

# create the plot and write it to the path
swiptapi::CreateRandomSwissPlot(filepath)