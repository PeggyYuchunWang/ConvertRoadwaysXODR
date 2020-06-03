using PyCall
using AutomotiveSimulator
using AutomotiveVisualization

function createCurve(segid, laneindex, road_geom, lane)
    tag = LaneTag(segid, laneindex)
    curve = nothing
        if road_geom.type_name == "line"
            length = road_geom.length
            width = float(lane.id)*lane.width.a/2.0
            heading = road_geom.hdg
            x1 = road_geom.x
            x2 = road_geom.x + length*cos(heading)
            y1 = road_geom.y
            y2 = road_geom.y + length*sin(heading)
            dx = width*sin(heading)
            dy = width*cos(heading)
            curve = gen_straight_curve(
                VecE2(x1 + dx, -(y1 + dy)),
                VecE2(x2 + dx, -(y2 + dy)),
                10
            )
        end
    return tag, curve
end

# TODO (Peggy): clean up imports and convert to Module in Julia
# TODO: Curves and other stuff
# TODO: Clean up code and decompose (suggestions welcome :))
function OpenDriveToRoadwaysConverter(filename, roadIndex)
    # read from current directory
    pushfirst!(PyVector(pyimport("sys")."path"), "")
    sys = pyimport("sys")
    # Set up opendrive parser
    openDriveParser = pyimport("src.open_drive_parser")
    odp = openDriveParser.OpenDriveParser()
    odp.parse_file(filename)
    # AS roadway object
    rw = Roadway()
    for (segid, r) in odp.data.roads
        if segid == roadIndex
            roadseg = RoadSegment{Float64}(segid)
            geom = r.planView[1]
            for sect in r.lanes.laneSection
                laneindex = 0
                for (id, lane) in sort(sect.right, rev=true)
                    if lane.type == "driving"
                        laneindex += 1
                        tag, curve = createCurve(segid, laneindex, geom, lane)
                        push!(roadseg.lanes, Lane(tag, curve, width=lane.width.a))
                    end
                end
                for (id, lane) in sort(sect.left)
                    if lane.type == "driving"
                        laneindex += 1
                        lane_width = lane.width.a
                        tag, curve = createCurve(segid, laneindex, geom, lane)
                        push!(roadseg.lanes, Lane(tag, curve, width=lane.width.a))
                    end
                end
            end
            push!(rw.segments, roadseg)
        end
    end
    return rw
end

# test data
roadway = OpenDriveToRoadwaysConverter("test_data/CarlaExs/Town01.xodr", 12)

open("test.txt", "w") do io
    write(io, roadway)
end

AutomotiveVisualization.colortheme["background"] = colorant"white"; # hide
camera = StaticCamera(position=VecE2(20,0.0), zoom=1, canvas_height=100)
snapshot = render([roadway], camera=camera)
