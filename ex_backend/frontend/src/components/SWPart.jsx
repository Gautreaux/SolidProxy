
const colorbar = {
    width:"100%",
    height: "4px",
    backgroundColor: 'green',
}

function SWPart(props) {
    var c = null;

    if (props.model.rebuild_error) {
        c = {
            backgroundColor: 'red',
        };
    }

    return <div style={c}>
        <div style={colorbar}></div>
        <div>Bodies: {props.model.bodycount}</div>
        {/* TODO - body type? */}
        <div>Faces: {props.model.facecount}</div>
        <div>Has Rebuild Error: {props.model.rebuild_error.toString()}</div>
    </div>
}

export default SWPart