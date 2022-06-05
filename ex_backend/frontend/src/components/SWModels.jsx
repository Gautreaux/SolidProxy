import { useState, useEffect } from "react";
import axios from "axios";

import SWModel from "./SWModel"


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
            return <div>
                {swmodels.map(swmodel => <SWModel
                    title={swmodel.title}
                    key={swmodel.title}
                />)}
            </div>
        } else {
            return <div key='no_models'>No Models are open</div>;
        }
    }

    console.log("Rendering for hash value: " + h)

    return <div>
        <div>h value: {props.h}</div>
        {_r()}
        </div>
}

export default SWModels;