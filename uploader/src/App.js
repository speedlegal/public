import React from 'react';
/* import styled from 'styled-components'; */

/* const server = 'http://localhost:8080'; */
const server = 'https://model-zsairbvdca-uc.a.run.app';

const Uploader = () => (
  <form action={`${server}/upload/documents`} method="post" enctype = "multipart/form-data">
    <input type="file" name="files" accept=".pdf" multiple="multiple"/>
    <input type="submit"/>
  </form>
);

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          SpeedLegal Uploader
        </p>
      </header>
      <Uploader/>
    </div>
  );
}

export default App;
