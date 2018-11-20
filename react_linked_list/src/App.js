import React, { Component } from 'react';
import './App.css';
import { LinkedListComp } from './components/linkedlistcomp'

class App extends Component {
  render() {
    return (
      <div className="App">
          <header className="App-header">
              <h1> Linked List </h1> 
              <LinkedListComp />
        </header>
      </div>
    );
  }
}

export default App;
