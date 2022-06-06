
import SWPart from "./SWPart"
import SWAssembly from "./SWAssembly"

const modelTileStyles = {
    border: "2px solid black",
    display: "inline-block",
    maxWidth: "500px",
    minWidth: "300px",
    // aspectRatio: "1",
    margin: "5px",
    padding: "2px",
    position: "relative",
}

function SWModel (props) {
    var model = props.model

    var specialization = null;

    if (model.filetype === 0) {
        specialization = <div>swDocNone</div>
    }
    else if (model.filetype === 1) {
        specialization = <SWPart key={model.title} model={model}/>
    }else if (model.filetype === 2){
        specialization = <SWAssembly key={model.title} model={model}/>
    }else{
        specialization = <div>Unsupported Filetype: {model.filetype}</div>
    }

    return <div key={model.title} style={modelTileStyles}>
        <h3>{model.title}</h3>
        {specialization}
        <hr/>
    </div>
}

export default SWModel