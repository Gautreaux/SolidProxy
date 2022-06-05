import React from 'react'
import './css/index.css'
import App from './components/App'

import {createRoot} from 'react-dom/client';
import axios from 'axios';

const container = document.getElementById('root');
const root = createRoot(container);

var old_h = 0;


function fetchH(){
  axios({
    method:"GET",
    url: 'swm_hash/',
  }).then((response) => {
    if(response.data.h !== old_h){
      let h = response.data.h
      console.log("NEW H:" + h);
      old_h = h
      root.render(<App h={h}/>)
    }
  }).catch((error) => {
    if (error.response) {
        console.log(error.response);
        console.log(error.response.status);
        console.log(error.response.headers);
    }
  }).finally(() => {
    setTimeout(fetchH, 1000)
  })
}

root.render(<App h={0}/>);

fetchH();