function clickNode(el) {
    d3.select(el).select('rect').attr('fill', "#6bcf57")
        .transition()
            .duration(2000)
        .attr('fill', "#57b9cf");

    let bird_node = "bird_" + el.id.split("_")[1];

    for (var b of node_b[0]) {
        if (b.id === bird_node) {
            b.dispatchEvent(new Event('click'));
        }
    }
}

var force = d3.layout.force()
        .size([600, 600])
        .nodes(d3.values(nodes))
        .edges(edges)
        .on("tick", tick)
        .edgeDistance(300)
        .charge(-500)
        .start();

var drag = force.drag()
    .on("dragstart", dragstart);


var svg_complex = d3.select("#main_view").call(d3.behavior.zoom().scaleExtent([0.5, 6]).on("zoom"), function () {
    svg_complex.attr("transform", "translate(" + d3.event.translate + ")" + "scale(" + d3.event.scale + ")")
    svg_bird.select('#frame').remove();

    let svgWidth = document.getElementById('main_view').getBoundingClientRect().width;
    let svgHeight = document.getElementById('main_view').getBoundingClientRect().height;

    let mapWidth = document.getElementById('main_g').getBoundingClientRect().width;
    let mapHeight = document.getElementById('main_g').getBoundingClientRect().height;

    let factor = mapWidth / $("#main_g")[0].getBBox().width;

    let factorSvgWidth = svgWidth / $("#main_g")[0].getBBox().width;
    let factorSvgHeight = svgHeight / $("#main_g")[0].getBBox().height;

    let dx = d3.event.translate[0] / d3.event.scale;
    let dy = d3.event.translate[1] / d3.event.scale;

    svg_bird.append('rect')
        .attr('id', 'frame')
        .attr('width', mapWidth * factorSvgWidth / factor / d3.event.scale )
        .attr('height', mapHeight * factorSvgHeight / factor / d3.event.scale )
        .attr('stroke', "#6bcf57")
        .attr('fill', 'none')
        .attr('transform', `translate(${-dx},${-dy}`);
})
.append("g").attr('id', 'main_g');

var edge = svg_complex.selectAll('.edge')
        .data(edges)
        .enter().append('line')
        .attr('class', 'main_view_edge');

var node = svg_complex.selectAll('.main_view_node')
        .data(force_bird.nodes())
        .enter().append('g')
        .attr('class', '.main_view_node')
        .attr('id', function (d) {
            return "main_" + d.name;
        })
        .on('click', function () {
            clickNode(this);
        })
        .call(drag);

d3.selectAll('.main_view_node').each(function (d) {
    complexView(d);
});

function complexView(d) {
    var length = 150;
    var attrNum = Object.keys(d.data).length;
    console.log(attrNum);

    var fontSize = 10;
    var height = (attrNum === 0) ? fontSize: attrNum * fontSize;
    height += fontSize;

    d3.select("g#" + "main_" + d.id).append('rect').
        attr('x', 0).attr('y', 0).attr('width', length).attr('height', height + 20)
        .attr('fill', "#6bcf57");

    d3.select("g#", "main_" + d.id).append('text').attr('x', length / 2).attr('y', 10)
        .attr('text-anchor', 'middle')
        .attr('font-size', fontSize).attr('font-family', 'sans-serif')
        .attr('fill', "#fff1e6").attr('border', 'bold').text(d.name);

    d3.select("g#", "main_" + d.id).append('line').
        attr('x1', 0).attr('y1', fontSize).attr('x2', length).attr('y2', fontSize)
        .attr('stroke', '#11172F').attr('stroke-width', 1);


    for (var i = 0; i < attrNum; i++) {
        var text = Object.keys(d.data)[i] + " : " + Object.values(d.data)[i];
        d3.select("g#" + "main_" + d.id).append('text').attr('x', 0).attr('y', 20 + i * fontSize)
        .attr('text-anchor', 'start')
        .attr('font-size', fontSize).attr('font-family', 'sans-serif')
        .attr('fill', '#fff1e6').attr('border', 'bold').text(text);

    }

}

function dragstart(d) {
    d3.event.sourceEvent.stopPropagation();
    d3.select(this).classed('fixed', d.fixed = true);
}

function tick() {
    edge.attr("x1", function (d) {return d.source.x; })
        .attr("y1", function (d) {return d.source.y; })
        .attr("x2", function (d) {return d.target.x; })
        .attr("y2", function (d) {return d.target.y; });

    node.attr("cx", function (d) {return d.x; })
        .attr("cy", function (d) {return d.y; });

    node.attr("transform", function (d) {return "translate(" + d.x + ", " + d.y + ")";});
        tick_bird();
}