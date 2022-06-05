import Note from "./Notes"

import SWModels from "./SWModels"

function App(props) {
  return (
    <div className='App'>
      <Note />
      <SWModels h={props.h}/>
    </div>
  );
}

export default App;