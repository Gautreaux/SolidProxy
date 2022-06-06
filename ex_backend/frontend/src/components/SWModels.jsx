import { useState, useEffect } from "react";
import axios from "axios";

import SWModel from "./SWModel"

const wrapperStyles = {
    width: "100%",
    display: "flex",
    flexWrap: 'wrap',
}

function SWModels(props) {

    var h = props.h;

    const [swmodels, setNewModels] = useState(null);

    useEffect(() => {
        getModels()
    }, [h])

    function getModels() {
        axios({
            method: "GET",
            url: "/swmodels/"
        }).then((response) => {
            setNewModels(response.data)
        }).catch((error) => {
            if (error.response){
                console.log(error.response);
                console.log(error.response.status);
                console.log(error.response.headers);    
            }
        })
    }

    function _r(){
        // console.log(swmodels);
        if (swmodels && swmodels.length > 0) {
            return <div style={wrapperStyles}>
                {swmodels.map(swmodel => <SWModel
                    model={swmodel}
                    key={swmodel.title}
                />)}
            </div>
        } else {
            return <div key='no_models'>No Models are open</div>;
        }
    }

    function resetModels(){
        axios({
            method:"DELETE",
            url:"/swmodels/",
        }).catch((error) => {
            if (error.response){
                console.log(error.response);
                console.log(error.response.status);
                console.log(error.response.headers);    
            }
        })
    }

    console.log("Rendering for hash value: " + h)

    return <div>
        <h1>Currently Open Models:</h1>
        <sub>h value: {props.h}</sub><br></br>
        <button onClick={() => {resetModels()}}>Reset</button>
        <hr></hr>
        {_r()}
        </div>
}

export default SWModels;