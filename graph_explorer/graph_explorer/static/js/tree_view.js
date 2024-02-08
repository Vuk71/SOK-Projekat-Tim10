"use strict";
var rootNode = treeData.name; // Definition of the root node of a tree
function _drawTree(treeData) {

    // Setting the margins and dimensions for the tree display
    var margin = {
        top: 55,
        right: 20,
        bottom: 30,
        left: 30
    };
    var width = 200 - margin.left - margin.right;
    var barHeight = 40;
    var barWidth = width * 0.40;
    var i = 0;
    var duration = 400;
    var root;

    // Tree layout definition
    var tree = d3.layout.tree()
        .nodeSize([0, 75])
        .children(function(d) {
            return d.children;
        });

    // Function to draw lines between nodes
    var line = d3.svg.line().interpolate('step')
        .x(function(d) {
            return d.x - 20;
        })
        .y(function(d) {
            return d.y - 40;
        });

    // Adding a div element to display the tooltip
    var div = d3.select('#tree')
        .append('div')
        .attr('class', 'tooltip')
        .style('opacity', 0);

    // Adding an SVG element to display the tree
    var tree_svg = d3.select('#tree').append('svg').attr('class', 'tree_view_svg')
        .append('g')
        .attr('transform', `translate(${ margin.left },${ margin.top })`).attr('class', 'svg_g');

    // A function to generate data for a line
    function lineData(d) {
        var points = [{
                x: d.source.y + barWidth / 2,
                y: d.source.x + barHeight - 5
            },
            {
                x: d.target.y + 20,
                y: d.target.x + barHeight / 1.5
            }
        ];
        return line(points);
    }

    // Setting up the root node
    root = treeData;
    root.x0 = 0;
    root.y0 = 0;

    // Updating the tree view
    update(root);

    // Setting the width of an SVG element
    d3.select('.tree_view_svg')
        .attr('width', $(".svg_g")[0].getBBox().width * 1.4);

    // Function to update the tree view
    function update(source) {
        var tree_nodes = tree.nodes(root);

        // Calculating the height of an SVG element based on the number of nodes
        var height = Math.max(500, tree_nodes.length * barHeight + margin.top + margin.bottom);

        // Transition the SVG element to the appropriate height
        d3.select('.tree_view_svg').transition()
            .duration(duration)
            .attr('height', height);

        // Updating the positions of nodes in the tree
        tree_nodes.forEach(function(n, i) {
            n.x = i * barHeight / 1.2;
        });
        tree_nodes.y = barHeight / 1.5;

        // Updating nodes in tree view
        var tree_node = tree_svg.selectAll('g.tree_node')
            .data(tree_nodes, function(d) {
                return d.id || (d.id = ++i);
            });

        // Adding new nodes
        var nodeEnter = tree_node.enter().append('g')
            .attr('class', 'tree_node')
            .attr('transform', function() {
                return `translate(${ source.y0},${ source.x0 })`;
            })
            .style('opacity', 1e-6).style('text-align', 'left');

        // A function to get the attribute in the form of a string
        function getAttributes(attributes) {
            var str = "";
            for (const [key, value] of Object.entries(attributes)) {
                str += "- " + key + " : " + value + "<br>";
            }
            return str;
        }

        //Adding rectangles (nodes) and defining actions on events
        nodeEnter.append('rect')
            .attr('y', -barHeight / 2)
            .attr('height', function() {
                return barHeight / 2
            })
            .attr('width', function(d) {
                return d.naziv.length * 16
            })
            .style('font-size', '15px').style('fill', function(d) {
                return d.color
            }).style('text-align', 'center')
            .attr('class', 'ractangle')
            .on('click', click)
            .on('mouseover', function(d) {
                // Setting the tooltip on hover
                div.transition()
                    .duration(500)
                    .style('opacity', 0);
                div.transition()
                    .duration(200)
                    .style('opacity', 1)
                    .style('pointer-events', 'auto')
                    .style('visibility', 'visible');
                div.html(
                        `<h3 class = 'popover-title' >${ d.naziv }</h3>
                    <br>
                    <p class='popover-assets'>
                            ${ getAttributes(d.attributes) }
                    </p>`)
                    .style('left', '20%')
                    .style('top', '80px').style('color', '#3AA9AD').style('font-size', '15px');
            }).on('mouseout', function(d) {
                // Hiding the tooltip when the mouse moves away
                setTimeout(function() {
                    if (!$('.tooltip:hover').length) {
                        div.transition()
                            .duration(500)
                            .style('opacity', 1);
                        div.transition()
                            .duration(500)
                            .style('opacity', 0)
                            .style('pointer-events', 'none')
                            .style('visibility', 'hidden');
                    }
                }, 0);
            });

        // Adding text to nodes
        nodeEnter.append('text').attr('id', function(d) {
                return 'text_' + d.name;
            })
            .attr('dy', -7)
            .attr('dx', 10.5)
            .style('fill', fontColor).style('text-align', 'left')
            .attr('font-size', 10).attr('font-family', 'sans-serif').text(function(d) {
                if (d.attr === true) {
                    return "- " + d.naziv;
                } else {
                    return "+ " + d.naziv;
                }
            });

        // Updating nodes
        tree_node.transition()
            .duration(duration)
            .attr('transform', function(d) {
                return `translate(${ d.y },${ d.x })`;
            })
            .style('opacity', 1)
            .select('rect')
            .select('text')
            .style('fill', fontColor).style('border', function(d) {
                return d.color
            }).style('fill', function(d) {
                console.log("Boja")
                return d.color
            });

        // Transition of new nodes
        nodeEnter.transition()
            .duration(duration)
            .attr('transform', function(d) {
                return `translate(${ d.y },${ d.x })`;
            })
            .style('opacity', 1);

        // Remove nodes that are no longer needed
        tree_node.exit().transition()
            .duration(duration)
            .attr('transform', function() {
                return `translate(${ source.y },${ source.x })`;
            })
            .style('opacity', 1e-6)
            .remove();

        // Updating edges between nodes
        var tree_link = tree_svg.selectAll('path.edge')
            .data(tree.links(tree_nodes), function(d) {
                return d.target.id;
            });

        //Adding new edges
        tree_link.enter().insert('path', 'g')
            .attr('class', 'edge')
            .attr('d', lineData)
            .transition()
            .duration(duration)
            .attr('d', lineData);

        // Updating existing edges
        tree_link.transition()
            .duration(duration)
            .attr('d', lineData);

        // Removing edges that are no longer needed
        tree_link.exit().transition()
            .duration(duration - 400)
            .attr('d', lineData)
            .remove();

        // Updating the initial node positions for the next tree update
        tree_nodes.forEach(function(d) {
            d.x0 = d.x + 50;
            d.y0 = d.y + 400;
        });

        // Updating the width of an SVG element
        d3.select('.tree_view_svg')
            .attr('width', $(".svg_g")[0].getBBox().width * 1.2);
    }

    // A function that is called when a node is clicked
    async function click(d) {
        let main_node = "main_" + d.init_name;
        console.log(main_node);

        // Broadcast a click to the corresponding node in the DOM
        for (var b of node[0]) {
            console.log(b.__data__.init_name);
            if (b.__data__.init_name == d.init_name) {
                b.dispatchEvent(new Event('click'));
            }
        }

        // Changing the display of the text on the clicked node
        if (d.attr === false) {
            if (d3.select('text#text_' + d.name).text() === ("- " + d.naziv))
                d3.select('text#text_' + d.name).text("+ " + d.naziv);
            else
                d3.select('text#text_' + d.name).text("- " + d.naziv);
        }

        // Updating the tree view based on opening/closing children
        if (d.children) {
            d._children = d.children;
            d.children = null;
        } else {
            d.children = await generateChildren(d);
            d._children = null;
        }
        update(d);
    }

    // Function for defining the color of text in nodes
    function fontColor(d) {
        return d._children ? '#FFFFFF' : d.children ? '#FFFFFF' : '#FFFFFF';
    }

    // A function to generate data about the childrens of a node
    function generateChildren(current_node) {
        return new Promise(function(resolve, reject) {
            $.get("/get_children", {
                node_id: current_node.id
            }, function(data) {
                // Parsing the received data in JSON format
                nodes = JSON.parse(data);
                node_data = [];

                // Creating data for nodes based on the obtained data
                for ([key, valueA] of Object.entries(current_node.data)) {
                    node_val = {
                        name: key,
                        naziv: key + " : " + valueA,
                        attributes: {},
                        children: [],
                        attr: true,
                        color: '#3AA9AD'
                    }
                    node_data.push(node_val);
                }

                // Adding children to a node
                nodes.forEach(function(node) {
                    node_val = {
                        name: node.id,
                        init_name: node.init_node_id,
                        naziv: node.name,
                        attributes: node.data,
                        children: [],
                        attr: false,
                        color: '#3AA9AD'
                    }
                    node_data.push(node_val);
                });
                resolve(node_data);
            });
        });
    }
}

// Calling a function to draw a tree with the given data
_drawTree(treeData);