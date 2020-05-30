using PyCall
using AutomotiveSimulator
using AutomotiveVisualization

function createCurve(id, laneindex, r, y)
    tag = LaneTag(id,laneindex)
    curve = nothing
        if r.planView[1].type_name == "line"
            curve = gen_straight_curve(VecE2(0.0, y), VecE2(r.length, y), 10)
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
    for (i, r) in odp.data.roads
        if i == roadIndex
            roadseg = RoadSegment{Float64}(i)
            origin = VecSE2(0.0,0.0,0.0)
            for sect in r.lanes.laneSection
                laneindex = length(roadseg.lanes)
                y = 0
                for (id, lane) in sort(sect.right, rev=true)
                    if lane.type == "driving"
                        laneindex += 1
                        tag, curve = createCurve(id, laneindex, r, y)
                        y += lane.width.a
                        push!(roadseg.lanes, Lane(tag, curve, width=lane.width.a))
                    end
                end
                for (id, lane) in sort(sect.left)
                    if lane.type == "driving"
                        laneindex += 1
                        tag, curve = createCurve(id, laneindex, r, y)
                        y += lane.width.a
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
roadway = OpenDriveToRoadwaysConverter("test_data/OpenDriveExs/Ex_SingleLane.xodr", 1)

AutomotiveVisualization.colortheme["background"] = colorant"white"; # hide
camera = StaticCamera(position=VecE2(10,0.0), zoom=5, canvas_height=100)
snapshot = render([roadway], camera=camera)
