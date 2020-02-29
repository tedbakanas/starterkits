#' @title Create Random Swiss Plot
#' @name CreateRandomSwissPlot
#' @description Uses the other functions in the swiptapi package to create a plot of busses in Switzerland.
#' 
#' @param filePath The full qualified path at which to write the plot
#' @importFrom leaflet leaflet addTiles addMarkers
#' @importFrom htmltools save_html
#' @importFrom logging loginfo
#' @export
CreateRandomSwissPlot <- function(filePath){
    
    point <- GetRandomSwissPoint()
    
    logging::loginfo(paste("Point selected:",point$x,point$y))
    
    swiAPI <- SwiPtApiClient$new()
    response <- swiAPI$SearchAroundPoint(lati = point$x,longi = point$y)
    
    logging::loginfo("Making plot")
    
    m <- leaflet::leaflet()
    m <- leaflet::addTiles(m)
    m <- leaflet::addMarkers(
        m,
        lng = response[["stations"]][["coordinate"]][["y"]],
        lat = response[["stations"]][["coordinate"]][["x"]],
        popup = response[["stations"]][["name"]]
    )
    logging::loginfo(paste("Saving plot:",filePath))
    htmltools::save_html(html = m,file = filePath)
    
}

#' @title Get Random Swiss Point
#' @name GetRandomSwissPoint
#' @description Uses basic math to pick a point in a circle that roughly approximates Switzerland
#' 
#' @return a named list of x and y lat/long coordinates
#' 
#' @importFrom logging loginfo
#' @export
GetRandomSwissPoint <- function(){
    
    logging::loginfo("Switzerland doesn't really look like a circle but thats ok!")
    
    swiCenterX <- 46.801111
    swiCenterY <- 8.226667
    radius <- sample(seq(0,2.3,0.01),1)
    theta <- sample(seq(0,2*pi,.1),1)
    x <- swiCenterX + radius*cos(theta)
    y <- swiCenterY + radius*sin(theta)
    return(list(x = x,y = y))
}