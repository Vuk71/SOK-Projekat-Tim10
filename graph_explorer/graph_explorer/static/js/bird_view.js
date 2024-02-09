//menja boju noda nad kojim se poziva
function birdNodeClick(node) {
    d3.select(node).select('circle')
        .attr("fill", "#3AA9AD")
        .transition()
        .duration(2000)
        .attr("fill", "#FFFFFF");
}

//omogucava zumiranje, poziva se u fitZoom
var zoom = d3.behavior
    .zoom()
    .scaleExtent([1/4, 4])
    .on('zoom.zoom', function () {
        svg_bird.attr('transform',
            'translate('+ d3.event.translate + ')' + 'scale(' + d3.event.scale + ')');
    });

//zumira selektovano
var svg_bird = d3.select("#bird_svg")
    .append("g").attr("id", "bird_g")
    .call(zoom);

console.log(edges);
console.log(nodes);

//simulacija sila
var force_bird = d3.layout.force()
        .size([500, 500])
        .nodes(d3.values(nodes))
        .links(edges)
        .on('tick', tick_bird)
        .linkDistance(300)
        .charge(-500)
        .start();

var edge_b = svg_bird.selectAll('.edge')
    .data(edges)
    .enter().append('line')
    .attr('class', 'bird_view_edge');

var node_b = svg_bird.selectAll('.bird_view_node')
    .data(force_bird.nodes())
    .enter().append('g')
    .attr('class', 'bird_view_node')
    .attr('id', function (d) {
        return "bird" + d.id;
    })
    .on("click", function () {
        birdNodeClick(this);
    });

d3.selectAll('.bird_view_node').each(function (d) {
    birdView(d);
});

//primenjuje simulaciju
function lapsedFitZoom(ticks, transitionDuration) {
    for (var i = ticks || 100; i > 0; --i) force_bird.tick();
    force_bird.stop();
    fitZoom(transitionDuration);
}

lapsedFitZoom(undefined, 500);
fitZoom(500);

//izracunava zoom faktor
function fitZoom(transitionDuration) {
    var bounds = svg_bird.node().getBBox();
    var parent = svg_bird.node().parentElement;
    var fullWidth = parent.clientWidth || parent.parentNode.clientWidth,
        fullHeight = parent.clientHeight || parent.parentNode.clientHeight;
    var width = bounds.width,
        height = bounds.height;

    console.log("Sirina: " + width);
    console.log("Visina: " + height);

    if (width === 0 || height === 0) return;
    if (width < 300 && height < 300) {
        width = 300;
        height = 300;
    }
    var scale = 0.15 / Math.max(width / fullWidth, height / fullHeight);

    var translate = [fullWidth / 3.5, fullHeight / 3.5];

    svg_bird.transition()
        .duration(transitionDuration || 0)
        .call(zoom.translate(translate).scale(scale).event);
    svg_bird.on('.zoom', null);
}

//prikaz sa odredjenim idjem
function birdView(d) {
    d3.select("g#" + "bird_" + d.id).append('circle')
        .attr('r', 10)
        .attr('fill', '#FFFFFF');
}

//azurira poziciju
function tick_bird() {
    node_b.attr("cx", function (d) {return d.x;})
        .attr("cy", function (d) {return d.y;});

    node_b.attr("transform", function (d) {
        return "translate(" + d.x + "," + d.y + ")";
    });

    edge_b.attr('x1', function (d) {return d.source.x;})
        .attr('y1', function (d) {return d.source.y;})
        .attr('x2', function (d) {return d.target.x;})
        .attr('y2', function (d) {return d.target.y;});

}

//ucitava html dokument pa upravlja njime
$(document).ready(function () {
    var gDimensions = document.getElementById('main_view').getBoundingClientRect();

    var littleGHeight = gDimensions.height;
    var littleGWidth = gDimensions.width;

    console.log("aaa");
    console.log(littleGHeight);
    console.log(littleGWidth);

    svg_bird.append('rect')
        .attr('height', littleGHeight)
        .attr('width', littleGWidth)
        .attr('fill', 'none')
        .attr('stroke', '#3AAA9D')
        .attr('id', 'frame');

    svg_bird.append('rect')
        .attr('height', littleGHeight)
        .attr('width', littleGWidth)
        .attr('fill', 'none')
        .attr('stroke', '#FFFFFF');
})


