
const colorbar = {
    width:"100%",
    height: "4px",
    backgroundColor: 'green',
}

function SWPart(props) {
    return <div>
        <div style={colorbar}></div>
        <div>Bodies: {props.model.bodycount}</div>
        {/* TODO - body type? */}
        <div>Faces: {props.model.facecount}</div>
    </div>
}

export default SWPart